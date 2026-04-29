from http.server import BaseHTTPRequestHandler, HTTPServer

from pathlib import Path

PORT = 8000

HTML = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>我的个人主页</title>
  <style>
    :root {
      --bg: #f7f2e7;
      --card: #fffaf2;
      --text: #1c1b1a;
      --accent: #c45b2e;
      --accent-2: #19535f;
      --line: #e2d6c3;
      --shadow: 0 18px 40px rgba(27, 31, 35, 0.14);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: "Space Grotesk", "Noto Sans SC", "PingFang SC", sans-serif;
      color: var(--text);
      background:
        radial-gradient(circle at 15% 10%, #f2d7ba 0, transparent 38%),
        radial-gradient(circle at 85% 20%, #c6ded6 0, transparent 35%),
        var(--bg);
      line-height: 1.65;
      min-height: 100vh;
    }

    .wrapper {
      width: min(1080px, 92%);
      margin: 0 auto;
    }

    header {
      position: sticky;
      top: 0;
      backdrop-filter: blur(8px);
      background: rgba(247, 242, 231, 0.85);
      border-bottom: 1px solid var(--line);
      z-index: 10;
    }

    .nav {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 14px 0;
    }

    .brand {
      font-weight: 800;
      letter-spacing: 1px;
      font-size: 1.1rem;
    }

    .nav a {
      color: var(--text);
      text-decoration: none;
      margin-left: 18px;
      font-weight: 600;
      transition: color 0.25s ease;
    }

    .nav a:hover {
      color: var(--accent);
    }

    .hero {
      padding: 72px 0 34px;
      display: grid;
      grid-template-columns: 1.25fr 1fr;
      gap: 26px;
      align-items: center;
    }

    .hero h1 {
      font-size: clamp(2rem, 4.7vw, 3.8rem);
      line-height: 1.1;
      margin-bottom: 15px;
    }

    .hero p {
      font-size: 1.05rem;
      max-width: 56ch;
      margin-bottom: 22px;
    }

    .cta {
      display: inline-block;
      background: linear-gradient(100deg, var(--accent), #de7f53);
      color: #fff;
      padding: 12px 22px;
      border-radius: 999px;
      text-decoration: none;
      font-weight: 700;
      letter-spacing: 0.3px;
      box-shadow: 0 10px 25px rgba(196, 91, 46, 0.35);
      transition: transform 0.2s ease;
    }

    .cta:hover {
      transform: translateY(-2px);
    }

    .portrait {
      background: linear-gradient(120deg, #f3d8b8, #bfd9d4);
      border-radius: 26px;
      padding: 22px;
      box-shadow: var(--shadow);
    }

    .portrait .frame {
      border: 2px dashed rgba(28, 27, 26, 0.2);
      border-radius: 18px;
      height: 320px;
      display: grid;
      place-items: center;
      font-size: 1.2rem;
      font-weight: 700;
      text-align: center;
      color: #2e2a28;
      padding: 20px;
    }

    section {
      margin: 36px 0;
    }

    .title {
      font-size: 1.5rem;
      margin-bottom: 14px;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 16px;
    }

    .card {
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: 16px;
      padding: 18px;
      box-shadow: 0 8px 20px rgba(27, 31, 35, 0.08);
    }

    .card h3 {
      margin-bottom: 8px;
      color: var(--accent-2);
    }

    .timeline {
      border-left: 3px solid #d6c8b1;
      padding-left: 16px;
      display: grid;
      gap: 16px;
    }

    .timeline-item {
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 12px 14px;
      position: relative;
    }

    .timeline-item::before {
      content: "";
      position: absolute;
      left: -24px;
      top: 18px;
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: var(--accent);
    }

    .contact {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }

    .tag {
      border: 1px solid #c4b59f;
      padding: 8px 12px;
      border-radius: 999px;
      background: #fff;
      text-decoration: none;
      color: var(--text);
      font-weight: 600;
    }

    footer {
      margin: 42px 0 20px;
      text-align: center;
      color: #6e665d;
      font-size: 0.95rem;
    }

    .reveal {
      opacity: 0;
      transform: translateY(22px);
      transition: opacity 0.7s ease, transform 0.7s ease;
    }

    .reveal.show {
      opacity: 1;
      transform: translateY(0);
    }

    @media (max-width: 900px) {
      .hero {
        grid-template-columns: 1fr;
      }

      .grid {
        grid-template-columns: 1fr;
      }

      .nav {
        flex-direction: column;
        gap: 8px;
      }

      .nav a {
        margin: 0 8px;
      }
    }
  </style>
</head>
<body>
  <header>
    <div class="wrapper nav">
      <div class="brand">MY LANDING</div>
      <nav>
        <a href="#about">关于我</a>
        <a href="/snake.html">Snake</a>
        <a href="/projects.html">项目经历</a>
        <a href="#journey">经历</a>
        <a href="#contact">联系</a>
      </nav>
    </div>
  </header>

  <main class="wrapper">
    <section class="hero reveal" id="about">
      <div>
        <h1>你好，我是你的名字</h1>
        <p>我专注于把想法变成可运行的产品，喜欢用简洁设计和清晰代码解决真实问题。这是我的个人主页，你可以在这里快速了解我做过的事情。</p>
        <a class="cta" href="/snake.html">打开 Snake</a>
      </div>
      <div class="portrait">
        <div class="frame">在这里放一张你的照片<br/>或一句个性签名</div>
      </div>
    </section>

    <section id="journey" class="reveal">
      <h2 class="title">成长经历</h2>
      <div class="timeline">
        <div class="timeline-item">
          <strong>2026</strong> - 持续构建个人作品集，专注前端体验与工程化。
        </div>
        <div class="timeline-item">
          <strong>2025</strong> - 完成多个课程项目，系统学习 Python 与 Web 开发。
        </div>
        <div class="timeline-item">
          <strong>2024</strong> - 开始独立做小项目，形成从想法到落地的完整流程。
        </div>
      </div>
    </section>

    <section id="contact" class="reveal">
      <h2 class="title">联系方式</h2>
      <div class="contact">
        <a class="tag" href="mailto:yourname@example.com">Email</a>
        <a class="tag" href="#">GitHub</a>
        <a class="tag" href="#">LinkedIn</a>
      </div>
    </section>

    <footer>
      <span id="year"></span> 你的名字. All rights reserved.
    </footer>
  </main>

  <script>
    document.getElementById("year").textContent = new Date().getFullYear();

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
          setTimeout(() => entry.target.classList.add("show"), index * 110);
        }
      });
    }, { threshold: 0.1 });

    document.querySelectorAll(".reveal").forEach((el) => observer.observe(el));
  </script>
</body>
</html>
"""

PROJECTS_HTML = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>项目经历</title>
  <style>
    :root {
      --bg: #eef4f6;
      --panel: #ffffff;
      --text: #132125;
      --muted: #4f6368;
      --accent: #1f7a8c;
      --line: #d7e3e7;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: "Space Grotesk", "Noto Sans SC", "PingFang SC", sans-serif;
      color: var(--text);
      background:
        radial-gradient(circle at 8% 14%, #c6e2eb 0, transparent 35%),
        radial-gradient(circle at 92% 18%, #d0efe4 0, transparent 32%),
        var(--bg);
      min-height: 100vh;
      line-height: 1.65;
    }

    .wrapper {
      width: min(980px, 92%);
      margin: 0 auto;
    }

    header {
      padding: 26px 0 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    h1 {
      font-size: clamp(1.8rem, 3.8vw, 2.9rem);
      letter-spacing: 0.3px;
    }

    .home-link {
      text-decoration: none;
      color: #fff;
      background: linear-gradient(100deg, var(--accent), #2d95aa);
      padding: 10px 16px;
      border-radius: 999px;
      font-weight: 700;
      box-shadow: 0 10px 20px rgba(31, 122, 140, 0.25);
    }

    .lead {
      color: var(--muted);
      margin: 2px 0 20px;
      max-width: 65ch;
    }

    .list {
      display: grid;
      gap: 16px;
      margin-bottom: 28px;
    }

    .item {
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 16px;
      padding: 18px;
      box-shadow: 0 8px 24px rgba(15, 37, 43, 0.08);
    }

    .item h2 {
      font-size: 1.2rem;
      color: #19444e;
      margin-bottom: 6px;
    }

    .meta {
      color: #3e6972;
      font-size: 0.95rem;
      margin-bottom: 10px;
      font-weight: 600;
    }

    .tags {
      margin-top: 12px;
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .tag {
      border: 1px solid #bdd3d9;
      border-radius: 999px;
      padding: 5px 10px;
      font-size: 0.9rem;
      background: #f8fdff;
    }

    footer {
      text-align: center;
      color: #5f7378;
      padding: 18px 0 22px;
      border-top: 1px solid #d6e1e5;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <main class="wrapper">
    <header>
      <h1>项目经历</h1>
      <a class="home-link" href="/">返回主页</a>
    </header>
    <p class="lead">这里集中展示我的项目实践，包括目标、技术方案和产出结果。你可以替换为自己的真实项目内容。</p>

    <section class="list">
      <article class="item">
        <h2>Classic Snake</h2>
        <p class="meta">2026.04 · 交互小游戏</p>
        <p>基于原生 JavaScript 与 Python 标准库页面服务实现的经典贪吃蛇，包含网格移动、食物生成、分数统计、暂停、失败与重开。</p>
        <div class="tags">
          <span class="tag">Python</span>
          <span class="tag">JavaScript</span>
          <span class="tag">Game Loop</span>
        </div>
        <div class="tags">
          <a class="home-link" href="/snake.html">开始游戏</a>
        </div>
      </article>

      <article class="item">
        <h2>智能日程助手</h2>
        <p class="meta">2026.01 - 2026.03 · 个人项目</p>
        <p>开发一个支持任务分组、优先级排序和提醒通知的日程管理工具。通过可视化统计面板帮助用户追踪完成率和时间投入。</p>
        <div class="tags">
          <span class="tag">Python</span>
          <span class="tag">Flask</span>
          <span class="tag">SQLite</span>
        </div>
      </article>

      <article class="item">
        <h2>数据看板系统</h2>
        <p class="meta">2025.08 - 2025.12 · 课程项目</p>
        <p>构建数据清洗与可视化一体化页面，支持按维度筛选并实时更新图表。降低了信息理解成本，提高决策效率。</p>
        <div class="tags">
          <span class="tag">JavaScript</span>
          <span class="tag">ECharts</span>
          <span class="tag">REST API</span>
        </div>
      </article>

      <article class="item">
        <h2>自动化脚本工具箱</h2>
        <p class="meta">2025.03 - 2025.06 · 个人项目</p>
        <p>整理常用自动化流程，覆盖文件整理、批量重命名、日志提取等场景。显著减少重复劳动并提升处理效率。</p>
        <div class="tags">
          <span class="tag">Python</span>
          <span class="tag">PowerShell</span>
          <span class="tag">Automation</span>
        </div>
      </article>
    </section>

    <footer>
      <span id="year"></span> 你的名字. Project Experience Page.
    </footer>
  </main>

  <script>
    document.getElementById("year").textContent = new Date().getFullYear();
  </script>
</body>
</html>
"""

SNAKE_HTML = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Classic Snake</title>
  <style>
    :root {
      --bg: #f7f2e7;
      --panel: #fffaf2;
      --text: #1c1b1a;
      --muted: #6e665d;
      --accent: #c45b2e;
      --accent-2: #19535f;
      --line: #e2d6c3;
      --cell: #f1e6d5;
      --snake: #19535f;
      --snake-head: #103841;
      --food: #c45b2e;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: "Space Grotesk", "Noto Sans SC", "PingFang SC", sans-serif;
      color: var(--text);
      background:
        radial-gradient(circle at 15% 10%, #f2d7ba 0, transparent 38%),
        radial-gradient(circle at 85% 20%, #c6ded6 0, transparent 35%),
        var(--bg);
      min-height: 100vh;
      line-height: 1.6;
    }

    .wrapper {
      width: min(960px, 92%);
      margin: 0 auto;
      padding: 28px 0 36px;
    }

    .topbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      margin-bottom: 22px;
    }

    .topbar h1 {
      font-size: clamp(2rem, 4vw, 3rem);
    }

    .back-link {
      text-decoration: none;
      color: #fff;
      background: linear-gradient(100deg, var(--accent), #de7f53);
      padding: 10px 16px;
      border-radius: 999px;
      font-weight: 700;
    }

    .layout {
      display: grid;
      grid-template-columns: minmax(0, 1fr) 280px;
      gap: 18px;
      align-items: start;
    }

    .panel {
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 18px;
      padding: 18px;
      box-shadow: 0 10px 30px rgba(27, 31, 35, 0.08);
    }

    .board-wrap {
      display: flex;
      justify-content: center;
    }

    .board {
      width: min(78vw, 560px);
      aspect-ratio: 1;
      display: grid;
      grid-template-columns: repeat(16, 1fr);
      grid-template-rows: repeat(16, 1fr);
      gap: 2px;
      background: var(--line);
      padding: 2px;
      border-radius: 14px;
    }

    .cell {
      background: var(--cell);
      border-radius: 4px;
    }

    .cell.snake {
      background: var(--snake);
    }

    .cell.head {
      background: var(--snake-head);
    }

    .cell.food {
      background: var(--food);
    }

    .meta {
      display: grid;
      gap: 12px;
    }

    .stat {
      padding: 12px 14px;
      border: 1px solid var(--line);
      border-radius: 14px;
      background: #fffdf8;
    }

    .stat strong {
      display: block;
      font-size: 1.5rem;
      color: var(--accent-2);
    }

    .controls,
    .dpad {
      display: grid;
      gap: 10px;
    }

    .controls {
      grid-template-columns: 1fr 1fr;
    }

    button {
      border: 1px solid #ccbda8;
      background: #fff;
      color: var(--text);
      border-radius: 12px;
      padding: 11px 14px;
      font: inherit;
      font-weight: 700;
      cursor: pointer;
    }

    button.primary {
      background: linear-gradient(100deg, var(--accent), #de7f53);
      color: #fff;
      border-color: transparent;
    }

    .dpad {
      grid-template-columns: repeat(3, 1fr);
    }

    .dpad .empty {
      visibility: hidden;
    }

    .hint {
      color: var(--muted);
      font-size: 0.95rem;
    }

    .status {
      min-height: 24px;
      font-weight: 700;
      color: var(--accent);
    }

    @media (max-width: 860px) {
      .layout {
        grid-template-columns: 1fr;
      }

      .topbar {
        flex-direction: column;
        align-items: flex-start;
      }

      .board {
        width: min(92vw, 520px);
      }
    }
  </style>
</head>
<body>
  <main class="wrapper">
    <div class="topbar">
      <div>
        <h1>Classic Snake</h1>
        <p class="hint">方向键或 WASD 控制移动，空格暂停，撞墙或撞到自己则结束。</p>
      </div>
      <a class="back-link" href="/">返回主页</a>
    </div>

    <section class="layout">
      <div class="panel board-wrap">
        <div class="board" id="board" aria-label="Snake game board"></div>
      </div>

      <aside class="panel meta">
        <div class="stat">
          当前分数
          <strong id="score">0</strong>
        </div>
        <div class="stat">
          游戏状态
          <strong id="stateText">进行中</strong>
        </div>

        <div class="controls">
          <button class="primary" id="restartBtn">重新开始</button>
          <button id="pauseBtn">暂停</button>
        </div>

        <div class="dpad">
          <span class="empty">.</span>
          <button data-dir="up">上</button>
          <span class="empty">.</span>
          <button data-dir="left">左</button>
          <button data-dir="down">下</button>
          <button data-dir="right">右</button>
        </div>

        <p class="status" id="statusText"></p>
      </aside>
    </section>
  </main>

  <script>
    const BOARD_SIZE = 16;
    const TICK_MS = 140;
    const DIRECTIONS = {
      up: { x: 0, y: -1 },
      down: { x: 0, y: 1 },
      left: { x: -1, y: 0 },
      right: { x: 1, y: 0 }
    };
    const KEY_TO_DIRECTION = {
      ArrowUp: "up",
      ArrowDown: "down",
      ArrowLeft: "left",
      ArrowRight: "right",
      w: "up",
      W: "up",
      s: "down",
      S: "down",
      a: "left",
      A: "left",
      d: "right",
      D: "right"
    };
    const OPPOSITE = {
      up: "down",
      down: "up",
      left: "right",
      right: "left"
    };

    const boardEl = document.getElementById("board");
    const scoreEl = document.getElementById("score");
    const stateTextEl = document.getElementById("stateText");
    const statusTextEl = document.getElementById("statusText");
    const pauseBtn = document.getElementById("pauseBtn");
    const restartBtn = document.getElementById("restartBtn");

    const cells = [];
    for (let index = 0; index < BOARD_SIZE * BOARD_SIZE; index += 1) {
      const cell = document.createElement("div");
      cell.className = "cell";
      boardEl.appendChild(cell);
      cells.push(cell);
    }

    let intervalId = null;
    let queuedDirection = null;
    let state = createInitialState();

    function createInitialState() {
      const middle = Math.floor(BOARD_SIZE / 2);
      const snake = [
        { x: middle, y: middle },
        { x: middle - 1, y: middle },
        { x: middle - 2, y: middle }
      ];
      return {
        snake,
        direction: "right",
        food: randomFood(snake),
        score: 0,
        paused: false,
        gameOver: false
      };
    }

    function randomFood(snake) {
      const occupied = new Set(snake.map((segment) => `${segment.x},${segment.y}`));
      const freeCells = [];
      for (let y = 0; y < BOARD_SIZE; y += 1) {
        for (let x = 0; x < BOARD_SIZE; x += 1) {
          const key = `${x},${y}`;
          if (!occupied.has(key)) {
            freeCells.push({ x, y });
          }
        }
      }
      return freeCells[Math.floor(Math.random() * freeCells.length)];
    }

    function queueDirection(nextDirection) {
      if (state.gameOver) {
        return;
      }
      const baseline = queuedDirection || state.direction;
      if (nextDirection === OPPOSITE[baseline]) {
        return;
      }
      queuedDirection = nextDirection;
    }

    function tick() {
      if (state.paused || state.gameOver) {
        render();
        return;
      }

      const directionName = queuedDirection && queuedDirection !== OPPOSITE[state.direction]
        ? queuedDirection
        : state.direction;
      queuedDirection = null;
      const delta = DIRECTIONS[directionName];
      const head = state.snake[0];
      const nextHead = { x: head.x + delta.x, y: head.y + delta.y };

      if (
        nextHead.x < 0 ||
        nextHead.x >= BOARD_SIZE ||
        nextHead.y < 0 ||
        nextHead.y >= BOARD_SIZE
      ) {
        state = { ...state, direction: directionName, gameOver: true };
        render();
        return;
      }

      const grows = nextHead.x === state.food.x && nextHead.y === state.food.y;
      const body = grows ? state.snake : state.snake.slice(0, -1);
      if (body.some((segment) => segment.x === nextHead.x && segment.y === nextHead.y)) {
        state = { ...state, direction: directionName, gameOver: true };
        render();
        return;
      }

      const nextSnake = [nextHead, ...state.snake];
      if (!grows) {
        nextSnake.pop();
      }

      state = {
        ...state,
        snake: nextSnake,
        direction: directionName,
        score: grows ? state.score + 1 : state.score,
        food: grows ? randomFood(nextSnake) : state.food
      };
      render();
    }

    function restartGame() {
      state = createInitialState();
      queuedDirection = null;
      render();
    }

    function togglePause() {
      if (state.gameOver) {
        return;
      }
      state = { ...state, paused: !state.paused };
      render();
    }

    function render() {
      cells.forEach((cell) => {
        cell.className = "cell";
      });

      state.snake.forEach((segment, index) => {
        const cellIndex = segment.y * BOARD_SIZE + segment.x;
        cells[cellIndex].classList.add("snake");
        if (index === 0) {
          cells[cellIndex].classList.add("head");
        }
      });

      const foodIndex = state.food.y * BOARD_SIZE + state.food.x;
      cells[foodIndex].classList.add("food");

      scoreEl.textContent = String(state.score);
      if (state.gameOver) {
        stateTextEl.textContent = "已结束";
        statusTextEl.textContent = "游戏结束，点击“重新开始”再来一局。";
      } else if (state.paused) {
        stateTextEl.textContent = "暂停中";
        statusTextEl.textContent = "已暂停，按空格或点击按钮继续。";
      } else {
        stateTextEl.textContent = "进行中";
        statusTextEl.textContent = "";
      }
      pauseBtn.textContent = state.paused ? "继续" : "暂停";
    }

    document.addEventListener("keydown", (event) => {
      const direction = KEY_TO_DIRECTION[event.key];
      if (direction) {
        event.preventDefault();
        queueDirection(direction);
        return;
      }
      if (event.code === "Space") {
        event.preventDefault();
        togglePause();
      }
    });

    document.querySelectorAll("[data-dir]").forEach((button) => {
      button.addEventListener("click", () => queueDirection(button.dataset.dir));
    });

    pauseBtn.addEventListener("click", togglePause);
    restartBtn.addEventListener("click", restartGame);

    render();
    intervalId = window.setInterval(tick, TICK_MS);
  </script>
</body>
</html>
"""


class PersonalSiteHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/index.html"):
            body = HTML.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        if self.path == "/projects.html":
            body = PROJECTS_HTML.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        if self.path == "/snake.html":
            body = load_page("snake_page.html").encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        if self.path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return

        self.send_response(404)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write("404 Not Found".encode("utf-8"))


def load_page(filename: str) -> str:
    return (Path(__file__).resolve().parent / filename).read_text(encoding="utf-8")


def run_server():
    server = HTTPServer(("127.0.0.1", PORT), PersonalSiteHandler)
    print(f"Personal site running at: http://127.0.0.1:{PORT}")
    print("Press Ctrl+C to stop.")
    server.serve_forever()


if __name__ == "__main__":
    run_server()
