from machine import ADC, Pin
import time

ADC_PIN = 4
VAPE_PIN = 5

adc = ADC(Pin(ADC_PIN))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

vape = Pin(VAPE_PIN, Pin.OUT, value=0)

MIN_START_DELTA = 120
MIN_STOP_DELTA = 60

ON_DEBOUNCE_MS = 80
OFF_DEBOUNCE_MS = 140

MIN_VALID_PUFF_MS = 400
MAX_PUFF_MS = 9000

STUCK_ON_FORCE_OFF_MS = 8000
COOLDOWN_MS = 250

SMOOTH_N = 16
LOOP_MS = 10

BOOT_BASELINE_SAMPLES = 420
BOOT_BASELINE_DELAY_MS = 3

IDLE_QUIET_MS = 300
IDLE_RECAL_SAMPLES = 160
IDLE_RECAL_SAMPLE_MS = 2

BASELINE_TRACK_ALPHA_NUM = 1
BASELINE_TRACK_ALPHA_DEN = 12
TRACK_MIN_MS = 15

MAX_PUFFS = 40
MAX_TOTAL_VAPE_MS = 150000

def now_ms():
    return time.ticks_ms()

def add_ms(t, ms):
    return time.ticks_add(t, ms)

def set_vape(x):
    vape.value(1 if x else 0)

def baseline_stats(n, delay_ms):
    s = 0
    mn = 1 << 30
    mx = 0
    for _ in range(n):
        x = adc.read()
        s += x
        if x < mn: mn = x
        if x > mx: mx = x
        time.sleep_ms(delay_ms)
    mean = s // n
    return mean, (mx - mn)

baseline, p2p0 = baseline_stats(BOOT_BASELINE_SAMPLES, BOOT_BASELINE_DELAY_MS)

noise = p2p0
if noise < 8:
    noise = 8

QUIET_BAND = max(22, noise * 2)
START_DELTA = max(MIN_START_DELTA, noise * 6)
STOP_DELTA = max(MIN_STOP_DELTA, noise * 3)

if STOP_DELTA >= START_DELTA:
    STOP_DELTA = START_DELTA - max(10, noise)

print("baseline:", baseline, "noise_p2p:", p2p0, "quiet:", QUIET_BAND, "start:", START_DELTA, "stop:", STOP_DELTA)

buf = [adc.read()] * SMOOTH_N
buf_i = 0
buf_sum = 0
for v in buf:
    buf_sum += v

def smooth_read():
    global buf_i, buf_sum
    x = adc.read()
    buf_sum -= buf[buf_i]
    buf[buf_i] = x
    buf_sum += x
    buf_i += 1
    if buf_i >= SMOOTH_N:
        buf_i = 0
    return buf_sum // SMOOTH_N

state_on = False
on_since = None
off_since = None
puff_start = 0
puff_counted = False
cooldown_until = 0

puffs = 0
total_ms = 0
locked = False

quiet_since = None
last_track = 0

def try_recalibrate():
    global baseline, quiet_since, last_track
    set_vape(False)
    time.sleep_ms(30)

    s = 0
    cnt = 0
    for _ in range(IDLE_RECAL_SAMPLES):
        x = smooth_read()
        d = x - baseline
        if d > QUIET_BAND or d < -QUIET_BAND:
            cnt = 0
            s = 0
            time.sleep_ms(IDLE_RECAL_SAMPLE_MS)
            continue
        s += x
        cnt += 1
        time.sleep_ms(IDLE_RECAL_SAMPLE_MS)

    if cnt >= (IDLE_RECAL_SAMPLES * 2) // 3:
        baseline = s // cnt
        quiet_since = None
        last_track = now_ms()
        print("recal:", baseline)

while True:
    t = now_ms()

    if locked:
        set_vape(False)
        time.sleep_ms(50)
        continue

    if time.ticks_diff(t, cooldown_until) < 0:
        set_vape(False)
        time.sleep_ms(LOOP_MS)
        continue

    r = smooth_read()
    d = r - baseline

    if not state_on:
        if d <= QUIET_BAND and d >= -QUIET_BAND:
            if quiet_since is None:
                quiet_since = t
            if time.ticks_diff(t, last_track) >= TRACK_MIN_MS:
                baseline += (d * BASELINE_TRACK_ALPHA_NUM) // BASELINE_TRACK_ALPHA_DEN
                last_track = t
            if time.ticks_diff(t, quiet_since) >= IDLE_QUIET_MS:
                try_recalibrate()
        else:
            quiet_since = None

        if d >= START_DELTA:
            if on_since is None:
                on_since = t
            elif time.ticks_diff(t, on_since) >= ON_DEBOUNCE_MS:
                state_on = True
                set_vape(True)
                puff_start = t
                puff_counted = False
                on_since = None
                off_since = None
                quiet_since = None
                print("PUFF START")
        else:
            on_since = None

    else:
        puff_ms = time.ticks_diff(t, puff_start)

        if (not puff_counted) and puff_ms >= MIN_VALID_PUFF_MS:
            puff_counted = True
            puffs += 1
            print("PUFF COUNT", puffs)
            if puffs >= MAX_PUFFS:
                locked = True
                set_vape(False)
                print("LOCK max puffs")
                continue

        if puff_ms >= MAX_PUFF_MS:
            state_on = False
            set_vape(False)
            if puff_counted:
                total_ms += puff_ms
            cooldown_until = add_ms(t, COOLDOWN_MS)
            puff_counted = False
            on_since = None
            off_since = None
            print("PUFF END timeout", puff_ms, total_ms)
            if total_ms >= MAX_TOTAL_VAPE_MS:
                locked = True
                print("LOCK max total")
            continue

        if puff_ms >= STUCK_ON_FORCE_OFF_MS:
            state_on = False
            set_vape(False)
            cooldown_until = add_ms(t, COOLDOWN_MS + 150)
            if puff_counted:
                total_ms += puff_ms
            puff_counted = False
            on_since = None
            off_since = None
            print("FORCE OFF", puff_ms, d, total_ms)
            try_recalibrate()
            time.sleep_ms(LOOP_MS)
            continue

        if d <= STOP_DELTA:
            if off_since is None:
                off_since = t
            elif time.ticks_diff(t, off_since) >= OFF_DEBOUNCE_MS:
                state_on = False
                set_vape(False)
                if puff_counted:
                    total_ms += puff_ms
                cooldown_until = add_ms(t, COOLDOWN_MS)
                puff_counted = False
                on_since = None
                off_since = None
                print("PUFF END pressure", puff_ms, total_ms)
                if total_ms >= MAX_TOTAL_VAPE_MS:
                    locked = True
                    print("LOCK max total")
        else:
            off_since = None

    time.sleep_ms(LOOP_MS)

