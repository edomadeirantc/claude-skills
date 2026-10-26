# Repertório de mercado — famílias G–J e o salto fora da caixa

As referências MK01–MK26 (`referencias.md §1.4`) foram validadas pelo
usuário como o nível profissional que a skill deve alcançar. Elas são a
**régua**, não o molde: de cada uma se tira o **movimento** (o verbo da
ideia), a tipografia e o acabamento; a cena, o objeto e as palavras nascem do
cliente. Uma peça que um observador reconheceria como "aquela referência com
outro texto" está reprovada, por melhor que esteja.

Serve para qualquer peça de alto impacto: post único, carrossel, story,
anúncio e slide (formatos em `formatos-e-composicao.md §5.6–§5.7`).

---

## R.1 Famílias

### G · Metáfora de objeto

**Assinatura:** um objeto do ofício, em escala ou estado inesperado, diz a
frase sozinho; fundo limpo (branco, cinza claro ou preto) ou um único
cenário; **um** acento saturado no objeto ou na palavra-chave.
**Refs:** MK03 (um se destaca), MK06 (o papel vira lâmpada), MK10 (menu do
sistema), MK11 (letra vira tecla), MK13 (recorte de luz), MK24 (objeto
tomado pelo tempo).

- **Tipografia:** grotesca compacta e pesada com entrelinha justa, em
  minúsculas com maiúscula inicial (Inter Tight 800, Manrope 800, Archivo
  800); marca-texto do acento atrás de 2–3 palavras; ou serif condensada +
  itálica no acento (MK24).
- **Núcleo de prompt:**
  `A single {OBJECT_OF_THE_TRADE} shown {TRANSFORMATION: becoming X | replacing the letter "Y" in the word "Z" | the only {ACCENT} one among identical grey ones | lit only by a narrow slit of light}, photographed as a premium still life on {BACKGROUND}, soft directional studio light, realistic materials and contact shadows; {ACCENT_HEX} appears only on {ELEMENT}.`
- **Quando usar:** serviço abstrato (consultoria, software, segurança,
  marketing), oferta que precisa de uma ideia em 1 segundo, anúncio.

### H · Cinema com contraponto tipográfico

**Assinatura:** fotografia de cinema ou de filme (paisagem, sala, plateia,
monocromia) em que a tipografia **conversa** com a cena: atravessa, é
engolida, orbita ou literaliza uma expressão.
**Refs:** MK01, MK02, MK08, MK09, MK14, MK19, MK21, MK22.

- **Tipografia:** troca de família no meio da frase (sans leve → serif
  itálica na palavra emocional; MK02, MK21); pilha de 3–4 vozes (MK01);
  palavra única gigante com frases pequenas em volta.
- **Núcleo de prompt:**
  `A cinematic {35mm film | anamorphic} photograph of {SCENE_THAT_LITERALIZES_THE_KEY_PHRASE}, {LIGHT}, {MONOCHROME_OR_PALETTE}; the composition leaves {ZONE} for a giant headline that {passes behind the subject's head | is partly swallowed by the landscape at its last line | is crossed by {OBJECT}}.`
- **Quando usar:** manifesto, posicionamento, capa de carrossel, post único
  de autoridade.

### I · Janela de interface sobre paisagem

**Assinatura:** paisagem ampla e calma (céu, campo, montanha, noite) com uma
janela de app ou site **real do cliente** flutuando no centro; nome ou marca
em grotesca grande acima; uma frase com trecho em bold abaixo; cabeçalho de
3 âncoras (tema · @ · categoria, pela recorrência de
`microtipografia-editorial.md §2.3`) e paginação com seta fina na base. O
cabeçalho e a paginação entram **em camada**, nunca no prompt.
**Refs:** MK07, MK12, MK15, MK17, MK18, MK20, MK23, MK26.

- **Regra de produção:** a janela é **captura real** do produto aplicada em
  camada (Figma/HTML) com sombra suave; o gerador entrega só a paisagem com
  o centro calmo. Gerar a interface inventa letras e logos.
- **Núcleo de prompt (só a paisagem):**
  `A calm wide {LANDSCAPE} photograph, {TIME_OF_DAY} light, {SMALL_HUMAN_FOR_SCALE optional}; the central 70% of the width from 28% to 72% of the height is soft, low-detail {sky|field|water} for a floating app window added later; no text, no UI, no logos.`
- **Quando usar:** SaaS, app, portal do cliente, monitoramento remoto,
  agenda online, série de "ferramentas" ou "bastidores do sistema".

### J · Caderno editorial

**Assinatura:** folha de papel com textura (bege, linho, quadriculado,
fichário), título em serif condensada itálica terminado em **dois-pontos**,
parágrafo curto em itálico, 3 miniaturas em fila ligadas por setas
manuscritas no acento, rodapé `@handle · salvar · →`.
**Refs:** MK04, MK05, MK16, MK25.

- **Exceção do @:** na J o @ pode descer para o rodapé, e no movimento MK13
  pode virar um microrrótulo na cena. A grafia e o tamanho são os mesmos dos
  outros slides da série; só a posição muda.

- **Regra de produção:** a página e as setas podem ser geradas; miniaturas
  são fotos reais do cliente aplicadas em camada.
- **Quando usar:** passo a passo, bastidor de processo, "como funciona",
  estudo de caso, comparação.

Numa série, troque de família só dentro de G–J (ou G–J com o kit da F),
mantendo uma luz, uma paleta, um acento, os mesmos materiais e os mesmos
pares tipográficos (§R.5). Não misture A–E com G–J na mesma série.

---

## R.2 Sistema tipográfico de contraste

Os movimentos que mais aparecem nas MK. Use no máximo **dois** por peça.
Os IDs TM1–TM8 são movimentos tipográficos; não confundir com os templates
T1–T5 de `templates/README.md`.

| Movimento | O que é | Refs | Frase de prompt |
|---|---|---|---|
| TM1 Troca no meio da frase | a palavra emocional muda de sans para serif itálica (ou vice-versa) | MK02, MK21, MK24 | `"{FRASE}" in a light grotesque sans, with the word "{PALAVRA}" set in a large high-contrast serif italic` |
| TM2 Escala extrema | uma palavra gigante (60–90% da largura) e o resto em corpo pequeno | MK02, MK12, MK15 | `the word "{X}" fills 85% of the width; all other lines are small` |
| TM3 Marca-texto | bloco do acento atrás de 2–3 palavras | MK06, MK10, MK11 | `a flat {ACCENT_HEX} highlighter block sits behind "{TRECHO}"` |
| TM4 Palavra-objeto | uma letra ou palavra substituída/atravessada por objeto real | MK02, MK11 | `the letter "{L}" is replaced by a realistic {OBJECT} at the same size` |
| TM5 Pilha de vozes | 3–4 linhas, cada uma numa voz (condensada, serif itálica, numeral) | MK01 | ver `variacao-de-layout.md` L2 |
| TM6 Engolida pela cena | a última linha some atrás do horizonte, da grama ou do sujeito | MK14, MK19 | ver `modelos-e-producao.md §10` (sanduíche) |
| TM7 Âncoras e microrrótulos | texto pequeno só nas bordas (3 âncoras) ou espalhado em pontos da cena | MK03, MK13 | ver `microtipografia-editorial.md` |
| TM8 Sublinhado editorial | parágrafo justificado com sublinhado fino | MK24 | aplicar em camada |

Famílias livres equivalentes: extensa pesada (Unbounded 800, Syne 800,
Archivo Expanded 800); grotesca compacta (Inter Tight 800, Manrope 800);
serif itálica de contraponto (Instrument Serif Italic, Playfair Display
Italic, DM Serif Display Italic); serif condensada editorial (Gloock, Bodoni
Moda Italic em corpo grande); sans leve (Inter 300). Acentos e hífens no
idioma final, sempre conferidos no QA.

---

## R.3 O salto: do repertório para uma ideia que só o cliente poderia ter

Siga os quatro passos **antes** dos três conceitos de `nichos-e-ideias.md
§N.4`; o resultado alimenta as alavancas 9–13 dessa seção.

1. **Verbo da referência.** Para cada MK escolhida, escreva o movimento em
   uma linha com um verbo, sem nomes de objetos: "transformar o material do
   ofício no resultado" (MK06), "literalizar a expressão do público" (MK14,
   MK21), "trocar uma letra pelo objeto" (MK11), "revelar só o essencial no
   escuro" (MK13).
2. **Inventário do cliente.** Liste, a partir do material e do briefing:
   10 objetos que só existem nesse trabalho; 5 expressões que o **público**
   usa para a dor (as palavras dele, não as do profissional); 3 interfaces
   ou documentos que o cliente usa (app, laudo, contrato, agenda, câmera).
3. **Busca fora do nicho.** Com ferramenta de busca disponível, procure
   peças premiadas ou de marcas líderes de **dois nichos vizinhos** e de
   uma linguagem de fora (cinema, sinalização, museu, embalagem, editorial
   de moda). Registre 3 achados com link e o verbo de cada um. Sem achado
   verificável, registre "nenhum"; nunca complete com link não aberto. São
   vocabulário de estudo: não baixe nem anexe ao gerador.
4. **Cruzamento.** Combine verbo × inventário em 6 ideias e reduza a 3
   (seguro, ousado, fora da curva). Cada uma passa por:
   - **2 segundos:** a ideia é entendida sem ler o subtítulo.
   - **Anti-réplica:** lado a lado com a MK de origem e com qualquer R/N/IG/MK
     citada, não é a mesma cena.
   - **Assinatura:** trocando o logo por um concorrente, a peça perderia
     sentido. Se continuar servindo para qualquer marca, volte ao passo 2.

Registro no conceito (`nichos-e-ideias.md §N.4`):
`Movimento: MK11 (letra-objeto) · Achado externo: {link} · Inventário usado: {objeto}, {expressão}`.

---

## R.4 Como cada família muda por formato

| Formato | G · Objeto | H · Cinema | I · Janela | J · Caderno |
|---|---|---|---|---|
| Post único 4:5 | objeto central, frase em 2 linhas, assinatura no rodapé | foto inteira + título entrelaçado | 1 janela, 1 frase | página com 1 miniatura grande |
| Carrossel | capa G, miolo alterna H/J; o objeto-símbolo em no máximo 1/3 dos slides | capa H, miolo alterna escalas (macro, plano aberto, só tipografia), nunca a mesma foto-base | janela em no máximo 1/3 dos slides; os demais em G/H ou só tipografia; paginação em camada | a prancheta/página em no máximo 2–3 slides; o resto em outras escalas (R.5) |
| Story/Reels 9:16 | objeto no terço central | título no meio; topo e base livres | janela menor, centro | evitar: texto pequeno demais |
| Anúncio | o melhor: entende-se sem ler | bom para marca; teste com G | bom para app/SaaS | fraco em mídia paga |
| Slide 16:9 | objeto à direita, texto à esquerda | foto de fundo, título em L8 | janela grande à direita | pouco indicado |

Zonas, proporções e áreas da plataforma em `formatos-e-composicao.md §5.7`.

## R.5 Série com movimento (a família é o fio, não o molde)

Erro visto no caso de consultoria de segurança, carrossel em caderno: os 9
slides saíram com a mesma prancheta vista de cima, o mesmo bloco de texto
no topo e a mesma densidade de texto. O universo estava certo; a série
estava morta. **Carrossel = um universo, não uma cena.** Uma família define
**luz, paleta, acento, materiais e pares tipográficos**; ela não define
cena, escala, câmera, densidade de texto nem cabeçalho. Esses vêm da linha
de cada slide no storyboard (`variacao-de-layout.md §V.5`). Regras para
qualquer carrossel:

1. **Um movimento por slide.** Cada slide nasce de uma MK diferente (ou de
   uma alavanca de `nichos-e-ideias.md §N.4`); dois slides seguidos nunca
   usam o mesmo movimento. Registre o movimento na coluna do storyboard e
   numa linha de comentário fora do texto do prompt.
2. **O objeto-símbolo da família aparece em no máximo 1/3 dos slides**
   (prancheta, janela, papel, painel). Nos outros, mude a escala: foto em
   tela cheia, macro, página só de tipografia, objeto como herói, recorte de
   luz no escuro, folha de contato, mão em cena.
3. **Densidade de texto varia pelo papel do slide.** Em 9 slides, pelo
   menos 3 com até 6 palavras (manchete sozinha), 1 de respiro só
   tipográfico, no máximo 3 com parágrafo.
4. **O cabeçalho varia:** 3 âncoras (capa, falha numerada, checklist), 2
   âncoras, microrrótulos espalhados na cena (MK13) ou só o @. O @ está
   presente em todos os slides; a posição vem do movimento: centro do topo
   por padrão, rodapé na J, microrrótulo no MK13, sempre com a mesma grafia
   e o mesmo tamanho.
5. **Vozes tipográficas pelo papel** (`variacao-de-layout.md §V.3`): serif
   itálica nas frases de reflexão, extensa pesada nos golpes curtos, mono
   nos rótulos.
6. **Referência de continuidade só nos slides do mesmo cenário.** Foto em
   tela cheia de outro lugar vai sem a capa como `--ref`, senão o gerador
   copia a mesa.

Teste antes de entregar: ponha as 9 miniaturas lado a lado. Se três
seguidas parecem a mesma foto com outro texto, refaça o storyboard
(`variacao-de-layout.md §V.5`).

---

## R.6 Prompts base completos G, H, I, J

Um prompt completo por família, na ordem de slots de `prompts.md §6.1`.
Cliente fictício: tudo entre `{}` sai do briefing, do storyboard ou da
bíblia da série. Nenhum deles é Família A: céu cerúleo, grama verde e lime
só entram se a bíblia da marca pedir.

Antes de colar:

- `Camera:` vem da linha do slide no storyboard (`variacao-de-layout.md
  §V.5`), nunca da bíblia. Dois slides seguidos não repetem a câmera.
- `Palette:` e `Light:` vêm da bíblia da série; o acento aparece num só
  elemento.
- As zonas em % são exemplo; a zona do texto vem do layout L# da linha.
- Texto em camada? Troque a linha `Text:` por `Do not include any text,
  letters, numbers, logos, watermarks, signage, UI elements, borders or
  frames.`
- Escreva o movimento numa linha de comentário no topo do `.txt`, por
  exemplo `# slide 3 · MK06 transformar · L8`. Linhas que começam com `#`
  não vão ao gerador (`scripts/generate.py` as remove); em outro gerador,
  apague essas linhas antes de colar.

### G · Metáfora de objeto

```text
A portrait 4:5 premium still-life image for {USE: the cover slide of an Instagram carousel | a single Instagram post | a paid ad} of {CLIENT: a small {NICHE} business}.
Subject: a single {OBJECT_OF_THE_TRADE} {TRANSFORMATION from the chosen concept: turning into {RESULT_OBJECT} at its upper end | the only {ACCENT_NAME} one among {N} identical grey ones | lit only by a narrow slit of light}, real materials with small signs of use, correct proportions and a soft contact shadow.
Setting: {BACKGROUND: a seamless matte {NEUTRAL} studio sweep | one ordinary place from the client's world, kept simple}; nothing else in the frame.
Camera: {CAMERA from the storyboard row: lens · height · angle}.
Light: {LIGHT_SENTENCE from the series bible}, one soft directional key with gentle falloff.
Palette: {PALETTE_SENTENCE from the series bible}; {ACCENT_HEX} appears only on {ELEMENT}; no other strong colors.
Composition: the object sits from {OBJECT_ZONE, e.g. 45% to 88%} of the height, centered; the band from {TEXT_ZONE from layout L#, e.g. 8% to 32%} of the height stays calm and empty for the headline.
Text: render only these exact lines: "{HEADLINE}" in {TYPE_MOVEMENT from §R.2, e.g. TM3: a compact heavy grotesque with a flat {ACCENT_HEX} highlighter block behind "{KEY_WORDS}"}; "{@handle}" small, {HANDLE_POSITION from the storyboard row}. Render only the exact text listed above; no additional lettering, dates, credits, logos or watermarks.
Do not include: extra objects, props on the background, a second accent color, glow, lens flare, people.
```

### H · Cinema com contraponto tipográfico

```text
A portrait 4:5 cinematic photograph for {USE} of {CLIENT}.
Subject: {SCENE_THAT_LITERALIZES_THE_KEY_PHRASE, built from the client's inventory (§R.3): who, doing what, with which real object}; natural poses, real clothing with creases, nobody looking at the camera.
Setting: {PLACE from the client's world, ordinary and well kept}, with {TWO_LIVED_IN_DETAILS from nichos-e-ideias.md §N.5}.
Camera: {CAMERA from the storyboard row: lens · height · angle}.
Light: {LIGHT_SENTENCE from the series bible}; low-key where the scene asks for it.
Palette: {PALETTE_SENTENCE or MONOCHROME_SENTENCE from the series bible}; {ACCENT_HEX} appears only on {ELEMENT}.
Composition: the subject occupies {SUBJECT_ZONE, e.g. the lower 55% of the frame}; the band from {TEXT_ZONE from layout L#, e.g. 14% to 46%} of the height is left for a giant headline that {passes behind the subject's head | is partly swallowed by {the horizon | the seat backs | the counter} at its last line}.
Layering: {the subject's head | the foreground element} overlaps the headline letters with a crisp edge; the rest of the headline stays fully readable.
Finish: shot on {35mm film stock | anamorphic cinema camera}, real grain, true-to-life color, slight halation on highlights; no teal-orange grading, no glow.
Text: render only these exact lines: "{HEADLINE}" in {TYPE_MOVEMENT from §R.2, e.g. TM1: a light grotesque sans with the word "{WORD}" in a large high-contrast serif italic}; "{@handle}" small, {HANDLE_POSITION from the storyboard row}. Render only the exact text listed above; no additional lettering, dates, credits, logos or watermarks.
Do not include: logos, readable signage, watermarks, borders.
```

### I · Janela de interface sobre paisagem (só a paisagem)

```text
A portrait 4:5 calm wide landscape photograph for {USE} of {CLIENT: a {PRODUCT_TYPE} app}, made to receive a real screenshot of the product as a floating window added later.
Subject: {LANDSCAPE the client's users recognize}, {SMALL_HUMAN_FOR_SCALE optional: one tiny figure at {POSITION}}.
Setting: {TIME_OF_DAY}; a quiet scene with one clear horizon.
Camera: {CAMERA from the storyboard row: lens · height · angle}.
Light: {LIGHT_SENTENCE from the series bible}.
Palette: {PALETTE_SENTENCE from the series bible}; no accent color in the landscape (the accent lives in the window).
Composition: the central 70% of the width from 28% to 72% of the height is soft, low-detail {sky | field | water | night sky} for the window; the top 4% to 12% and the bottom 88% to 96% stay calm for the header line and the pagination, both added later as layers.
Finish: {FINISH_SENTENCE from the series bible}, natural grain, no HDR look.
Do not include any text, letters, numbers, UI, windows, screens, logos, watermarks, borders or frames.
```

### J · Caderno editorial

```text
A portrait 4:5 photograph of a single {PAPER: beige textured | linen | graph | ring-binder} page for {USE} of {CLIENT}.
Subject: the page fills 90% of the frame; three empty rectangular frames with thin pencil borders sit in a row from 50% to 76% of the height, left blank for real client photos added later; two hand-drawn arrows in {ACCENT_HEX} marker link frame 1 to frame 2 and frame 2 to frame 3.
Setting: the page rests on {SURFACE from the client's world}, visible only at the edges.
Camera: {CAMERA from the storyboard row: lens · height · angle, e.g. straight top-down | 30-degree tilt from the lower edge}.
Light: {LIGHT_SENTENCE from the series bible}, soft enough to show the paper texture.
Palette: {PALETTE_SENTENCE from the series bible}; {ACCENT_HEX} appears only on the arrows.
Composition: title from 10% to 22% of the height, left-aligned at 8% of the width; short paragraph from 26% to 40%; footer line at 92%.
Text: render only these exact lines: "{TITLE ending with a colon}" in a condensed serif italic; "{PARAGRAPH, max 18 words}" in a small serif italic; "{@handle} · salvar · →" small in the footer. Render only the exact text listed above; no additional lettering, dates, credits, logos or watermarks.
Do not include: photos inside the frames, extra handwriting, sticky notes, logos, a second accent color.
```

A J vale para no máximo 1/3 dos slides de uma série (§R.5.2); as miniaturas
reais entram em camada.

## R.7 Ritmo impacto × leitura e o surreal crível

Pedido validado pelo usuário (segurança eletrônica, 25/10/2026): a série
alterna **slides de impacto** (imagem surreal, quase sem texto) e **slides de
leitura** (copy que explica e prende). Um só tipo cansa: só impacto vira
pôster sem conteúdo, só leitura vira apostila.

| Tipo | Imagem | Texto | Função |
|---|---|---|---|
| **Impacto (I)** | uma ideia visual impossível numa cena fotográfica crível | até 6 palavras | parar o polegar, criar a pergunta |
| **Leitura (L)** | foto calma ou textura da série, espaço amplo para o texto | 20–45 palavras, frases curtas | responder a pergunta e abrir a próxima |

Regras:

1. A capa é sempre **I**. O fechamento pode ser I ou L, com um único pedido.
2. Nunca três slides seguidos do mesmo tipo; padrão I-L-I-L, com o resumo
   (slide de salvar) como L.
3. Cada L termina com um **gancho de passagem** de até 5 palavras que puxa o
   próximo slide ("Agora, o alarme →", "O último é o que mais esquecem →").
   Não é promessa nem número inventado.
4. Cada I responde a uma pergunta que o L seguinte explica: a imagem planta,
   a copy colhe.

**Surreal crível** (para os I): **uma** coisa impossível dentro de uma foto
que, fora isso, é totalmente plausível: luz coerente, sombras de contato,
materiais reais, escala física. Alavancas que funcionam: escala (a casa
dentro da mala), deslocamento (a sala ao vivo na tela, na praia), presença
na ausência (a sombra de alguém lendo numa sala vazia), isolamento (a casa
sozinha no meio do mar). Escreva no prompt `photographed as a real scene;
the only impossible element is {X}`. Mais de um elemento impossível vira
colagem de IA e reprova no QA.

No storyboard (`variacao-de-layout.md §V.5`), escreva `I` ou `L` na coluna
"papel".
