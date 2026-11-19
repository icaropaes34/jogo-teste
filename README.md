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
- **Chefão a cada 5 ondas (5, 10, 15...):** a **Fortaleza**, um bombardeiro de asa voadora com uns 90 m de envergadura, que circula em volta de você com alguns caças de escolta. Uma barra no topo da tela mostra a vida dele. Os **4 motores** são os pontos fracos (losangos laranja): cada míssil tira um bom pedaço, e a rajada também ajuda. As **4 torretas** (quadrados vermelhos) atiram rajadas e podem ser derrubadas com a rajada ou com um míssil. A Fortaleza também lança mísseis, então guarde flares. Com os 4 motores destruídos, ela cai e vale muitos pontos. A cada novo chefão, ela fica mais resistente.
- Cada onda traz mais caças, e eles ficam mais resistentes. Os pontos de cada abate aumentam com a onda.

## Missões

Cada onda tem uma **missão** com objetivo, e cada modo tem as suas (as do modo Força Aérea Brasileira estão na seção dele). Um quadro no canto superior esquerdo mostra o nome, o objetivo e o andamento (no celular ele fica embaixo da barra do topo). Na primeira vez de cada tipo, uma dica explica o que fazer.

- **Caça** (ondas 1, 6, 11...): abata todos os caças inimigos (no modo FAB, os intrusos).
- **Escolta** (ondas 2, 7, 12...): um **cargueiro aliado** quadrimotor, com contorno **verde** e barra de vida, cruza a região em linha reta. Parte dos caças inimigos vai atrás dele em vez de você, e um segundo grupo chega por trás no meio do caminho. Mantenha o cargueiro vivo por 55 segundos até ele chegar ao destino. Se ele cair, a missão fracassa e você ainda precisa limpar a onda.
- **Ataque ao solo** (ondas 3, 8, 13...): **radares** (em terra, com a antena girando) e **barcos de patrulha** (nos lagos) marcados com **losangos amarelos**. Aponte o nariz para baixo: o míssil trava neles e a rajada também acerta. Os barcos atiram para cima quando você chega perto. Alguns caças defendem a área.
- **Defesa da base** (ondas 4, 9, 14...): a **nossa base** (pista, hangares e torre, marcada com um quadrado **azul**) é atacada por **bombardeiros** (marcados com **BOMB**) que chegam um atrás do outro. Cada bomba tira 20% da base; se ela chegar a zero, a missão fracassa. Intercepte e derrube todos antes.
- **Chefão** (ondas 5, 10, 15...): a Fortaleza, como antes.

Missão cumprida vale **300 pontos × a onda**. O resultado aparece também no cartão de melhoria.

Para testar uma missão: `index.html?missao=escort` (ou `hunt`, `strike`, `defend`; no modo FAB, `chase`, `show`, `intercept`, `recon`) força esse tipo em todas as ondas que não são de chefão.

## Caixas de suprimentos (power-ups)

Caixas caem de **paraquedas** no céu, de tempos em tempos (a cada 20 a 30 segundos) e às vezes quando um inimigo é abatido. Cada uma tem a cor e a letra do tipo no HUD, com a distância. Fora da tela, uma seta na borda aponta para ela. Para pegar, **voe através da caixa** (vale 50 pontos).

| Letra | Caixa | Efeito |
|---|---|---|
| **R** (verde) | Conserto | casco +40 |
| **M** (laranja) | Munição | os 4 mísseis e os flares prontos na hora, e recarga rápida por 15 s |
| **E** (azul) | Escudo | 12 s sem levar dano (um anel azul em volta do avião) |
| **A** (rosa) | Ala | um **caça aliado pilotado pelo computador** voa com você por 30 s |

O **ala** é um avião igual ao seu (um jato, ou um Tucano no modo FAB), marcado **ALA** no HUD. Sem inimigos, ele voa em formação ao lado da sua asa direita. Com inimigos por perto, ele escolhe o mais próximo de você, persegue, atira rajadas e lança mísseis. Também ataca a Fortaleza (as torretas) e, nas missões de ataque ao solo, os alvos em terra com mísseis. Os abates dele contam para o seu placar. Quando o tempo acaba, ele sobe e volta para a base. Os tempos dos efeitos ativos aparecem no canto da tela.

## Placar, combo e recordes

- O placar (**PONTOS**) fica no canto superior esquerdo, ao lado do seu **RECORDE**. Quando você passa dele, aparece **NOVO RECORDE!**.
- Abate de avião: 100 × a onda. Radar ou barco: 150 × a onda. Missão cumprida: 300 × a onda. Caixa: 50.
- **Combo:** abates seguidos, com menos de 5 segundos entre um e outro, multiplicam os pontos: x2, x3, até **x5**. O contador e uma barrinha do tempo aparecem no canto.
- **Recordes:** os 10 melhores placares ficam salvos neste navegador (`localStorage`, chave `patrol.recordes`), com onda, modo e data. Os 5 primeiros aparecem no cartão inicial e no cartão de fim de jogo, que avisa quando você bate o recorde ou entra na lista. Se você fechar a página no meio do voo, o placar até ali também é guardado.

## Modo Força Aérea Brasileira

Na tela inicial dá para escolher entre dois modos (clique no cartão do modo, ou aperte **B**). A escolha fica salva.

- **Caça a jato:** o modo original, descrito acima.
- **Força Aérea Brasileira:** você pilota um **Tucano** da **Esquadrilha da Fumaça**, o turboélice de treinamento da FAB, em pixel art. A pintura segue a do Super Tucano da Fumaça: azul brilhante com raios amarelos contornados de branco nas asas e na cauda, cocar da FAB (estrela verde e amarela com disco branco e centro azul) nas asas e na fuselagem, e a bandeirola verde e amarela no leme. A hélice gira na frente, inclusive vista da cabine.
  - **Avião a hélice:** mais lento que o jato (cerca de 450 km/h em cruzeiro e 620 km/h com potência máxima), porém mais ágil nas curvas. O som é de turboélice, com o zumbido das pás.
  - **Objetivo: perseguir e abater.** Aviões **intrusos** voam à sua frente tentando fugir. Eles costuram, dão uma curva brusca quando você cola na cauda deles e soltam **flares** contra os seus mísseis (às vezes despistam). Eles são mais lentos que você na potência máxima, então segure o turbo para alcançar e use a rajada (as metralhadoras ficam nas asas). A partir da onda 2 chegam **caças de escolta** que atiram e lançam mísseis em você. A cada 5 ondas, a Fortaleza aparece como no outro modo.
  - **Fumaça colorida:** o Tucano solta fumaça pela cauda, como nas apresentações da Esquadrilha. A tecla **X** (no celular, o botão **FUMAÇA** na barra do topo) troca entre **bandeira** (verde, amarela e azul se alternando), verde, amarela, azul, branca e desligada.

- **Missões próprias da FAB** (diferentes das do caça a jato):
  - **Perseguição** (ondas 1, 6, 11...): abata os intrusos que fogem à sua frente.
  - **Apresentação da Esquadrilha** (ondas 2, 7, 12...): um circuito de **argolas** no céu, como num show aéreo. Passe por dentro delas na ordem (a próxima é a dourada, com uma seta na borda quando está fora de vista) antes que o tempo acabe. Com a **fumaça ligada**, cada argola vale o dobro. Sem inimigos: é pura pilotagem.
  - **Interceptação** (ondas 3, 8, 13...): **contrabandistas** voam para uma **pista clandestina** (losango vermelho). O objetivo não é abater: **cole na cauda** de cada um, a menos de 400 m atrás dele, por 6 segundos (uma barrinha verde enche embaixo dele) para forçar o pouso. Ele tenta escapar com curvas bruscas. Forçar o pouso vale 250 × a onda; abater vale menos. Se um chegar à pista, a missão fracassa.
  - **Reconhecimento** (ondas 4, 9, 14...): **fotografe** as pistas clandestinas (quadrados roxos com **FOTO**) voando baixo, a menos de 450 m de altura, por cima de cada uma. Caças de escolta defendem a área.
  - A cada 5 ondas, a Fortaleza aparece como no outro modo.
  - O caça aliado das caixas de suprimentos não atira nos contrabandistas (eles devem ser forçados a pousar).

Para abrir direto num modo: `index.html?modo=fab` ou `index.html?modo=jato`.

## Pausa

Aperte **P** ou **Esc** (no celular, o botão **II** na barra do topo; no computador ele também fica no rodapé). O jogo para, e o relógio das missões, do escudo e do combo também. O cartão de pausa tem:

- **Continuar** (ou P / Esc de novo).
- **Trocar para o outro modo**: começa um voo novo no modo caça a jato ou Força Aérea Brasileira.
- **Tela inicial**: encerra o voo e volta ao cartão inicial, onde dá para trocar o modo, ligar o tutorial e ver os recordes.

O placar do voo encerrado vai para os recordes. Trocar de aba ou sair do app também pausa.

## Tutorial

Na primeira vez, o jogo começa com um **tutorial guiado** de 9 passos: pilotar, turbo, tonneau, meia-volta, rajada com o círculo de mira (contra um alvo de treino), míssil, flares (contra um míssil de treino, que não causa dano), pegar uma **caixa de suprimentos** (ela traz o caça aliado, para você ver como ele voa) e troca de visão. As ondas de inimigos só começam quando o tutorial termina. Dá para pular a qualquer momento com **Esc** ou o botão **PULAR TUTORIAL**.

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

| Ação | Mouse / teclado | Celular (`mobile.html`, deitado) |
|---|---|---|
| Pilotar | mover o mouse, ou **W A S D** / setas (W sobe, S desce, A e D fazem a curva) | joystick: arrastar o polegar esquerdo na metade esquerda da tela |
| Tonneau (giro completo) | clique ou **R** | botão **GIRO** |
| Pós-combustor (turbo) | segurar o botão esquerdo (ou Shift) | botão **TURBO** (liga e desliga) |
| Rajada de tiros (15) | **E** ou botão do meio do mouse | botão **TIRO** (segure para continuar atirando) |
| Meia-volta (180°) | **Q** | botão **VOLTA** |
| Soltar flares | **C** | botão **FLARE** |
| Escolher melhoria | **1**, **2**, **3** ou clique | tocar na opção |
| Disparar míssil | clique direito ou **F** | botão **MISSIL** |
| Trocar a visão | **Espaço** | botão **VISÃO** na barra do topo |
| Som liga / desliga | **M** | botão **SOM** na barra do topo |
| Volume dos efeitos e da música | botão **SOM** no rodapé (ou **SOM E MUSICA** no cartão inicial) | botão **SOM** na barra do topo |
| Trocar a fumaça (modo FAB) | **X** | botão **FUMAÇA** na barra do topo |
| Trocar o modo (tela inicial) | **B** ou clique no modo | toque no modo |
| Pausa (continuar, trocar de modo, tela inicial) | **P** ou **Esc** | botão **II** na barra do topo |
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

## Versão para celular

Celulares e tablets abrem sozinhos o **`mobile.html`**, uma versão separada feita para toque:

- **Joystick virtual:** encoste o polegar esquerdo em qualquer lugar da metade esquerda da tela. Ali aparece o joystick. Para cima sobe, para baixo desce, para os lados faz a curva. Solte e o jato volta a voar nivelado.
- **Botões de ação no polegar direito,** em pixel art com ícones: TIRO (o maior), MISSIL, GIRO, VOLTA, FLARE e TURBO. Eles afundam ao toque e vibram de leve. Uma sombra mostra a recarga, e os números mostram mísseis e flares prontos. TIRO acende verde quando o alvo está no círculo de mira. GIRO pisca quando tiros estão chegando, e FLARE pisca em vermelho quando um míssil vem atrás de você.
- **Na horizontal:** ao tocar para voar, o jogo entra em tela cheia e tenta travar na horizontal. Onde o navegador não deixa travar (como no iPhone), aparece o aviso **GIRE O CELULAR**, e o jogo fica pausado enquanto a tela estiver em pé.
- No celular, a visão de cabine mostra só o HUD, sem o painel de instrumentos, para sobrar tela. A resolução interna é mais baixa, para manter a fluidez.
- Para usar a versão de computador num aparelho de toque, abra `index.html?desktop=1` (há um link no cartão inicial do celular).

O `mobile.html` é gerado a partir do `index.html` pelo script `tools/build-mobile.py`. Depois de mudar o `index.html`, rode `python3 tools/build-mobile.py` para atualizar a versão de celular.

## Sons e música

O jogo começa com o som ligado (ele toca a partir do primeiro clique ou toque, como os navegadores exigem). O botão **SOM** abre um painel com liga/desliga e o volume separado dos **efeitos** e da **música**; a escolha fica salva no navegador. **M** liga e desliga.

- **Ambiente:** o ronco do motor sobe com o acelerador, o pós-combustor ruge no turbo, e o vento aumenta com a velocidade e nas curvas fechadas. Na cabine tudo soa mais abafado.
- **Combate:** canhão, mísseis, flares, impactos e explosões. Os sons ficam à esquerda ou à direita conforme a posição, mais baixos e abafados de longe, e a explosão distante chega um pouco depois do clarão (velocidade do som).
- **Alarmes:** bipe rápido de míssil chegando e bipe duplo quando um inimigo está na sua mira.
- **Música:** uma faixa no título, outra no voo calmo, duas que se alternam nas ondas, uma para o chefão e outra no fim de jogo, com troca suave. Fanfarras marcam onda limpa, chegada do chefão, vitória sobre ele e derrota. Nas pausas (melhoria, ajuda, celular em pé) a música fica abafada.

Se o jogo for aberto direto do disco (`file://`), os arquivos de som não carregam e entram os sons sintetizados antigos.

### Créditos dos sons e da música

Todos os arquivos estão em `audio/`, sob licença **CC0 1.0** (domínio público: uso livre, crédito não obrigatório, mas registrado aqui com gratidão).

| Arquivos | Origem | Autor | Licença |
|---|---|---|---|
| `eng_low`, `eng_roar`, `burner`, `prop`, `missile`, `flare`, `gun`, `boom_s`, `boom_l`, `hit` | [Sci-Fi Sounds](https://kenney.nl/assets/sci-fi-sounds) | Kenney | CC0 |
| `tink`, partes de `gun`, `hit`, `flare`, `missile` | [Impact Sounds](https://kenney.nl/assets/impact-sounds) | Kenney | CC0 |
| `lock`, `mslwarn`, `alert` | [Digital Audio](https://kenney.nl/assets/digital-audio) | Kenney | CC0 |
| `click`, `confirm` | [Interface Sounds](https://kenney.nl/assets/interface-sounds) | Kenney | CC0 |
| `wind` | [wind1](https://opengameart.org/content/wind1) | Luke.RUSTLTD | CC0 |
| `mus_title`, `mus_fly`, `mus_combat1`, `mus_combat2`, `mus_over` | [5 Chiptunes (Action)](https://opengameart.org/content/5-chiptunes-action) | Juhani Junkala (SubspaceAudio) | CC0 |
| `mus_boss` | [Epic Boss Battle](https://opengameart.org/content/boss-battle-music) | Juhani Junkala (SubspaceAudio) | CC0 |
| `jg_boss`, `jg_clear`, `jg_win`, `jg_over` | [Homebrew Free Jingle and Fanfare Music](https://github.com/Beatscribe/homebrew_vgm) | Beatscribe | CC0 |

Os efeitos foram cortados, misturados, transformados em loops sem emenda e convertidos para MP3 pelo script `tools/build-audio.py` (precisa de ffmpeg e numpy); a lista de quais arquivos originais entram em cada som está nele. As músicas foram só convertidas para MP3.

## Desempenho

O jogo renderiza numa resolução interna baixa (por volta de 340 pixels de altura) e amplia sem suavização. Se os quadros ficarem lentos, ele reduz a resolução sozinho. Na primeira carga, o terreno é gerado em paralelo (web workers), com barra de progresso.

## Para testar

Parâmetros de URL úteis: `?seed=123` (outro mundo), `?fixedres=1` (desliga a resolução automática), `?desktop=1` (fica na versão de computador num aparelho de toque), `?missao=escort|strike|defend|hunt` (força um tipo de missão).
