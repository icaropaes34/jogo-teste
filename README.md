# Patrol

Um brinquedo de voo em pixel art: você pilota um caça bimotor sobre uma região de lagos no outono, na última luz do dia. Tudo é desenhado por código, num único arquivo `index.html`: o mundo em WebGL2 puro, a cabine em Canvas 2D, sem bibliotecas e sem imagens. O único recurso externo são as fontes do Google Fonts.

## Objetivo

Caças inimigos (escuros, com pontas laranja e contorno vermelho) chegam em ondas, te perseguem e atiram. Sobreviva e derrube todos:

- Quando um inimigo te coloca na mira, aparece **ALERTA: NA MIRA** e a luz **ALERTA** pisca.
- Quando os tiros estão chegando, aparece **TIROS! GIRE!**. Faça um **tonneau** (clique ou **R**): durante o giro os tiros não te acertam.
- Derrube os inimigos com a **rajada** de 15 tiros (tecla **E**) e com os **mísseis** (clique direito ou **F**). Com um inimigo à frente do nariz, o míssil trava nele.
- **Mira da rajada:** um círculo aparece à frente do inimigo mais próximo do nariz, onde os tiros precisam chegar. Quando ele fica verde (com **ATIRE**), a rajada sai direto para ele e os tiros se curvam até o alvo.
- **Meia-volta** (tecla **Q**): vira o jato 180° em pouco mais de um segundo, para o lado do inimigo mais próximo. Ótima para encarar quem está na sua cauda.
- A partir da onda 2, os inimigos também lançam **mísseis**. Aparece **MISSIL! FLARE** e um losango vermelho marca o míssil. Solte **flares** (tecla **C**) para despistá-lo. Os flares recarregam a cada onda.
- **Melhorias entre as ondas:** ao limpar uma onda, o jogo pausa e você escolhe 1 de 3 melhorias (teclas **1**, **2**, **3** ou clique): Motor, Blindagem, Canhão, Recarga rápida, Flares, Manobra, Mira ou Reparo. Elas valem até você ser abatido.
- Setas vermelhas na borda da tela apontam para inimigos fora de vista. Eles também aparecem como pontos no radar da cabine.
- O **casco** (barra no rodapé) se recupera devagar quando você fica alguns segundos sem levar tiros. Se ele zerar, você é abatido e pode voar de novo.
- Cada onda traz mais caças, e eles ficam mais resistentes. Os pontos de cada abate aumentam com a onda.

## Tutorial

Na primeira vez, o jogo começa com um **tutorial guiado** de 8 passos: pilotar, turbo, tonneau, meia-volta, rajada com o círculo de mira (contra um alvo de treino), míssil, flares (contra um míssil de treino, que não causa dano) e troca de visão. As ondas de inimigos só começam quando o tutorial termina. Dá para pular a qualquer momento com **Esc** ou o botão **PULAR TUTORIAL**.

Para fazer o tutorial de novo, use o botão **TUTORIAL: LIGADO / DESLIGADO** na tela inicial (ou a tecla **T** nela).

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
| Pilotar | mover o mouse, ou **W A S D** / setas (W sobe, S desce, A e D fazem a curva) | arrastar o dedo na tela |
| Tonneau (giro completo) | clique ou **R** | botão **GIRO** |
| Pós-combustor (turbo) | segurar o botão esquerdo (ou Shift) | segurar **TURBO** |
| Rajada de tiros (15) | **E** ou botão do meio do mouse | botão **TIRO** |
| Meia-volta (180°) | **Q** | botão **VOLTA** |
| Soltar flares | **C** | botão **FLARE** |
| Escolher melhoria | **1**, **2**, **3** ou clique | tocar na opção |
| Disparar míssil | clique direito ou **F** | botão **MISSIL** |
| Trocar a visão | **Espaço** | botão **VISÃO** |
| Som liga / desliga | **M** ou o botão no rodapé | botão no rodapé |
| Ajuda "Como jogar" | **H** ou o botão **?** | botão **?** |

Os botões do mouse funcionam juntos: dá para segurar o turbo e disparar ao mesmo tempo.

### As três visões

- **Cima** (norte para cima): o jato voa na direção do cursor.
- **Perseguição**: câmera atrás do jato. A distância do cursor até o centro da tela define a curva e a subida ou descida. Cursor no centro = voo nivelado.
- **Cabine**: mesmo controle da perseguição, com painel de instrumentos e HUD.

A troca entre visões é suave (cerca de um segundo).

**Pelo teclado:** W sobe, S desce, A e D fazem a curva, em todas as visões (na visão de cima, A e D viram o jato e W e S mudam a altitude). Soltando as teclas, o jato volta a voar nivelado. Se você mexer o mouse, o controle volta para o mouse.

## Dicas

- **Não dá para bater no chão.** O jato arremete sozinho antes do terreno (a luz **PUXAR** pisca no painel). O perigo são os tiros inimigos.
- Até você mexer o mouse ou usar o teclado, o jato faz curvas em S sozinho.
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
- Luzes: PUXAR, ALT BX (altitude baixa), PC, MISSIL (recarregando), G ALTO, AGUA (voo rasante na água), ALERTA (inimigo mirando, tiros ou míssil chegando), GIRO

No HUD: escada de arfagem alinhada com o horizonte real, fita de proa, velocidade, altitude, G, altura sobre o solo (R), Mach, mísseis prontos (MIS), flares (FLR), casco, círculo de mira da rajada e marcadores em volta dos inimigos com a distância em km.

## Desempenho

O jogo renderiza numa resolução interna baixa (por volta de 340 pixels de altura) e amplia sem suavização. Se os quadros ficarem lentos, ele reduz a resolução sozinho. Na primeira carga, o terreno é gerado em paralelo (web workers), com barra de progresso.

## Para testar

Parâmetros de URL úteis: `?seed=123` (outro mundo), `?fixedres=1` (desliga a resolução automática), `?touch=1` (mostra os botões de toque).
