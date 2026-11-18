# Patrol

Um brinquedo de voo em pixel art: você pilota um caça bimotor sobre uma região de lagos no outono, na última luz do dia. Tudo é desenhado por código, num único arquivo `index.html`: o mundo em WebGL2 puro, a cabine em Canvas 2D, sem bibliotecas e sem imagens. O único recurso externo são as fontes do Google Fonts.

## Como jogar no navegador

### Jeito mais fácil: GitHub Pages

1. No GitHub, abra o repositório e vá em **Settings → Pages**.
2. Em **Build and deployment → Source**, escolha **Deploy from a branch**.
3. Escolha a branch `main` e a pasta `/ (root)`, e clique em **Save**.
4. Espere um ou dois minutos. O jogo fica em:
   **https://icaropaes34.github.io/jogo-teste/**

### No seu computador

Baixe o `index.html` e abra no Chrome, Edge ou Firefox. Se o navegador reclamar de arquivo local, rode um servidor simples na pasta:

```bash
python3 -m http.server 8000
```

e abra `http://localhost:8000`.

Precisa de um navegador com WebGL2 (qualquer Chrome, Edge, Firefox ou Safari recente).

## Controles

| Ação | Mouse / teclado | Toque (celular, deitado) |
|---|---|---|
| Pilotar | mover o mouse | arrastar o dedo na tela |
| Tonneau (giro completo) | clique | botão **GIRO** |
| Pós-combustor (turbo) | segurar o botão esquerdo (ou Shift) | segurar **TURBO** |
| Disparar míssil | clique direito ou **F** | botão **FOGO** |
| Trocar a visão | **Espaço** | botão **VISÃO** |
| Som liga / desliga | **M** ou o botão no rodapé | botão no rodapé |
| Ajuda "Como jogar" | **H** ou o botão **?** | botão **?** |

Os botões esquerdo e direito funcionam juntos: dá para segurar o turbo e disparar ao mesmo tempo.

### As três visões

- **Cima** (norte para cima): o jato voa na direção do cursor.
- **Perseguição**: câmera atrás do jato. A distância do cursor até o centro da tela define a curva e a subida ou descida. Cursor no centro = voo nivelado.
- **Cabine**: mesmo controle da perseguição, com painel de instrumentos e HUD.

A troca entre visões é suave (cerca de um segundo).

## Dicas

- **Não dá para bater.** O jato arremete sozinho antes do terreno (a luz **PUXAR** pisca no painel).
- Até você mexer o mouse pela primeira vez, o jato faz curvas em S sozinho (luz **AUTO**).
- Desça bem baixo sobre um lago para levantar água e deixar uma esteira.
- O míssil vai para onde o nariz aponta. Se você estiver nivelado, ele acerta o chão à frente. São 4 nas asas, e cada um volta a ficar pronto alguns segundos depois do disparo (os quadradinhos no rodapé mostram quantos estão prontos).
- Na terra o impacto deixa uma cratera queimada com brasas; na água, uma coluna de água e espuma.

## O painel da cabine

Todos os instrumentos mostram valores reais do voo:

- **VEL / KT**: velocidade em nós · **ATIT**: horizonte artificial · **ALT**: altitude em pés, com dígitos
- **CURVA**: indicador de curva e derrapagem · **PROA**: bússola · **VV**: velocidade vertical
- **MAPA SOLO**: radar âmbar que mapeia o terreno à frente (6 km), com varredura
- **RPM / TEMP**: motores esquerdo (E) e direito (D) · **HORA**: relógio com a hora local
- **MAN**: manete, que acompanha o pós-combustor (**PC**)
- Luzes: PUXAR, ALT BX (altitude baixa), PC, MISSIL (recarregando), G ALTO, AGUA (voo rasante na água), AUTO, GIRO

No HUD: escada de arfagem alinhada com o horizonte real, fita de proa, velocidade, altitude, G, altura sobre o solo (R), Mach e mísseis prontos (MIS).

## Desempenho

O jogo renderiza numa resolução interna baixa (por volta de 340 pixels de altura) e amplia sem suavização. Se os quadros ficarem lentos, ele reduz a resolução sozinho. Na primeira carga, o terreno é gerado em paralelo (web workers), com barra de progresso.

## Para testar

Parâmetros de URL úteis: `?seed=123` (outro mundo), `?fixedres=1` (desliga a resolução automática), `?touch=1` (mostra os botões de toque).
