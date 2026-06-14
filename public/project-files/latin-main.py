import pygame
from bs4 import BeautifulSoup
import requests
import random
import math
import time

shake = False

def check_word(word, found_words):
    if len(word) <= 3 or letters[6] not in word or word in found_words:
        return False

    for char in word:
        if char not in letters:
            return False

    url = "https://www.perseus.tufts.edu/hopper/morph"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    params = {
        "l": word,
        "la": "la"
    }
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)

        if response.status_code == 429:
            time.sleep(0.1)
            return check_word(word, letters[6])

        if response.status_code != 200:
            return False

        soup = BeautifulSoup(response.content, "html.parser")
        word_freq_element = soup.find("a", href=True, string="Word frequency statistics")
        return word_freq_element is not None

    except requests.exceptions.RequestException:
        return False

pygame.init()

WIDTH, HEIGHT = 800, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Latin Spelling Bee")

font_Header = pygame.font.Font(None, 20)
font_large = pygame.font.Font(None, 72)
font_medium = pygame.font.Font(None, 48)
font_small = pygame.font.Font(None, 15)
font = pygame.font.Font(None, 36)

circle_spacing = 40
circle_radius = 8  
yellow_circle_radius = 12 
square_size = 18  
start_x = 485
start_y = 160
num_circles = 8

score = 0
score_step = 10
current_circle = 0
target_circle = 0
animation_progress = 0.0
animation_speed = 0.05

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LGRAY = (228, 228, 228)
DGRAY = (72, 72, 72)
MYELLOW = (253, 221, 7)
DARK_GRAY = (169, 169, 169)

cursor_visible = True
cursor_timer = 0
shake_time = 0
shake_duration = 200
shake_amplitude = 10

latin_letters = ["A", "E", "I", "O", "U", "C", "L", "M", "N", "P", "R", "S", "T"]
vowels = ["A", "E", "I", "O", "U"]
center_letter = random.choice(vowels)
other_letters = random.sample([l for l in latin_letters if l != center_letter], 6)
letters = [center_letter] + other_letters
random.shuffle(letters)

found_words = set()
input_word = ""
clock = pygame.time.Clock()
input_box_rect = pygame.Rect(WIDTH // 2 - 150, 40, 300, 50)

hex_positions = [
    (WIDTH // 2 - 70 - 150 - 80, HEIGHT // 2 - 41 + 100 - 30 - 30 + 50 - 40 - 20),
    (WIDTH // 2 - 150 - 80, HEIGHT // 2 - 80 + 100 - 30 - 30 + 50 - 40 - 20),
    (WIDTH // 2 + 70 - 150 - 80, HEIGHT // 2 - 41 + 100 - 30 - 30 + 50 - 40 - 20),
    (WIDTH // 2 - 70 - 150 - 80, HEIGHT // 2 + 41 + 100 - 30 - 30 + 50 - 40 - 20),
    (WIDTH // 2 - 150 - 80, HEIGHT // 2 + 80 + 100 - 30 - 30 + 50 - 40 - 20),
    (WIDTH // 2 + 70 - 150 - 80, HEIGHT // 2 + 41 + 100 - 30 - 30 + 50 - 40 - 20),
    (WIDTH // 2 - 150 - 80, HEIGHT // 2 + 100 - 30 - 30 + 50 - 40 - 20)
]

button_width = 100
button_height = 50
button_radius = 10
enter_button_rect = pygame.Rect(WIDTH // 2 - 160, HEIGHT - 100, button_width, button_height)
reshuffle_button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 100, button_width, button_height)
delete_button_rect = pygame.Rect(WIDTH // 2 + 60, HEIGHT - 100, button_width, button_height)

# Animation variables
animation_message = ""
animation_y = 0
animation_active = False

def draw_word_box():
    box_x = 400
    box_y = 180
    box_width = 380
    box_height = 400
    border_thickness = 1
    border_radius = 20

    pygame.draw.rect(screen, LGRAY, (box_x, box_y, box_width, box_height), border_thickness, border_radius)

    header = f"You have found {len(found_words)} words"
    header_text = font_Header.render(header, True, DGRAY)
    screen.blit(header_text, (box_x + 10, box_y + 10))

    font_size = max(30 - len(found_words) * 2, 12)
    font_dynamic = pygame.font.Font(None, font_size)

    line_y = box_y + 50
    for word in found_words:
        word_text = font_dynamic.render(word, True, BLACK)
        screen.blit(word_text, (box_x + 10, line_y))

        line_start = (box_x + 10, line_y + word_text.get_height() + 5)
        line_end = (box_x + 10 + word_text.get_width() // 3, line_y + word_text.get_height() + 5)
        dash_length = 80
        for i in range(line_start[0], line_end[0], dash_length * 2):
            pygame.draw.line(screen, LGRAY, (i, line_start[1]), (i + dash_length, line_start[1]), 2)

        line_y += word_text.get_height() + 15

def render_input_word():
    global cursor_timer, cursor_visible, shake_time, input_word, shake_offset, shake, animation_y, animation_active
    font_size = max(70 - len(input_word) * 2, 22)
    font_dynamic = pygame.font.Font(None, font_size)

    if shake_time > 0:
        shake_offset = math.sin(shake_time / 100) * shake_amplitude
        shake = True
        shake_time -= clock.get_time()
    else:
        shake = False
        shake_offset = 0

    x_offset = WIDTH // 2 - 150 + 10 + shake_offset

    if input_word:
        for char in input_word:
            if char in letters:
                color = YELLOW if char == letters[6] else BLACK
            else:
                color = GRAY

            char_text = font_dynamic.render(char, True, color)
            screen.blit(char_text, (x_offset - 120, 60))
            x_offset += char_text.get_width()
    else:
        placeholder_text = font_dynamic.render("Type something", True, GRAY)
        screen.blit(placeholder_text, (x_offset - 120, 60))

    cursor_timer += clock.get_time()
    if cursor_timer >= 1000:
        cursor_visible = not cursor_visible
        cursor_timer = 0
    if cursor_visible:
        cursor_width = max(font_size // 20, 2)
        cursor_height = max(font_size // 11, 2)

        cursor_x = x_offset
        cursor_y = input_box_rect.y + 15

        pygame.draw.line(screen, YELLOW, (cursor_x - 120, cursor_y), (cursor_x - 120, cursor_y + cursor_height * 10), cursor_width)

    if animation_active:
        animation_text = font_medium.render(animation_message, True, BLACK)
        screen.blit(animation_text, (WIDTH // 2 - animation_text.get_width() // 2, animation_y))
        animation_y -= 1
        if animation_y < 10:
            animation_active = False

hex_size = 50

def draw_hexagon(surface, color, position, size):
    x, y = position
    points = [
        (x + size * math.cos(math.radians(angle)), y + size * math.sin(math.radians(angle)))
        for angle in range(0, 360, 60)
    ]
    inner_size = size - 5
    inner_points = [
        (x + inner_size * math.cos(math.radians(angle)), y + inner_size * math.sin(math.radians(angle)))
        for angle in range(0, 360, 60)
    ]
    pygame.draw.polygon(surface, color, inner_points)

isShaking = False

def get_letter_from_click(mouse_pos):
    for i, pos in enumerate(hex_positions):
        x, y = pos
        dx, dy = mouse_pos[0] - x, mouse_pos[1] - y
        distance = math.sqrt(dx * dx + dy * dy)
        if distance <= hex_size:
            return i
    return None

def reshuffle_letters():
    global letters
    center_letter = letters[6]
    other_letters = letters[:6] + letters[7:]
    random.shuffle(other_letters)
    letters = other_letters[:6] + [center_letter] + other_letters[6:]

def show_end_screen():
    screen.fill(WHITE)
    end_text = font_large.render("Congratulations!", True, BLACK)
    score_text = font_medium.render(f"Your Score: {score}", True, BLACK)
    screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 + 10))
    pygame.display.flip()
    pygame.time.wait(3000)

running = True
hex_scale = [1] * 7
hex_scale_time = [0] * 7

text_labels = [
    ("Genius", 80),
    ("Amazing", 70),
    ("Great", 60),
    ("Nice", 50),
    ("Solid", 40),
    ("Good", 30),
    ("Moving Up", 20),
    ("Good Start", 10),
    ("Beginner", 0)
]

while running:
    screen.fill(WHITE)
    
    for label, min_score in text_labels:
        if score >= min_score:
            text_surface = font_small.render(label, True, BLACK)
            screen.blit(text_surface, (415, 155))
            break
    for i in range(num_circles - 1):
        line_start_x = start_x - 30 + i * circle_spacing + circle_spacing // 2
        pygame.draw.line(screen, LGRAY, (line_start_x, start_y), (line_start_x + circle_spacing, start_y), 2)
    for i in range(num_circles):
        if i == num_circles - 1:
            pygame.draw.rect(screen, GRAY, (start_x + i * circle_spacing - square_size // 2, start_y - square_size // 2, square_size, square_size))
        else:
            pygame.draw.circle(screen, GRAY, (start_x + i * circle_spacing, start_y), circle_radius)
        if target_circle > current_circle:
            animation_progress += animation_speed
            if animation_progress >= 1.0:
                animation_progress = 0.0
                current_circle += 1
        if target_circle > current_circle:
            start_pos = start_x + current_circle * circle_spacing
            end_pos = start_x + target_circle * circle_spacing
            yellow_x = int(start_pos + (end_pos - start_pos) * animation_progress)
        else:
            yellow_x = start_x + current_circle * circle_spacing

        if current_circle == num_circles - 1:
            pygame.draw.rect(screen, MYELLOW, (yellow_x - square_size // 2, start_y - square_size // 2, square_size, square_size))
        else:
            pygame.draw.circle(screen, MYELLOW, (yellow_x, start_y), yellow_circle_radius)
        
        score_text = font_small.render(str(score), True, BLACK)
        text_rect = score_text.get_rect(center=(yellow_x, start_y))
        screen.blit(score_text, text_rect)    

    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    def draw_button(rect, text, is_pressed):
        color = DARK_GRAY if is_pressed else LGRAY
        pygame.draw.rect(screen, color, rect, border_radius=button_radius)
        text_surface = font_small.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)

    draw_button(enter_button_rect, "Enter", enter_button_rect.collidepoint(mouse_pos) and mouse_pressed[0])
    draw_button(reshuffle_button_rect, "Reshuffle", reshuffle_button_rect.collidepoint(mouse_pos) and mouse_pressed[0])
    draw_button(delete_button_rect, "Delete", delete_button_rect.collidepoint(mouse_pos) and mouse_pressed[0])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                continue
            if event.key == pygame.K_BACKSPACE:
                input_word = input_word[:-1]
            elif event.key == pygame.K_RETURN:
                if check_word(input_word, found_words):
                    found_words.add(input_word)
                    points = len(input_word)
                    score += points
                    if points > 4:
                        animation_message = f"Amazing +{points}"
                    else:
                        animation_message = f"Good +{points}"
                    animation_y = 60
                    animation_active = True
                    if (score >= 10 and score <= 20) and target_circle == 0 or (score >= 20 and score <= 30)and target_circle == 1 or (score >= 30 and score <= 40) and target_circle == 2 or (score >= 40 and score <= 50) and target_circle == 3 or (score >= 50 and score <= 60) and target_circle == 4 or (score >= 60 and score <= 70) and target_circle == 5 or (score >= 70 and score <= 80)and target_circle == 6:
                        target_circle += 1
                    if score >= 80:
                        show_end_screen()
                        running = False
                else:
                    if input_word == "":
                        shaking = False
                    else:
                        shaking = True
                        shake_time = shake_duration
            else:
                input_word += event.unicode.upper()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if enter_button_rect.collidepoint(event.pos):
                if check_word(input_word, found_words):
                    found_words.add(input_word)
                    points = len(input_word)
                    score += points
                    if points > 4:
                        animation_message = f"Amazing +{points}"
                    else:
                        animation_message = f"Good +{points}"
                    animation_y = 60
                    animation_active = True
                    if (score >= 10 and score <= 20) and target_circle == 0 or (score >= 20 and score <= 30)and target_circle == 1 or (score >= 30 and score <= 40) and target_circle == 2 or (score >= 40 and score <= 50) and target_circle == 3 or (score >= 50 and score <= 60) and target_circle == 4 or (score >= 60 and score <= 70) and target_circle == 5 or (score >= 70 and score <= 80)and target_circle == 6:
                        target_circle += 1
                    if score >= 80:
                        show_end_screen()
                        running = False
                else:
                    if input_word == "":
                        shaking = False
                    else:
                        shaking = True
                        shake_time = shake_duration
            elif reshuffle_button_rect.collidepoint(event.pos):
                reshuffle_letters()
            elif delete_button_rect.collidepoint(event.pos):
                input_word = ""
            else:
                hex_index = get_letter_from_click(event.pos)
                if hex_index is not None:
                    input_word += letters[hex_index]
                    hex_scale[hex_index] = 0.8
                    hex_scale_time[hex_index] = pygame.time.get_ticks()
            
        
    if shake_time > 0 and not isShaking:
        isShaking = True
    elif shake_time <= 0 and input_word != "" and isShaking:
        isShaking = False
        input_word = ""

    for i in range(7):
        if hex_scale_time[i] > 0 and pygame.time.get_ticks() - hex_scale_time[i] > 200:
            hex_scale[i] = 1
            hex_scale_time[i] = 0

    for i, pos in enumerate(hex_positions):
        color = MYELLOW if i == 6 else LGRAY
        draw_hexagon(screen, color, pos, hex_size * hex_scale[i])
        letter = letters[i]
        text = font.render(letter, True, BLACK)
        screen.blit(text, (pos[0] - text.get_width() // 2, pos[1] - text.get_height() // 2))

    input_text = font_medium.render(input_word, True, BLACK)
    render_input_word()

    draw_word_box()
    pygame.display.flip()
    clock.tick(60)
    cursor_timer += clock.get_time()

pygame.quit()
