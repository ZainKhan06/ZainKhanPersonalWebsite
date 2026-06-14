<script setup>
import hardwareBoard from './assets/hardware-board.jpg';
import isaNotes from './assets/isa-notes.jpg';
import logicAnalyzer from './assets/logic-analyzer.jpg';
import profilePhoto from './assets/zain-profile.png';
import assistiveArmCamera from './assets/assistive-arm-camera.jpg';
import assistiveArmMounted from './assets/assistive-arm-mounted.jpg';
import instructionSetSvg from './assets/cpu-schematic.png';
import smartpipeCode from './assets/smartpipe-code.jpg';
import smartpipeHardware from './assets/smartpipe-hardware.jpg';
import smartpipeAppNotes from './assets/smartpipe-app-notes.jpg';
import smartpipeAppPlan from './assets/smartpipe-app-plan.jpg';
import smartpipeAppReminder from './assets/smartpipe-app-reminder.png';
import smartpipeAppSettings from './assets/smartpipe-app-settings.jpg';
import smartpipeAppTracking from './assets/smartpipe-app-tracking.jpg';
import programmatic1 from './assets/IMG_9554.PNG';
import programmatic2 from './assets/IMG_9555.PNG';
import programmatic3 from './assets/IMG_9556.PNG';
import programmatic4 from './assets/IMG_9557.PNG';
import programmatic5 from './assets/IMG_9558.PNG';
import programmatic6 from './assets/IMG_9559.PNG';
import programmatic7 from './assets/IMG_9560.PNG';


const linkedinUrl = 'https://www.linkedin.com/in/zain-khan-88a352259/';
const nonprofitRepoUrl = 'https://github.com/ZShirwani/Final';
const fileBase = import.meta.env.BASE_URL + 'project-files/';

const programmaticPhotos = [
  { src: programmatic1, alt: 'Programmatics students building Raspberry Pi LED circuits on breadboards' },
  { src: programmatic2, alt: 'Student wiring a Raspberry Pi and breadboard circuit during Programmatics class' },
  { src: programmatic3, alt: 'Group of Programmatics students collaborating on electronics and Raspberry Pi circuits' },
  { src: programmatic4, alt: 'Programmatics students testing LED circuits with jumper wires and Raspberry Pi' },
  { src: programmatic5, alt: 'Programmatics class working around a table on circuits and Raspberry Pi hardware' },
  { src: programmatic6, alt: 'Student testing a working LED circuit in Programmatics class' },
  { src: programmatic7, alt: 'Programmatics students learning electronics with Raspberry Pi, breadboards, and LEDs' },
];


const projects = [
  {
    title: 'Custom 16-Bit Computer',
    category: 'Computer architecture',
    body: 'Built a 16-bit computer from logic gates up, then wrote the assembler, compiler, and language needed to run programs on it. The final goal was getting Tetris working on a computer I built from the ground up.',
    repoUrl: 'https://github.com/ZainKhan06/hack-app',
    details: ['NAND, NOT, AND, OR, XOR, multiplexers, and demultiplexers', 'ALU arithmetic, bitwise operations, comparisons, and conditional execution support', 'Program counter, instruction register, registers, control unit, memory interface, and jump logic', 'RAM, ROM, memory mapping, instruction storage, and data storage', 'Custom ISA, assembler symbol resolution, compiler code generation, and graphics output'],
    images: [
      {
        src: instructionSetSvg,
        alt: 'Nand2Tetris custom 16-bit computer instruction set reference',
        label: 'Instruction set reference',
      },
      {
        src: logicAnalyzer,
        alt: 'Logic analyzer showing digital timing signals from the custom computer project',
        label: 'Signal verification',
      },
    ],
    code: [
      {
        label: 'HackAssembler.py',
        text: 'comp_table = { "D+A": "0000010", "D-A": "0010011", "D&M": "1000000" }\nnext_variable_address = 16\noutput_lines.append(binary_instruction)',
      },
      {
        label: 'CPU.hdl',
        text: 'ALU(x=Dout, y=AMout, zx=instruction[11], nx=instruction[10],\n    zy=instruction[9], ny=instruction[8], f=instruction[7], no=instruction[6],\n    out=ALUout, zr=ZRout, ng=NGout);',
      },
    ],
    files: [
      { label: 'HackAssembler.py', href: `${fileBase}HackAssembler.py`, download: 'HackAssembler.py' },
      { label: 'Assembler README', href: `${fileBase}hack-assembler-README.md`, download: 'hack-assembler-README.md' },
      { label: 'CPU.hdl', href: `${fileBase}CPU.hdl`, download: 'CPU.hdl' },
      { label: 'ALU.hdl', href: `${fileBase}ALU.hdl`, download: 'ALU.hdl' },
    ],
  },
  {
    title: 'Jack Compiler',
    category: 'Compiler design',
    body: 'Built a Python compiler for Jack programs that translates higher-level code into VM code. It handles parsing, variables, control flow, and code generation.',
    repoUrl: null,
    details: ['Jack tokenization and syntax analysis', 'Recursive descent compilation engine', 'Symbol table scopes for variables and subroutines', 'VM writer for generated code', 'Folder or single-file compilation'],
    code: [
      {
        label: 'JackCompiler.py',
        text: 'if os.path.isdir(path):\n    for filename in os.listdir(path):\n        if filename.endswith(".jack"):\n            compile_file(os.path.join(path, filename))',
      },
    ],
    files: [
      { label: 'jack-compiler.zip', href: `${fileBase}jack-compiler.zip`, download: 'jack-compiler.zip' },
    ],
  },
  {
    title: 'Yale Hackathon — Assistive Arm + Voice Navigation',
    category: 'Hackathon / Assistive Technology',
    body: 'Yale hackathon project combining an assistive robotic arm concept with a voice navigation app. The idea was to support accessibility through simple robotics, sensing, and spoken directions.',
    repoUrl: 'https://github.com/ZainKhan06/SenseTrack',
    details: [
      'Combined the assistive robotic arm and voice navigation app into one hackathon project',
      'Designed for accessibility, navigation support, and physical interaction with the environment',
      'Used rapid prototyping to move from concept to demo under hackathon time constraints',
      'Explored robotics, sensing, mobile UX, and assistive technology in one integrated build',
      'Created a voice-first navigation experience that gives clear spoken directions and guidance',
    ],
    images: [
      {
        src: assistiveArmMounted,
        alt: 'Wearable assistive robotic arm mounted on a prototype board',
        label: 'Assistive arm prototype',
      },
      {
        src: assistiveArmCamera,
        alt: 'Assistive prototype with camera and servo assembly',
        label: 'Camera and servo rig',
      },
    ],
  },
  {
    title: 'Wi-Fi Robot Car',
    category: 'Robotics',
    body: 'Built a Raspberry Pi robot car controlled over Wi-Fi from a custom iPhone app. The app used the phone gyroscope like a steering wheel, letting the car respond to tilt-based steering while also streaming a live camera feed for remote navigation.',
    repoUrl: null,
    details: [
      'Raspberry Pi 5 with L298N motor driver and dual-motor drive',
      'Custom iPhone app connected to the robot over Wi-Fi',
      'Phone gyroscope control so tilting the phone steers the car like a steering wheel',
      'Python TCP server for real-time movement commands',
      'Live camera feed streamed from the robot for remote navigation',
      'GPIO setup, PWM motor tuning, motor wiring, TCP debugging, and camera stream configuration',
      'Demo video is shown at 2x speed',
    ],
    video: {
      src: `${import.meta.env.BASE_URL}videos/robot-car-demo.mp4`,
      caption: 'Robot car demo shown at 2x speed.',
    },
  },
  {
    title: 'SmartPipe',
    category: 'Product concept',
    body: 'Early-stage hardware and mobile app project for helping users reduce vaping. The system combines device sensing, app tracking, reminders, notes, analytics, and coaching features.',
    repoUrl: 'Private repo',
    details: ['ADC-based puff sensing with debounced start/stop detection', 'Adaptive baseline recalibration and safety lockouts for max puffs and total use', 'Flutter app concepts for authentication, dashboard, progress monitoring, goals, and analytics', 'Weekly, monthly, and long-term trend views', 'BLE connectivity, data synchronization, haptics, notes, reminders, and AI coaching'],
    code: [
      {
        label: 'SmartPipe.py',
        text: 'START_DELTA = max(MIN_START_DELTA, noise * 6)\nSTOP_DELTA = max(MIN_STOP_DELTA, noise * 3)\nif puffs >= MAX_PUFFS:\n    locked = True',
      },
    ],
    images: [
      {
        src: smartpipeHardware,
        alt: 'SmartPipe prototype electronics with microcontroller, battery, and sensors',
        label: 'Prototype electronics',
      },
      {
        src: smartpipeCode,
        alt: 'SmartPipe code showing puff tracking and debug output',
        label: 'Tracking software',
      },
      {
        src: smartpipeAppSettings,
        alt: 'SmartPipe app settings screen with Bluetooth, haptics, and daily goals',
        label: 'App settings',
      },
      {
        src: smartpipeAppTracking,
        alt: 'SmartPipe app tracking screen with session controls and usage stats',
        label: 'Session tracking',
      },
      {
        src: smartpipeAppPlan,
        alt: 'SmartPipe app plan screen with daily hit goal and quitting timeline',
        label: 'Adaptive plan',
      },
      {
        src: smartpipeAppNotes,
        alt: 'SmartPipe app notes modal',
        label: 'Notes modal',
      },
      {
        src: smartpipeAppReminder,
        alt: 'SmartPipe app notes screen with reminder set',
        label: 'Reminders',
      },
    ],
    files: [
      { label: 'SmartPipe.py', href: `${fileBase}SmartPipe.py`, download: 'SmartPipe.py' },
    ],
  },
  {
    title: 'AI Servo Light Switch',
    category: 'Automation',
    body: 'Built a servo-based light switch system that can physically turn a standard wall switch on and off using Raspberry Pi control.',
    repoUrl: null,
    details: ['Servo motor and controller board', 'Mechanical linkage for switch activation', 'Environmental-condition detection and actuation logic', 'Mechanical alignment, actuation force, reliability, and safety considerations'],
  },
  {
    title: 'Latin Wordle',
    category: 'Educational game',
    body: 'Made a Wordle-style game for practicing Latin vocabulary with guesses, feedback, validation, and scoring.',
    repoUrl: null,
    details: ['Daily-style word challenges', 'Letter-position feedback', 'Latin vocabulary acquisition', 'Word database, guess validation, feedback engine, and scoring system'],
  },
  {
    title: 'Epic Latin Game',
    category: 'Python/Pygame',
    body: 'Built a Python/Pygame Latin practice game with vocabulary challenges, feedback, and a simple game loop.',
    repoUrl: 'https://github.com/ZainKhan06/EpicLatinGame',
    details: ['Python and Pygame', 'Vocabulary practice and interactive challenges', 'Student feedback and progress reinforcement', 'Event-driven programming, graphical UI, and game loop architecture'],
    code: [
      {
        label: 'main.py',
        text: 'def check_word(word, found_words):\n    if len(word) <= 3 or letters[6] not in word:\n        return False\n    response = requests.get("https://www.perseus.tufts.edu/hopper/morph", params={"l": word, "la": "la"})',
      },
    ],
    files: [
      { label: 'main.py', href: `${fileBase}latin-main.py` },
    ],
  },
  {
    title: 'Programmatics Website',
    category: 'Nonprofit web development',
    body: 'Designed and maintained the Programmatics website to show the nonprofit’s programs, mission, outreach, and student impact.',
    repoUrl: nonprofitRepoUrl,
    details: ['Built web pages for a real student-led nonprofit', 'Highlighted electronics, Raspberry Pi, coding, and community programs', 'Supported outreach and accessibility for students and families', 'Connected technical work with nonprofit leadership and education'],
  },
  {
    title: 'Lipid Bilayer Website',
    category: 'Science education',
    body: 'Built a biology website explaining lipid bilayers and cell membrane concepts with clear visuals for students.',
    repoUrl: null,
    details: ['Phospholipids and membrane structure', 'Membrane transport, diffusion, and cell structure', 'Interactive visuals and student-friendly explanations', 'Scientific communication and educational design'],
  },
];

const skills = [
  'Computer Architecture',
  'Digital Logic',
  'CPU Design',
  'Embedded Systems',
  'Robotics',
  'Motor Control',
  'SwiftUI',
  'Flutter',
  'BLE',
  'Networking',
  'Compiler Design',
  'Programming Language Design',
  'Data Analytics',
  'Mechatronics',
  'Assistive Technology',
  'Accessibility',
  'Hackathons',
  'Python',
  'Pygame',
  'STEM Education',
  'Leadership',
  'Public Speaking',
  'Curriculum Design',
  'Project Management',
];
</script>

<template>
  <main>
    <nav class="topbar" aria-label="Primary navigation">
      <a class="brand" href="#">Zain Khan</a>
      <div>
        <a href="#computer">Computer</a>
        <a href="#projects">Projects</a>
        <a href="#impact">Impact</a>
        <a :href="linkedinUrl" target="_blank" rel="noreferrer">LinkedIn</a>
      </div>
    </nav>

    <section class="hero" aria-labelledby="hero-title">
      <div class="hero-panel">
        <img class="portrait" :src="profilePhoto" alt="Zain Khan" />
        <p class="intro">Electrical engineering & robotics builder | Embedded systems | STEM educator</p>
        <h1 id="hero-title">Engineering projects, robotics, and STEM education.</h1>
        <p class="hero-copy">
          I focus on practical engineering projects: embedded systems, robotics, digital logic, mobile apps, and hands-on STEM programs for younger students.
        </p>
        <div class="hero-links">
          <a href="#computer">Flagship build</a>
          <a href="#projects">Project details</a>
          <a :href="linkedinUrl" target="_blank" rel="noreferrer">LinkedIn</a>
        </div>
      </div>
      <div class="hero-metrics" aria-label="Portfolio highlights">
        <div>
          <strong>16-bit</strong>
          <span>custom computer</span>
        </div>
        <div>
          <strong>60+</strong>
          <span>students taught</span>
        </div>
        <div>
          <strong>Full-stack</strong>
          <span>hardware to apps</span>
        </div>
      </div>
    </section>

    <section id="computer" class="showcase">
      <div class="showcase-copy">
        <p class="eyebrow">Flagship project</p>
        <h2>Custom 16-Bit Computer</h2>
        <p>
          A complete 16-bit computer project built from logic gates through CPU design, assembler, compiler, graphics, and Tetris.
        </p>
      </div>
      <div class="device-frame">
        <img :src="instructionSetSvg" alt="Hack instruction set diagram" />
      </div>
    </section>

    <section class="image-story" aria-label="Custom computer project evidence">
      <figure class="wide-photo">
        <img :src="logicAnalyzer" alt="Logic analyzer showing digital timing signals" />
        <figcaption>Signal verification on real hardware.</figcaption>
      </figure>
      <div class="stacked-photos">
        <figure>
          <img :src="isaNotes" alt="Notebook page with custom instruction set notes" />
          <figcaption>Instruction set notes.</figcaption>
        </figure>
        <figure>
          <img :src="hardwareBoard" alt="Wired hardware setup with boards and cables" />
          <figcaption>Hardware bench.</figcaption>
        </figure>
      </div>
    </section>

    <section id="projects" class="projects">
      <div class="section-title">
        <p class="eyebrow">Selected work</p>
        <h2>Projects</h2>
      </div>
      <div class="project-list">
        <article v-for="project in projects" :key="project.title">
          <details>
            <summary>
              <span class="project-category">{{ project.category }}</span>
              <h3>{{ project.title }}</h3>
              <p>{{ project.body }}</p>
              <span class="expand-label">Open details</span>
            </summary>
            <div class="project-detail">
              <div class="repo-row">
                <a
                  v-if="project.repoUrl && project.repoUrl.startsWith('https')"
                  class="repo-link"
                  :href="project.repoUrl"
                  target="_blank"
                  rel="noreferrer"
                >
                  View repo
                </a>
                <span v-else-if="project.repoUrl" class="repo-note">{{ project.repoUrl }}</span>
                <span v-else class="repo-note">Repo not published yet</span>
              </div>

              <ul>
                <li v-for="detail in project.details" :key="detail">{{ detail }}</li>
              </ul>

              <div v-if="project.images" class="project-media">
                <figure v-for="image in project.images" :key="image.label">
                  <img :src="image.src" :alt="image.alt" />
                  <figcaption>{{ image.label }}</figcaption>
                </figure>
              </div>


              <div v-if="project.video" class="project-video">
                <video controls playsinline preload="metadata">
                  <source :src="project.video.src" type="video/mp4" />
                  Your browser does not support the video tag.
                </video>
                <p>{{ project.video.caption }}</p>
              </div>

              <div v-if="project.code" class="code-samples">
                <div v-for="sample in project.code" :key="sample.label">
                  <span>{{ sample.label }}</span>
                  <pre><code>{{ sample.text }}</code></pre>
                </div>
              </div>

              <div v-if="project.files" class="file-links">
                <a v-for="file in project.files" :key="file.label" :href="file.href" :download="file.download || file.label">
                  {{ file.label }}
                </a>
              </div>
            </div>
          </details>
        </article>
      </div>
    </section>

    <section id="impact" class="impact">
      <div>
        <p class="eyebrow">Programmatic STEM Nonprofit</p>
        <h2>Programmatics</h2>
        <p>
          Co-founded and led Programmatics, a student-run STEM nonprofit that teaches younger students through hands-on projects. The program covers electronics, circuits, Raspberry Pi systems, GPIO, sensors, LEDs, Python hardware control, Scratch, and Unity.
        </p>
        <ul class="impact-details">
          <li>Reached 60+ students through Goodnow Library, Curtis Middle School, and Stow programs.</li>
          <li>Designed hands-on lessons on voltage, current, pinouts, breadboards, GPIO, sensors, LEDs, and Python-based hardware control.</li>
          <li>Guided students through wiring, debugging, and integrating physical electronics with software.</li>
          <li>Built outreach material and maintained the nonprofit website to explain programs, mission, and community impact.</li>
          <li>Supported local community work through Sustainable Sudbury and environmental cleanup initiatives.</li>
        </ul>
        <a class="impact-link" :href="nonprofitRepoUrl" target="_blank" rel="noreferrer">
          View nonprofit repo
        </a>
      </div>
      <div class="programmatic-gallery">
        <figure v-for="photo in programmaticPhotos" :key="photo.src">
          <img :src="photo.src" :alt="photo.alt" />
        </figure>
      </div>
    </section>

    <section class="skills" aria-label="Technical skills">
      <span v-for="skill in skills" :key="skill">{{ skill }}</span>
    </section>

    <footer class="footer">
      <p>Connect with me on LinkedIn.</p>
      <a :href="linkedinUrl" target="_blank" rel="noreferrer">linkedin.com/in/zain-khan-88a352259</a>
    </footer>
  </main>
</template>
