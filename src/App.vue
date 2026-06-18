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
const currentGithubUrl = 'https://github.com/ZainKhan06';
const oldGithubUrl = 'https://github.com/ZainKhansn';
const nonprofitRepoUrl = 'https://github.com/ZShirwani/Final';
const cellMembraneRepoUrl = 'https://github.com/ZainKhansn/cellmembranewebsite';
const fileBase = import.meta.env.BASE_URL + 'project-files/';

const programmaticPhotos = [programmatic1, programmatic2, programmatic3, programmatic4, programmatic5, programmatic6, programmatic7];

const projects = [
  {
    title: 'Custom 16-Bit Computer',
    category: 'Computer architecture',
    body: 'Built a 16-bit computer from logic gates up, then wrote the assembler, compiler, and language needed to run programs on it. The final goal was getting Tetris working on a computer I built from the ground up.',
    repoUrl: 'https://github.com/ZainKhan06/hack-app',
    details: ['Logic gates, ALU, CPU, registers, RAM, ROM, control unit, memory mapping, assembler, compiler, graphics output, and Tetris.'],
    images: [
      { src: instructionSetSvg, alt: 'Nand2Tetris custom 16-bit computer instruction set reference', label: 'Instruction set reference' },
      { src: hardwareBoard, alt: 'Custom computer hardware wiring and board setup', label: 'Hardware build' },
      { src: isaNotes, alt: 'Handwritten instruction set and computer architecture notes', label: 'Architecture notes' },
      { src: logicAnalyzer, alt: 'Logic analyzer showing timing signals', label: 'Signal verification' },
    ],
    code: [
      { label: 'HackAssembler.py', text: 'comp_table = { "D+A": "0000010", "D-A": "0010011", "D&M": "1000000" }\nnext_variable_address = 16\noutput_lines.append(binary_instruction)' },
      { label: 'CPU.hdl', text: 'ALU(x=Dout, y=AMout, zx=instruction[11], nx=instruction[10],\n    zy=instruction[9], ny=instruction[8], f=instruction[7], no=instruction[6],\n    out=ALUout, zr=ZRout, ng=NGout);' },
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
    details: ['Tokenization, recursive descent parsing, symbol tables, VM writing, and folder or single-file compilation.'],
    code: [{ label: 'JackCompiler.py', text: 'if os.path.isdir(path):\n    for filename in os.listdir(path):\n        if filename.endswith(".jack"):\n            compile_file(os.path.join(path, filename))' }],
    files: [{ label: 'jack-compiler.zip', href: `${fileBase}jack-compiler.zip`, download: 'jack-compiler.zip' }],
  },
  {
    title: 'Yale Hackathon — Assistive Arm + Voice Navigation',
    category: 'Hackathon / Assistive Technology',
    body: 'Yale hackathon project combining an assistive robotic arm concept with a voice navigation app for accessibility, sensing, and spoken directions.',
    repoUrl: 'https://github.com/ZainKhan06/SenseTrack',
    details: ['Assistive robotic arm prototype, camera and servo rig, voice-first navigation, sensing, and rapid prototyping.'],
    images: [
      { src: assistiveArmMounted, alt: 'Wearable assistive robotic arm mounted on a prototype board', label: 'Assistive arm prototype' },
      { src: assistiveArmCamera, alt: 'Assistive prototype with camera and servo assembly', label: 'Camera and servo rig' },
    ],
  },
  {
    title: 'Wi-Fi Robot Car',
    category: 'Robotics',
    body: 'Built a Raspberry Pi robot car controlled over Wi-Fi from a custom iPhone app with gyro steering and live camera streaming.',
    repoUrl: null,
    details: ['Raspberry Pi 5, L298N motor driver, iPhone app, Python TCP server, PWM motor control, GPIO debugging, and camera stream setup.'],
    video: { src: `${import.meta.env.BASE_URL}videos/robot-car-demo.mp4`, caption: 'Robot car demo shown at 2x speed.' },
  },
  {
    title: 'SmartPipe',
    category: 'Product concept',
    body: 'Early-stage hardware and mobile app project for helping users reduce vaping with sensing, tracking, reminders, notes, analytics, and coaching features.',
    repoUrl: null,
    details: ['ADC puff sensing, adaptive baseline calibration, Flutter app concepts, BLE connectivity, analytics, haptics, notes, reminders, and AI coaching.'],
    code: [{ label: 'SmartPipe.py', text: 'START_DELTA = max(MIN_START_DELTA, noise * 6)\nSTOP_DELTA = max(MIN_STOP_DELTA, noise * 3)\nif puffs >= MAX_PUFFS:\n    locked = True' }],
    images: [
      { src: smartpipeHardware, alt: 'SmartPipe prototype electronics', label: 'Prototype electronics' },
      { src: smartpipeCode, alt: 'SmartPipe code showing puff tracking', label: 'Tracking software' },
      { src: smartpipeAppSettings, alt: 'SmartPipe app settings screen', label: 'App settings' },
      { src: smartpipeAppTracking, alt: 'SmartPipe app tracking screen', label: 'Session tracking' },
      { src: smartpipeAppPlan, alt: 'SmartPipe app plan screen', label: 'Adaptive plan' },
      { src: smartpipeAppNotes, alt: 'SmartPipe app notes modal', label: 'Notes modal' },
      { src: smartpipeAppReminder, alt: 'SmartPipe app reminder screen', label: 'Reminders' },
    ],
    files: [{ label: 'SmartPipe.py', href: `${fileBase}SmartPipe.py`, download: 'SmartPipe.py' }],
  },
  { title: 'AI Servo Light Switch', category: 'Automation', body: 'Built a servo-based light switch system that can physically turn a standard wall switch on and off using Raspberry Pi control.', repoUrl: 'https://github.com/ZainKhansn/AutomaticRoomLight', details: ['Servo motor, controller board, mechanical linkage, actuation logic, alignment, reliability, and safety.'] },
  { title: 'Epic Latin Game', category: 'Python/Pygame', body: 'Built a Python/Pygame Latin practice game with vocabulary challenges, feedback, and a simple game loop.', repoUrl: 'https://github.com/ZainKhan06/EpicLatinGame', details: ['Python, Pygame, vocabulary practice, graphical UI, event-driven programming, and game loop architecture.'], code: [{ label: 'main.py', text: 'def check_word(word, found_words):\n    if len(word) <= 3 or letters[6] not in word:\n        return False' }], files: [{ label: 'main.py', href: `${fileBase}latin-main.py` }] },
  { title: 'Programmatics Website', category: 'Nonprofit web development', body: 'Designed and maintained the Programmatics website to show the nonprofit’s programs, mission, outreach, and student impact.', repoUrl: nonprofitRepoUrl, details: ['Web pages for a student-led nonprofit, electronics, Raspberry Pi, coding, outreach, accessibility, and education.'] },
  { title: 'Lipid Bilayer Website', category: 'Science education', body: 'Built a biology website explaining lipid bilayers and cell membrane concepts with clear visuals for students.', repoUrl: cellMembraneRepoUrl, details: ['Cell membrane structure, phospholipids, membrane transport, diffusion, cell structure, and science communication.'] },
];

const skills = ['Computer Architecture', 'Digital Logic', 'CPU Design', 'Embedded Systems', 'Robotics', 'Motor Control', 'SwiftUI', 'Flutter', 'BLE', 'Networking', 'Compiler Design', 'Programming Language Design', 'Data Analytics', 'Mechatronics', 'Assistive Technology', 'Accessibility', 'Hackathons', 'Python', 'Pygame', 'STEM Education', 'Leadership', 'Public Speaking', 'Curriculum Design', 'Project Management'];
</script>

<template>
  <main>
    <nav class="topbar" aria-label="Primary navigation">
      <a class="brand" href="#">Zain Khan</a>
      <div>
        <a href="#work">Work</a>
        <a href="#projects">Projects</a>
        <a href="#impact">Impact</a>
        <a :href="linkedinUrl" target="_blank" rel="noreferrer">LinkedIn</a>
      </div>
    </nav>

    <section class="hero" aria-labelledby="hero-title">
      <div class="hero-copy-block">
        <p class="kicker">Electrical engineering • robotics • embedded systems</p>
        <h1 id="hero-title">Building real hardware, software, and STEM programs.</h1>
        <p>I work on practical engineering projects: custom computers, robotics, mobile apps, compilers, and hands-on STEM education for younger students.</p>
        <div class="hero-actions">
          <a href="#projects">View projects</a>
          <a :href="currentGithubUrl" target="_blank" rel="noreferrer">GitHub: ZainKhan06</a>
          <a :href="oldGithubUrl" target="_blank" rel="noreferrer">Old GitHub: ZainKhansn</a>
          <a :href="linkedinUrl" target="_blank" rel="noreferrer">LinkedIn</a>
        </div>
      </div>
      <aside class="hero-card" aria-label="Profile summary">
        <img class="portrait" :src="profilePhoto" alt="Zain Khan" />
        <div><span>Current focus</span><strong>Hardware + code projects</strong></div>
        <div class="metrics">
          <p><b>16-bit</b><span>custom computer</span></p>
          <p><b>60+</b><span>students taught</span></p>
          <p><b>Full-stack</b><span>hardware to app</span></p>
        </div>
      </aside>
    </section>

    <section id="work" class="featured">
      <div class="feature-text">
        <p class="kicker">Flagship build</p>
        <h2>Custom 16-Bit Computer</h2>
        <p>A complete computer architecture project built from logic gates through CPU design, assembler, compiler, graphics, and Tetris.</p>
        <a class="text-link" href="#projects">Open full project notes</a>
      </div>
      <div class="feature-board"><img :src="instructionSetSvg" alt="Hack instruction set diagram" /></div>
    </section>

    <section id="projects" class="projects">
      <div class="section-heading">
        <p class="kicker">Selected work</p>
        <h2>Project archive</h2>
        <p>Project photos and build notes are organized inside each project card.</p>
      </div>
      <div class="project-grid">
        <article v-for="(project, index) in projects" :key="project.title" class="project-card" :class="{ large: index === 0 || index === 4 }">
          <div class="project-topline">
            <span>{{ project.category }}</span>
            <a v-if="project.repoUrl && project.repoUrl.startsWith('https')" :href="project.repoUrl" target="_blank" rel="noreferrer">Repo</a>
          </div>
          <h3>{{ project.title }}</h3>
          <p>{{ project.body }}</p>
          <div v-if="project.images" class="media-grid">
            <figure v-for="image in project.images" :key="image.label"><img :src="image.src" :alt="image.alt" /><figcaption>{{ image.label }}</figcaption></figure>
          </div>
          <div v-if="project.video" class="project-video"><video controls playsinline preload="metadata"><source :src="project.video.src" type="video/mp4" />Your browser does not support the video tag.</video><small>{{ project.video.caption }}</small></div>
          <details class="project-details"><summary>Details</summary><ul><li v-for="detail in project.details" :key="detail">{{ detail }}</li></ul></details>
          <details v-if="project.code" class="code-drawer"><summary>Code samples</summary><div v-for="sample in project.code" :key="sample.label" class="code-sample"><span>{{ sample.label }}</span><pre><code>{{ sample.text }}</code></pre></div></details>
          <div v-if="project.files" class="file-links"><a v-for="file in project.files" :key="file.label" :href="file.href" :download="file.download || file.label">{{ file.label }}</a></div>
        </article>
      </div>
    </section>

    <section id="impact" class="impact">
      <div class="impact-copy">
        <p class="kicker">Programmatics STEM Nonprofit</p>
        <h2>Teaching circuits, Raspberry Pi, and coding through hands-on projects.</h2>
        <p>Co-founded and led Programmatics, a student-run STEM nonprofit that teaches younger students electronics, circuits, Raspberry Pi systems, GPIO, sensors, LEDs, Python hardware control, Scratch, and Unity.</p>
        <ul>
          <li>Reached 60+ students through Goodnow Library, Curtis Middle School, and Stow programs.</li>
          <li>Designed hands-on lessons on voltage, current, pinouts, breadboards, GPIO, sensors, LEDs, and Python.</li>
          <li>Guided students through wiring, debugging, and integrating physical electronics with software.</li>
          <li>Built outreach material and maintained the nonprofit website.</li>
        </ul>
        <a class="text-link" :href="nonprofitRepoUrl" target="_blank" rel="noreferrer">View nonprofit repo</a>
      </div>
      <div class="photo-wall"><figure v-for="photo in programmaticPhotos" :key="photo"><img :src="photo" alt="Programmatics class photo" /></figure></div>
    </section>

    <section class="skills" aria-label="Technical skills"><span v-for="skill in skills" :key="skill">{{ skill }}</span></section>
    <footer class="footer"><p>GitHub:</p><a :href="currentGithubUrl" target="_blank" rel="noreferrer">ZainKhan06</a><a :href="oldGithubUrl" target="_blank" rel="noreferrer">ZainKhansn old main account</a><a :href="linkedinUrl" target="_blank" rel="noreferrer">LinkedIn</a></footer>
  </main>
</template>
