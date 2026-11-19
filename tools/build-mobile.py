#!/usr/bin/env python3
# Builds mobile.html (the phone version) from index.html.
# Run it after every change to index.html:  python3 tools/build-mobile.py
# It swaps the mouse/keyboard UI for a touch kit (joystick + pixel-art action
# buttons), adds the landscape lock / "gire o celular" overlay, a lower internal
# resolution and an HUD-only cockpit. Each replacement asserts it found its
# target, so a change in index.html that breaks one fails loudly.
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = os.path.join(ROOT, 'index.html'); dst = os.path.join(ROOT, 'mobile.html')
s=open(src).read()
def rep(a,b,cnt=1):
    global s
    n=s.count(a)
    assert n==cnt, (n,a[:90])
    s=s.replace(a,b)

# ---------- head
import re as _re
s=_re.sub(r"<script>\n// phones and tablets get the touch version.*?</script>\n", '', s, flags=_re.S)
rep('<title>Patrol</title>','<title>Patrol · celular</title>\n<meta name="theme-color" content="#17112a">\n<meta name="mobile-web-app-capable" content="yes">\n<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">')
rep('content="Patrol: um brinquedo de voo de caça em pixel art sobre a região dos lagos no outono."','content="Patrol para celular: voo de caça em pixel art, com joystick na tela e botões de toque."')

# ---------- CSS: replace old touch css with the mobile control kit
old_touch_css=s[s.index('/* touch */'):s.index('@media (max-width:640px){ #strip .long{display:none} }')]
new_css=r'''/* ===== mobile controls ===== */
html,body{overscroll-behavior:none;-webkit-tap-highlight-color:transparent}
#strip{gap:10px;padding:4px 8px;font-size:10px;top:max(6px,env(safe-area-inset-top));bottom:auto}
#strip .k,#strip .long,#pips,#flareKey{display:none!important}
#strip button{font-size:10px;padding:3px 7px}
#hullbar{width:56px}
.card{padding:16px 18px 14px}
h1{font-size:clamp(26px,6vh,46px);margin-bottom:6px}
.sub{margin-bottom:8px}
.how{font-size:11px}
.how b{min-width:120px}
#go{margin-top:8px}
#deskLink{display:block;margin-top:10px;font-size:10px;color:var(--dim)}
#ctl{position:absolute;inset:0;z-index:4;display:none;pointer-events:none;touch-action:none}
#stickZone{position:absolute;left:0;top:44px;bottom:0;width:46%;pointer-events:auto;touch-action:none}
#stick{position:absolute;width:132px;height:132px;margin:-66px 0 0 -66px;display:none;pointer-events:none}
#stick .base{position:absolute;inset:0;image-rendering:pixelated}
#stick .knob{position:absolute;left:50%;top:50%;width:52px;height:52px;margin:-26px 0 0 -26px;image-rendering:pixelated}
#stickHint{position:absolute;left:calc(14px + env(safe-area-inset-left));bottom:18px;font-family:"Press Start 2P",monospace;font-size:8px;color:rgba(243,227,207,.55);line-height:1.6;pointer-events:none}
#stickHint i{display:block;width:84px;height:84px;margin-bottom:6px;opacity:.45;background-size:contain;image-rendering:pixelated}
.act{position:absolute;pointer-events:auto;touch-action:none;width:var(--s);height:var(--s);padding:0;border:0;background:none;color:var(--ink);font-family:"Press Start 2P",monospace;
  -webkit-user-select:none;user-select:none}
.act .face{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;box-sizing:border-box;
  background:linear-gradient(#3a2d55 0 50%,#2c2145 50% 100%);border:3px solid var(--ring,#6b5a86);
  box-shadow:inset 3px 3px 0 rgba(255,255,255,.13),inset -3px -3px 0 rgba(0,0,0,.38),0 0 0 3px #0d0918,5px 5px 0 3px rgba(13,9,24,.5);transition:transform .05s}
.act svg{width:calc(var(--s) * .44);height:calc(var(--s) * .44);shape-rendering:crispEdges;fill:var(--ic,#ffd3a1)}
.act .lb{font-size:7px;letter-spacing:.5px;color:var(--ink);text-shadow:1px 1px 0 #0d0918}
.act .cd{position:absolute;left:0;right:0;top:0;height:0;background:rgba(13,9,24,.62);pointer-events:none}
.act .ct{position:absolute;right:-6px;top:-6px;min-width:20px;height:20px;padding:0 4px;box-sizing:border-box;display:flex;align-items:center;justify-content:center;
  font-size:9px;color:#17112a;background:var(--gold);border:2px solid #0d0918}
.act .ct.zero{background:#ff5a46;color:#fff}
.act.on .face{transform:translate(3px,4px);border-color:var(--gold);box-shadow:inset 3px 3px 0 rgba(0,0,0,.4),0 0 0 3px #0d0918,1px 1px 0 3px rgba(13,9,24,.5);background:linear-gradient(#4b3a6e 0 50%,#3a2d55 50% 100%)}
.act.lit{--ring:var(--gold)}
.act.lit .face{background:linear-gradient(#7a5530 0 50%,#5a3d22 50% 100%)}
.act.ready{--ring:#7be38a}
.act.ready .lb{color:#a8ffb0}
.act.alarm .face{animation:alarm .36s steps(1) infinite}
@keyframes alarm{0%{border-color:#ff5a46;background:linear-gradient(#a8322a 0 50%,#7a2420 50% 100%)}50%{border-color:#ffd3a1;background:linear-gradient(#3a2d55 0 50%,#2c2145 50% 100%)}}
.act.big{--ic:#ffe08a}
.act.wait svg{opacity:.45}
#ctl .act{--s:62px}
#bGun{--s:88px;right:calc(18px + env(safe-area-inset-right));bottom:22px}
#bMsl{right:calc(122px + env(safe-area-inset-right));bottom:16px}
#bRoll{right:calc(28px + env(safe-area-inset-right));bottom:130px}
#bFlip{right:calc(112px + env(safe-area-inset-right));bottom:104px;--s:56px}
#bFlare{right:calc(200px + env(safe-area-inset-right));bottom:16px;--s:56px}
#bBoost{right:calc(186px + env(safe-area-inset-right));bottom:90px;--s:56px}
@media (max-height:340px){ #ctl .act{--s:54px} #bGun{--s:76px;bottom:14px} #bRoll{bottom:110px} #bFlip{bottom:88px} #bBoost{bottom:76px} }
#tip{top:calc(40px + env(safe-area-inset-top));font-size:11px;padding:6px 10px;max-width:min(470px,62vw)}
body.ck #tip{top:calc(40px + env(safe-area-inset-top))}
#tip .hd{font-size:8px;margin-bottom:4px}
#tip .skip{margin-top:5px;font-size:9px}
#toast{font-size:10px;top:34%}
#rotate{position:fixed;inset:0;z-index:20;display:none;flex-direction:column;align-items:center;justify-content:center;gap:22px;background:var(--night);text-align:center;padding:24px}
#rotate .ph{width:64px;height:110px;border:6px solid var(--peach);box-shadow:6px 6px 0 #8a3b3b;position:relative;animation:turn 2.4s steps(1) infinite}
#rotate .ph:after{content:"";position:absolute;left:50%;bottom:6px;width:12px;height:6px;margin-left:-6px;background:var(--peach)}
@keyframes turn{0%,45%{transform:rotate(0)}50%,95%{transform:rotate(-90deg)}}
#rotate .t1{font-family:"Press Start 2P",monospace;font-size:15px;color:var(--peach);line-height:1.6}
#rotate .t2{font-size:12px;color:var(--dim);max-width:300px;line-height:1.5}
@media (orientation:portrait){ body.mob #rotate{display:flex} }
'''
s=s.replace(old_touch_css,new_css)
rep('@media (max-width:640px){ #strip .long{display:none} }','')

# ---------- HTML: title card text for touch, strip, controls, rotate overlay
how_old=s[s.index('      <div><b>Mover o mouse</b>'):s.index('      <div class="p">Não dá para bater no chão')]
how_new='''      <div><b>FUMAÇA</b>no modo Força Aérea Brasileira, o botão na barra do topo troca a cor da fumaça do Tucano.</div>
      <div><b>Polegar esquerdo</b>joystick: arraste em qualquer lugar da metade esquerda da tela. Para cima sobe, para baixo desce, para os lados faz a curva. Solte e o jato volta a voar nivelado.</div>
      <div><b>TIRO</b>rajada de 15 tiros. Leve o círculo de mira até o inimigo: quando ele fica verde, o botão acende e os tiros se curvam até o alvo.</div>
      <div><b>MÍSSIL</b>dispara um míssil (4 nas asas, o número mostra quantos estão prontos). Trava no inimigo à frente do nariz.</div>
      <div><b>GIRO</b>tonneau: durante o giro os tiros não te acertam. O botão pisca quando é hora de girar.</div>
      <div><b>VOLTA</b>meia-volta: vira o jato 180°, para o lado do inimigo mais próximo.</div>
      <div><b>FLARE</b>despista mísseis inimigos. O botão pisca em vermelho quando um míssil vem atrás de você.</div>
      <div><b>TURBO</b>liga e desliga o pós-combustor.</div>
      <div><b>VISÃO / SOM / ?</b>na barra do topo: troca a câmera, abre o som (liga, desliga e volume) e esta ajuda.</div>
'''
s=s.replace(how_old,how_new)
rep('''      <div class="p">Não dá para bater no chão: o jato arremete sozinho antes do terreno. Voe baixo sobre um lago para levantar água. O míssil vai para onde o nariz aponta, ou para o chão à frente quando você voa nivelado.</div>
    </div>''','''      <div class="p">Não dá para bater no chão: o jato arremete sozinho antes do terreno. Jogue com o celular deitado; o jogo tenta entrar em tela cheia e travar na horizontal.</div>
    </div>
    <a id="deskLink" href="index.html?desktop=1">versão para computador (mouse e teclado)</a>''')
strip_old=s[s.index('<div id="strip">'):s.index('<div id="touch">')]
strip_new='''<div id="strip">
  <span class="long"><span id="vname">PERSEGUIÇÃO</span></span>
  <span style="display:none"><span class="k" id="flareKey">C</span><b id="flares">6</b></span>
  <span id="pips"><span></span><span></span><span></span><span></span></span>
  <span id="score">CASCO <span id="hullbar"><i id="hull"></i></span> ABATES <b id="kills">0</b> ONDA <b id="wave">0</b></span>
  <button id="smokeBtn" class="fabOnly">FUMAÇA: BANDEIRA</button>
  <button id="viewbtn">VISÃO</button>
  <button id="helpbtn" title="Como jogar">?</button>
  <button id="sndbtn" title="Som, música e volume">SOM</button>
</div>
'''
s=s.replace(strip_old,strip_new)
touch_old=s[s.index('<div id="touch">'):s.index('</div>', s.index('<div id="touch">'))+len('</div>')]
touch_new='''<div id="ctl">
  <div id="stickZone"></div>
  <div id="stickHint"><i id="stickHintImg"></i>ARRASTE AQUI<br>PARA PILOTAR</div>
  <div id="stick"><div class="base" id="stickBase"></div><div class="knob" id="stickKnob"></div></div>
  <button class="act big" id="bGun"><span class="face"><svg data-ic="gun"></svg><span class="lb">TIRO</span></span><span class="cd"></span></button>
  <button class="act" id="bMsl"><span class="face"><svg data-ic="msl"></svg><span class="lb">MISSIL</span></span><span class="cd"></span><span class="ct">4</span></button>
  <button class="act" id="bRoll"><span class="face"><svg data-ic="roll"></svg><span class="lb">GIRO</span></span><span class="cd"></span></button>
  <button class="act" id="bFlip"><span class="face"><svg data-ic="flip"></svg><span class="lb">VOLTA</span></span><span class="cd"></span></button>
  <button class="act" id="bFlare"><span class="face"><svg data-ic="flare"></svg><span class="lb">FLARE</span></span><span class="cd"></span><span class="ct">6</span></button>
  <button class="act" id="bBoost"><span class="face"><svg data-ic="boost"></svg><span class="lb">TURBO</span></span></button>
</div>
<div id="rotate"><div class="ph"></div><div class="t1">GIRE O CELULAR</div><div class="t2">O Patrol é jogado com o celular deitado. O jogo fica pausado enquanto a tela estiver em pé.</div></div>'''
s=s.replace(touch_old,touch_new)

# ---------- JS: mobile flag, resolution, panel
rep("const PARAMS = new URLSearchParams(location.search);","const PARAMS = new URLSearchParams(location.search);\nconst MOBILE = true;\ndocument.body.classList.add('mob');")
rep("  const base = clamp(Math.round(innerHeight / 340), 1, 8);","  // phones: about 190 pixels tall inside, so the ray-marched world stays fast\n  const base = clamp(Math.round(Math.min(innerHeight, innerWidth) / 190), 2, 8);")
rep("if (slowT > 1.5 && resDrop < 4 && innerHeight / (SCALE + 1) >= 170)","if (slowT > 1.5 && resDrop < 3 && Math.min(innerHeight, innerWidth) / (SCALE + 1) >= 120)")
# cockpit on a phone: HUD only, no instrument panel (thumbs cover the corners anyway)
rep("    if (slide > 0) { drawCanopy(slide); stepRadar(dt, layout().radar); drawPanel(slide); }","    if (slide > 0 && !MOBILE) { drawCanopy(slide); stepRadar(dt, layout().radar); drawPanel(slide); }")
rep("  PAN.h = clamp(Math.round(H * 0.36), 100, 150);","  PAN.h = MOBILE ? 0 : clamp(Math.round(H * 0.36), 100, 150);")
open(dst,'w').write(s)
print('stage1 ok')

# ================= stage 2: JS =================
s=open(dst).read()
rep("const isTouch = matchMedia('(pointer: coarse)').matches || PARAMS.get('touch') === '1';","const isTouch = true;")
rep("const input = { mx: 0, my: 0, moved: false, auto: true, ldown: false, ldownT: 0, touchSteer: false, keys: false, kTurn: 0, kPitch: 0 };",
    "const input = { mx: 0, my: 0, moved: false, auto: true, ldown: false, ldownT: 0, touchSteer: false, keys: false, kTurn: 0, kPitch: 0, stick: { on: false, x: 0, y: 0, used: false } };")
rep("""  if (input.keys && !input.auto) {
    turn = input.kTurn;
    pitchT = input.kPitch * (vw === 0 ? 0.35 : 0.7);
  } else if (input.auto) {""","""  if (input.stick.used && !input.auto) {
    // virtual joystick: x turns, up climbs; let go and the jet levels out
    const sx = input.stick.on ? input.stick.x : 0, sy = input.stick.on ? input.stick.y : 0;
    turn = Math.sign(sx) * Math.pow(Math.abs(sx), 1.25);
    pitchT = -sy * (vw === 0 ? 0.4 : 0.85);
  } else if (input.keys && !input.auto) {
    turn = input.kTurn;
    pitchT = input.kPitch * (vw === 0 ? 0.35 : 0.7);
  } else if (input.auto) {""")
# tutorial texts for the phone
rep("""tt: '<b>Arraste o dedo</b> na tela para pilotar.' }""","""tt: 'Arraste o <b>polegar esquerdo</b> em qualquer lugar da metade esquerda: é o joystick. Para cima sobe, para baixo desce, para os lados faz a curva.' }""")
rep("""tt: 'Segure <b>TURBO</b> para o pós-combustor.' }""","""tt: 'Toque em <b>TURBO</b> para ligar o pós-combustor (toque de novo para desligar).' }""")
rep("""tt: 'Toque em <b>VISÃO</b> para trocar a visão.' }""","""tt: 'Toque em <b>VISÃO</b>, na barra do topo, para trocar a câmera: de cima, perseguição e cabine.' }""")
rep("""tt: 'Toque em <b>GIRO</b> para um tonneau. Durante o giro os tiros não te acertam.' }""","""tt: 'Toque em <b>GIRO</b> para um tonneau. Durante o giro os tiros não te acertam: o botão pisca quando é hora de girar.' }""")
rep("""tt: 'Míssil inimigo chegando! Toque em <b>FLARE</b> para despistá-lo.'""","""tt: 'Míssil inimigo chegando (o <b>losango vermelho</b>)! Toque em <b>FLARE</b>, que está piscando, para despistá-lo.'""")
rep("""tt: 'Um <b>alvo de treino</b> apareceu. Leve o <b>círculo de mira</b> até ele e, quando ficar verde, toque em <b>TIRO</b>.'""","""tt: 'Um <b>alvo de treino</b> apareceu (a seta na borda mostra onde). Leve o <b>círculo de mira</b> até ele e, quando o botão <b>TIRO</b> acender verde, toque nele (ou segure).'""")
# start: show controls, go fullscreen and lock landscape
rep("""  if (isTouch) document.getElementById('touch').style.display = 'block';""","""  document.getElementById('ctl').style.display = 'block';
  goLandscape();""")
# portrait pauses the game
rep("""  if (state !== 'help' && state !== 'upgrade') {
  stepFlight(dt);""","""  if (state !== 'help' && state !== 'upgrade' && !portrait()) {
  stepFlight(dt);""")
rep("""  drawOverlay(dt);
  Snd.update();""","""  drawOverlay(dt);
  updateCtl(dt);
  Snd.update();""")
# replace the old touch bindings with the new control kit
a=s.index("// touch: drag to steer, buttons for the rest")
b=s.index("function updatePips() {")
new_js=r'''// touch: a floating joystick on the left, action buttons on the right
const portrait = () => innerHeight > innerWidth * 1.05;
function goLandscape() {
  const el = document.documentElement, rq = el.requestFullscreen || el.webkitRequestFullscreen;
  try {
    const p = rq && !document.fullscreenElement ? rq.call(el, { navigationUI: 'hide' }) : null;
    const lock = () => { try { const o = screen.orientation; if (o && o.lock) o.lock('landscape').catch(() => {}); } catch (e) {} };
    if (p && p.then) p.then(lock).catch(() => {}); else lock();
  } catch (e) {}
}
cv.addEventListener('touchstart', e => { e.preventDefault(); if (state === 'title') { startPlay(); return; } if (state === 'help') { toggleHelp(); return; } }, { passive: false });
titleEl.addEventListener('touchstart', e => { if (e.target.closest('a')) return; if (state === 'title') { e.preventDefault(); startPlay(); } else if (state === 'help') { e.preventDefault(); toggleHelp(); } }, { passive: false });
document.getElementById('over').addEventListener('touchstart', e => { if (state === 'over') { e.preventDefault(); restartGame(); } }, { passive: false });
document.getElementById('upgHint').textContent = 'toque numa opção';
document.getElementById('ovGo').textContent = 'TOQUE PARA VOAR DE NOVO';
{ const vb = document.getElementById('viewbtn'), f = e => { e.preventDefault(); e.stopPropagation(); if (state === 'play') setView((view + 1) % 3); };
  vb.addEventListener('touchstart', f, { passive: false }); vb.addEventListener('click', f); }
for (const id of ['helpbtn', 'sndbtn']) document.getElementById(id).addEventListener('touchstart', e => { e.stopPropagation(); }, { passive: true });

// pixel icons, drawn from little bitmaps (12x12)
const ICONS = {
  gun: ['.....##.....', '.....##.....', '...######...', '..#..##..#..', '.#........#.', '###..##..###', '###..##..###', '.#........#.', '..#..##..#..', '...######...', '.....##.....', '.....##.....'],
  msl: ['.....##.....', '....####....', '....####....', '....####....', '....####....', '....####....', '....####....', '...######...', '..##.##.##..', '..#..##..#..', '.....##.....', '....#..#....'],
  roll: ['....####....', '..##....##..', '.#........#.', '.#.........#', '#..........#', '#....##....#', '#....##.....', '#.........#.', '.#.......###', '.#........#.', '..##........', '....####....'],
  flip: ['..#.........', '.###........', '#####.......', '..#.........', '..#.........', '..#....###..', '..#...#...#.', '..#..#.....#', '...##......#', '...........#', '..........#.', '......####..'],
  flare: ['.....#......', '.....#......', '..#..#..#...', '...#.#.#....', '....###.....', '#######.####', '....###.....', '...#.#.#....', '..#..#..#...', '.....#......', '.....#......', '............'],
  boost: ['.....#......', '....##......', '....###.....', '...####.#...', '...#####....', '..######.#..', '..##.####...', '.###..###...', '.##....##...', '.##.##.##...', '..#.##.#....', '...####.....'],
};
const svgOf = rows => rows.map((r, y) => [...r].map((c, x) => c === '#' ? `<rect x="${x}" y="${y}" width="1" height="1"/>` : '').join('')).join('');
document.querySelectorAll('svg[data-ic]').forEach(el => { el.setAttribute('viewBox', '0 0 12 12'); el.innerHTML = svgOf(ICONS[el.dataset.ic]); });
// joystick art: pixel ring and knob as tiny canvases scaled up without smoothing
function pixelDisc(size, r0, r1, fill, edge) {
  const c = document.createElement('canvas'); c.width = c.height = size; const x = c.getContext('2d');
  for (let j = 0; j < size; j++) for (let i = 0; i < size; i++) { const d = Math.hypot(i + 0.5 - size / 2, j + 0.5 - size / 2); if (d <= r1 && d >= r0) { x.fillStyle = d > r1 - 1.2 ? edge : fill; x.fillRect(i, j, 1, 1); } }
  return c.toDataURL();
}
{ const ring = pixelDisc(33, 12.5, 16.4, 'rgba(255,211,161,.20)', 'rgba(255,211,161,.75)'), knob = pixelDisc(13, 0, 6.4, 'rgba(255,184,90,.9)', '#0d0918');
  for (const [id, url] of [['stickBase', ring], ['stickKnob', knob], ['stickHintImg', ring]]) { const el = document.getElementById(id); el.style.backgroundImage = `url(${url})`; el.style.backgroundSize = '100% 100%'; } }
{
  const zone = document.getElementById('stickZone'), stick = document.getElementById('stick'), knob = document.getElementById('stickKnob'), hint = document.getElementById('stickHint');
  let id = null, ox = 0, oy = 0; const R = 54;
  const move = (x, y) => {
    let dx = x - ox, dy = y - oy; const L = Math.hypot(dx, dy); if (L > R) { dx *= R / L; dy *= R / L; }
    knob.style.transform = `translate(${dx}px,${dy}px)`;
    const dz = v => Math.abs(v) < 0.12 ? 0 : (v - Math.sign(v) * 0.12) / 0.88;
    input.stick.x = clamp(dz(dx / R), -1, 1); input.stick.y = clamp(dz(dy / R), -1, 1);
    if (Math.hypot(dx, dy) > 10) tutorial.did('move');
  };
  zone.addEventListener('touchstart', e => {
    e.preventDefault(); if (state !== 'play' || id !== null) return;
    const t = e.changedTouches[0]; id = t.identifier; ox = t.clientX; oy = t.clientY;
    stick.style.left = ox + 'px'; stick.style.top = oy + 'px'; stick.style.display = 'block'; hint.style.display = 'none';
    input.stick.on = true; input.stick.used = true; input.auto = false; move(ox, oy);
  }, { passive: false });
  zone.addEventListener('touchmove', e => { e.preventDefault(); for (const t of e.changedTouches) if (t.identifier === id) move(t.clientX, t.clientY); }, { passive: false });
  const end = e => { for (const t of e.changedTouches) if (t.identifier === id) { id = null; input.stick.on = false; input.stick.x = input.stick.y = 0; stick.style.display = 'none'; knob.style.transform = ''; } };
  zone.addEventListener('touchend', end); zone.addEventListener('touchcancel', end);
}
const held = new Set();
const act = (id, down, up) => {
  const b = document.getElementById(id);
  const on = e => { e.preventDefault(); e.stopPropagation(); if (state !== 'play') return; b.classList.add('on'); held.add(id); try { navigator.vibrate && navigator.vibrate(12); } catch (er) {} down(); };
  const off = e => { e.preventDefault(); b.classList.remove('on'); held.delete(id); if (up) up(); };
  b.addEventListener('touchstart', on, { passive: false }); b.addEventListener('touchend', off, { passive: false }); b.addEventListener('touchcancel', off, { passive: false });
  b.addEventListener('mousedown', on); b.addEventListener('mouseup', off); b.addEventListener('mouseleave', e => { if (held.has(id)) off(e); });
};
act('bGun', () => fireGun());
act('bMsl', () => fireMissile());
act('bRoll', () => startRoll());
act('bFlip', () => startFlip());
act('bFlare', () => dropFlare());
act('bBoost', () => { jet.boost = !jet.boost; if (jet.boost) tutorial.did('boost'); });
const CB = id => document.getElementById(id);
const ctlEls = Object.fromEntries(['bGun', 'bMsl', 'bRoll', 'bFlip', 'bFlare', 'bBoost'].map(k => [k, { b: CB(k), cd: CB(k).querySelector('.cd'), ct: CB(k).querySelector('.ct') }]));
let ctlT = 0;
function updateCtl(dt) {
  if (state === 'play' && held.has('bGun')) fireGun(); // hold TIRO to keep firing bursts
  ctlT += dt; if (ctlT < 0.05) return; ctlT = 0;
  const set = (k, frac, cls) => { const c = ctlEls[k]; if (c.cd) c.cd.style.height = Math.round(clamp(frac, 0, 1) * 100) + '%'; for (const n of ['lit', 'ready', 'alarm', 'wait']) c.b.classList.toggle(n, !!(cls && cls[n])); };
  const armed = jet.slots.filter(q => q.armed).length, rl = 4.5 * reloadK();
  const nextSlot = jet.slots.filter(q => !q.armed).reduce((m, q) => Math.min(m, q.t), 1e9);
  const tg = state === 'play' && (enemies.length || boss) ? gunTarget() : null;
  set('bGun', gun.burst > 0 ? 0 : gun.cd / (1.1 * reloadK()), { ready: tg && tg.inCone && gun.cd <= 0, wait: gun.cd > 0 });
  set('bMsl', armed ? 0 : nextSlot / rl, { wait: !armed, ready: armed && tg && tg.dist < 5000 });
  ctlEls.bMsl.ct.textContent = armed; ctlEls.bMsl.ct.classList.toggle('zero', !armed);
  set('bRoll', jet.rollT >= 0 ? 1 - jet.rollT / 1.15 : 0, { alarm: game.incoming && jet.rollT < 0, lit: jet.rollT >= 0 });
  set('bFlip', jet.flipT >= 0 ? 1 : jet.flipCd / (flipDur() + 0.6), { lit: jet.flipT >= 0, wait: jet.flipCd > 0 });
  set('bFlare', jet.flares ? clamp(1 - (T - jet.flareT) / 0.35, 0, 1) : 1, { alarm: game.mslWarn && jet.flares > 0, wait: !jet.flares });
  ctlEls.bFlare.ct.textContent = jet.flares; ctlEls.bFlare.ct.classList.toggle('zero', !jet.flares);
  set('bBoost', 0, { lit: jet.boost });
}

'''
new_js=new_js.replace('const held = new Set();','const tHeld = new Set();').replace('held.add(id)','tHeld.add(id)').replace('held.delete(id)','tHeld.delete(id)').replace('held.has(','tHeld.has(')
s=s[:a]+new_js+s[b:]
# old held Set for keys exists? rename ours if conflict
open(dst,'w').write(s)
print('stage2 ok')
