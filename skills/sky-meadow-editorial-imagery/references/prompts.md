# Arquitetura de prompt e biblioteca

## 6. Arquitetura do prompt

### 6.1 Ordem dos slots

Para Gemini/Nano Banana, escreva **frases descritivas**, não listas de
palavras-chave. Siga esta ordem:

| # | Slot | Pergunta que responde |
|---|---|---|
| 1 | FORMATO E PROPÓSITO | Que peça é e para quê |
| 2 | SUJEITO | O herói da ideia: objeto, pessoa, gesto, material |
| 3 | CENÁRIO | Escala/cena da linha do storyboard (`variacao-de-layout.md §V.5`) |
| 4 | CÂMERA | Lente, altura, ângulo da linha do storyboard (nunca da bíblia) |
| 5 | LUZ | Hora, direção, qualidade |
| 6 | PALETA | Frase de paleta da bíblia da série + acento único |
| 7 | COMPOSIÇÃO E ESPAÇO NEGATIVO | Zonas da [formatos-e-composicao.md §5](formatos-e-composicao.md) em porcentagem |
| 8 | CAMADAS | Se o sujeito invade a zona do título |
| 9 | ACABAMENTO | CGI limpo ou filme 35 mm |
| 10 | EXCLUSÕES | Sem texto, logos, artefatos |

### 6.2 Template mestre

```text
A {FORMAT} {FINISH_SHORT} image for {USE: the cover slide of an Instagram carousel | the {N}th slide of an Instagram carousel | a single Instagram post | a website hero | …}.
{SUBJECT_SENTENCE}
It is set {SETTING_SENTENCE}.
Camera: {CAMERA_SENTENCE from this slide's storyboard row}.
Light: {LIGHT_SENTENCE}.
Palette: {PALETTE_SENTENCE from the series bible}{ACCENT_CLAUSE}; no other strong colors.
Composition: {SAFE_ZONE_SENTENCE}
{LAYER_SENTENCE}
Finish: {FINISH_SENTENCE}.
Do not include any text, letters, numbers, logos, watermarks, signage, UI elements, borders or frames.
```
Este template é a variante **sem texto**. Quando a copy for aplicada pelo
gerador, substitua a última frase por uma lista fechada dos textos exatos
(título, subtítulo, CTA e, se ativado, cabeçalho). Termine com: `Render only
the exact text listed above; no additional lettering, dates, credits, logos
or watermarks.` Não misture a lista com a proibição geral de letras/números.

### 6.3 Banco de frases por slot

**Câmera** (exemplos; a escolha vem da linha do storyboard, e dois slides seguidos não repetem a mesma)
- Rente ao chão: `low camera height just above the grass, slight upward angle, 28mm lens, deep focus on the subject`
- Herói monumental: `camera placed below the crest looking up, 35mm lens, subject silhouetted against the sky`
- Perspectiva forçada: `very low angle, 20mm wide lens, the nearest hand/object almost touching the lens, strong perspective`
- Aérea: `high aerial view, 50mm equivalent, looking down at a shallow angle`
- Para cima: `worm's-eye view pointing straight up`

**Luz**
- L1 Meio-dia limpo (padrão): `clear bright midday sunlight from high above, soft natural shadows, crisp air`
- L2 Contraluz dourada: `late-afternoon sun low behind the subject, warm golden rim light on grass tips and edges, gentle glow`
- L3 Entardecer pastel (R11): `soft pastel dusk, pink and lavender clouds, diffuse warm light`
- L4 Estúdio (R01): `large soft studio key light from the front-left, subtle fill, soft contact shadow on the seamless floor`
- L5 Noir (R02): `low-key moody light, deep shadows, a single soft spotlight on the accent figure`

**Acabamento**
- F1 CGI limpo: `hyperreal 3D render with photographic lighting, physically accurate materials, crisp detail, clean and calm, subtle atmospheric haze at the horizon` — **só para peças sem pessoas**; com pessoas gera pele de cera.
- F2 Filme 35 mm: `shot on 35mm color film, fine natural grain, slightly soft highlights, true-to-life color, authentic candid feel`
- F3 Moda editorial: `high-end editorial fashion photography, sharp detail, natural skin texture, minimal retouching`
- F4 Fotografia editorial real (**padrão para pessoas**): ver `realismo-fotografico.md §R.2` e o bloco §R.6.

**Materiais para objetos-herói**
`clear glass with soft internal refractions` · `frosted glass` · `polished chrome` ·
`matte ceramic` · `natural oak wood` · `soft upholstered fabric with deep tufting` ·
`brushed aluminium`

**Acento** (`{ACCENT_CLAUSE}`)
- `, with a single vivid lime-green (#D4FF1A) accent on {ELEMENT}`
- `, with a single coral (#FF5A3C) accent on {ELEMENT}`
- `, set against a warm amber (#E8940F) seamless backdrop`

Hex no prompt orienta, mas não garante a cor exata: confira no QA e corrija
por edição ou no tratamento.

**Camadas** (`{LAYER_SENTENCE}`)
- Com texto atrás: `The top of the subject rises about 10% into the headline zone; its silhouette is crisp and sharply defined against a smooth background, with no motion blur, so it can be cleanly cut out.`
- Sem texto atrás: `The subject stays fully below the headline zone with clear background between them.`

### 6.4 Regras de escrita

- Um sujeito por frase; um herói por imagem.
- Posições em **porcentagem ou terços**, nunca "à esquerda" sozinho.
- Diga o que deve estar **vazio** com tanta precisão quanto o que deve
  aparecer.
- Proporção vai no **parâmetro** do modelo, não só no texto.
- Não cite fotógrafos ou artistas vivos, celebridades, personagens ou marcas
  ([SKILL.md §13](../SKILL.md)). Descreva as qualidades visuais.
- Prompt em inglês; texto que for aparecer na imagem, entre aspas, no idioma
  final.

### 6.5 Referências e cabeçalho editorial

Antes de preencher os slots, execute a consulta visual de `acervo-visual.md`
e registre os IDs consultados fora do prompt. Anexe ao gerador somente
imagens autorizadas, informando a função de cada uma. Se entregar um prompt
para outro terminal ou gerador, diga quais arquivos devem acompanhá-lo;
um caminho local ou ID no texto não envia uma imagem por si só.

Se a peça pedir microlegendas no topo, inclua o bloco e as três strings exatas
de `microtipografia-editorial.md §4`, adaptadas ao tema. Defina os slides
escolhidos e reutilize as mesmas âncoras. No modo sobreposição, gere a faixa
vazia e entregue os rótulos separadamente para composição tipográfica.

Carrossel de Instagram: o @handle exato entra na lista fechada de textos,
centralizado no topo, em todos os slides (`microtipografia-editorial.md §2.1`
e §4, variante Instagram). Família F: bloco base em
`familia-social-conversao.md §F.6`; SaaS: `saas.md §S.6`.

---

## 15. Prompts prontos

Substitua os campos `{...}`. Cada exemplo segue o template da §6.2.

Os exemplos completos da Família A (hero, carrossel, panorama, janela de céu) estão em
`familia-ceu-campo.md`, "Apêndice A · prompts prontos da Família A". Para G–J, parta
dos núcleos de `repertorio-mercado.md §R.1`; em carrossel, cada slide segue a sua linha
do storyboard (`variacao-de-layout.md §V.5`).

### P11 · Carrossel 1080×1350 — capa de conversão (F1) com @handle

Use o bloco de `familia-social-conversao.md §F.6` com a série preenchida.
Exemplo de sujeito (produto na pele): `A {PERSON}'s hands, cropped at the wrists, cradle the {PRODUCT} against {BODY_PART}; {SKIN_AND_NAIL_DETAILS}; the label faces the camera and is reproduced exactly as in the reference image.`

### P12 · Carrossel — miolo com especialista do nicho (F4)

```text
A portrait {3:4 | 4:5} photograph for an inner slide of the same Instagram carousel. {Only if the storyboard row marks "mesmo lugar da capa = sim": Reference image 1 is the approved cover; keep the same light, colors and the same person's general look and clothing; build a new framing, camera and scale; do not copy its layout or typography.}
Camera: {CAMERA from this slide's storyboard row}.
{PROFESSIONAL of the niche, no recognizable real person}, {NICHE_GESTURE_OR_OBJECT that is not the niche cliché}, warm directional light, natural skin texture.
Composition: the subject occupies 8% to 70% of the height; from 55% downward the photograph fades into near-black; keep 4–9% calm for the handle line.
Text, rendered exactly:
- "{@handle}" centered at the top, baseline at {6% (4:5) | 8.8% (3:4 for crop)}.
- Only the side labels this slide gets in the recurrence table (`microtipografia-editorial.md §2.3`); in a middle slide usually: "{PASSO 2/4}" left-aligned at 6% of the width, small uppercase sans, same baseline. Category pill only on slides 1–2.
- Headline centered, 56% to 80%: "{TÍTULO}".
- Subline, small sans, 82%: "{APOIO}".
- Reserved band: from 86% to 96% of the height keep only calm dark background, with no text, dots, squares, numbers or shapes (page counter added later as an overlay).
Render only the exact text listed above; no additional lettering, dates, credits, logos or watermarks.
```

### P13 · Carrossel — fechamento (F5)

```text
A portrait {3:4 | 4:5} closing slide of the same Instagram carousel, plain {#0A0A0A | #FFFFFF} background matching the series, no photograph.
Text, rendered exactly, left-aligned at 8% of the width, block centered vertically:
- "{@handle}" centered at the top, baseline at {6% (4:5) | 8.8% (3:4 for crop)}; optional action label "{AGORA | SALVE}" right-aligned at 94% on the same baseline.
- Headline in the series headline font: "{PERGUNTA OU CONVITE}".
- Subline, small sans: "{APOIO}".
- An outlined pill with a bookmark icon and "{CTA, ex.: SALVAR ESTE POST | PEÇA O SEU NO DIRECT}".
- Reserved band: from 86% to 96% of the height keep only calm background, with no text, dots, squares, numbers or shapes (page counter added later as an overlay).
Render only the exact text listed above; no additional lettering, dates, credits, logos or watermarks.
```

---

## 16. Exclusões padrão

Inclua o equivalente no prompt ou no `--no` do modelo:

- texto, letras, números, logos, marcas d'água, placas, interface, molduras;
- pessoas reais, celebridades, personagens, bandeiras, insígnias;
- dedos extras, mãos deformadas, membros fundidos;
- grama de plástico/carpete, nuvens clonadas, horizonte torto involuntário;
- HDR, halos, lens flare excessivo, glow neon, gradientes roxos/índigo;
- segundo acento cromático, objetos extras no céu, sol na zona do título.
