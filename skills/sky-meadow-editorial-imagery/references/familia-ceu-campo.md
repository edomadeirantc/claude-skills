# Família A — Céu & Campo editorial

**Melhor para:** natureza, bem-estar, território. Para marca, SaaS ou
"fora da caixa", comece por G–J (`repertorio-mercado.md §R.1`).

## 2. DNA visual — 8 pilares

Cada pilar já vem com vocabulário pronto para prompt (em inglês).

1. **Céu como página** — gradiente cerúleo saturado: profundo no topo,
   claro no horizonte; cúmulos brancos nas laterais, nunca atrás do título.
   `deep saturated cerulean sky graduating to pale blue at the horizon, a few crisp white cumulus clouds kept to the edges`
2. **Terra como pedestal** — crista de colina curva ou campo amplo, grama
   densa com lâminas individuais, flores silvestres pontuais (amarelas,
   brancas, rosa). `a rounded grassy hill crest, dense lush grass with individually defined blades, scattered small wildflowers`
3. **Um monumento** — um único sujeito ou objeto, cotidiano ou surreal,
   isolado contra o céu, ocupando 15–35% da altura do quadro.
   `a single {object} stands alone on the crest, silhouetted cleanly against the sky`
4. **Profundidade em camadas** — primeiro plano (grama/flores desfocadas),
   plano médio (sujeito nítido), fundo (céu). É o que permite texto entre
   camadas. `soft out-of-focus grass and flowers in the immediate foreground, tack-sharp subject in the midground`
5. **Escala e ponto de vista** — câmera rente ao chão olhando levemente
   para cima, lente 24–35 mm; ou perspectiva forçada com objeto quase na
   lente. `low camera height close to the ground, slight upward angle, 28mm lens`
6. **Luz limpa** — sol alto e claro ou contraluz dourada de fim de tarde;
   sombras suaves; sem HDR. `clear bright midday sunlight, soft natural shadows, no HDR look`
7. **Um acento** — apenas uma cor fora do sistema céu/grama/branco por peça
   (lime, coral ou âmbar), aplicada ao objeto, roupa ou fundo.
8. **Acabamento** — CGI hiper-real limpo **ou** fotografia de filme 35 mm
   com grão fino. Nunca os dois na mesma série.

---

## 3. Paleta e contraste

| Token | Hex | Uso | Branco sobre ele | Tinta `#0B1630` sobre ele |
|---|---|---|---|---|
| `sky-zenith` | `#0E4DB3` | Topo do céu | **7,69:1** ✔ texto livre | 2,33:1 ✘ |
| `sky-mid` | `#2F80D9` | Meio do céu | 4,03:1 · só título grande (≥24 px, ou ≥18,66 px bold) | 4,45:1 · só título grande |
| `sky-horizon` | `#A8D5F4` | Horizonte | 1,56:1 ✘ | **11,51:1** ✔ |
| `cloud` | `#F3F7FB` | Nuvens | 1,08:1 ✘ | 16,65:1 ✔ |
| `grass-shadow` | `#24510F` | Grama na sombra | 9,30:1 ✔ | 1,93:1 ✘ |
| `grass-mid` | `#4C9A1E` | Grama | 3,53:1 · só título grande | 5,08:1 ✔ |
| `grass-light` | `#9CCB3B` | Grama ao sol | 1,91:1 ✘ | 9,40:1 ✔ |
| `accent-lime` | `#D4FF1A` | Acento esporte | 1,16:1 ✘ | **15,46:1** ✔ |
| `accent-coral` | `#FF5A3C` | Acento marca | 3,10:1 · só título grande | 5,79:1 ✔ |
| `accent-amber` | `#E8940F` | Fundo estúdio | 2,42:1 ✘ | 7,40:1 ✔ |
| `ink` | `#0B1630` | Texto escuro | 17,92:1 ✔ | — |

Valores aproximados das referências; contraste calculado pela fórmula WCAG.

**Regras de prompt derivadas do contraste**

- Texto **branco** → peça céu profundo e sem nuvens na zona do título:
  `the headline zone is uninterrupted deep cerulean sky, no clouds and no bright haze behind it`.
- Texto **escuro (tinta)** → peça céu claro e uniforme na zona do título:
  `the headline zone is a smooth pale sky-blue gradient, evenly lit`.
- Texto sobre **lime** → sempre tinta escura ou verde-escuro (R06).
- Nunca deixe o título cruzar a linha do horizonte: o contraste inverte no meio
  da palavra.

---

## 4. Arquétipos de composição

### Tabela de decisão

| Objetivo da peça | Arquétipo principal | Alternativa |
|---|---|---|
| Marca, produto, símbolo, lançamento | A · Monumento na colina | E · Objeto gigante |
| Software, criação, trabalho, educação | B · Horizonte de campo | C · Janela de céu |
| Bem-estar, natureza, calma, sustentabilidade | B · Horizonte de campo | C · Janela de céu |
| Esporte, energia, performance | D · Perspectiva forçada | E · Objeto gigante |
| Liderança, jornada, decisão | F · Caminhante solitário | A |
| Diferenciação, "fuja do comum" | G · Um se destaca | E |
| Comunidade, alegria, equipe, família | H · Alegria na crista | B |

---

### A · Monumento na colina (R05, R07, R11, R12)

Um objeto ou figura no topo de um monte gramado, recortado contra o céu.

- **Melhor em:** hero desktop centralizado, hero mobile, capa de carrossel.
- **Texto:** acima do objeto, na faixa de céu; o topo do objeto pode invadir
  a base do título (sanduíche).
- **Núcleo de prompt:**
  `A single {OBJECT} stands alone on the crest of a rounded grassy hill, seen from a low camera close to the ground. The hill fills the lower {N}% of the frame and curves gently out of frame on both sides. Behind it, a deep saturated cerulean sky.`
- **Objetos que funcionam:** símbolo 3D de vidro/cromo, escultura, produto
  real ampliado, objeto do ofício da marca transformado. Mesa, cadeira,
  notebook e sofá na colina são assinaturas das referências (R01/R05/R12):
  não use.
- **Armadilhas:** objeto pequeno demais (<12% da altura), monte sem curvatura,
  grama de plástico, objeto flutuando sem contato com a grama.

### B · Horizonte de campo (R03, R10, R14)

Campo amplo, horizonte no terço inferior, céu dominante.

- **Melhor em:** hero desktop com texto à esquerda ou centralizado; slides
  internos de carrossel; fundo de seção.
- **Texto:** céu central/superior.
- **Núcleo:** `A wide open meadow with the horizon in the lower third, camera just above the grass tips so the nearest blades and wildflowers are softly blurred in the foreground. {OPTIONAL_SUBJECT} The sky occupies the upper two thirds.`
- **Armadilhas:** horizonte inclinado, flores em excesso (vira estampa),
  nuvens no centro.

### C · Janela de céu (R04, R16)

Câmera apontada para cima; folhagem emoldura um vazio de céu central.

- **Melhor em:** hero mobile 9:16, story, slide de citação, slide final.
- **Texto:** centro exato do vazio.
- **Núcleo:** `Worm's-eye view looking straight up at the sky, framed on all edges by {FOLIAGE: sunlit tree canopies | large banana leaves}. The foliage forms an irregular frame and leaves a large clean area of sky in the center, about {N}% of the frame.`
- **Armadilhas:** moldura fechada demais, sol estourado no centro, folhas
  cruzando a zona de texto.

### D · Perspectiva forçada esportiva (R06, R13)

Atleta em ângulo baixo; mão, raquete ou bola quase encostando na lente.

- **Melhor em:** hero desktop e mobile de esporte/performance; capa de carrossel.
- **Texto:** título gigante condensado **atrás** do atleta; mão/bola na frente.
- **Núcleo:** `Dynamic low-angle sports photograph. A {ATHLETE_DESCRIPTION} reaches toward the camera, {HAND_OR_OBJECT} very close to the lens and large in frame, with the body receding behind it. {SECONDARY_OBJECT} in the near foreground, slightly soft. Bright blue sky with white clouds behind.`
- **Armadilhas:** mão deformada, dedos extras, desfoque de movimento na
  silhueta (impede recorte), logotipos de marcas esportivas.

### E · Objeto gigante em estúdio (R01)

Pessoa interagindo com um objeto várias vezes maior que ela, em fundo
contínuo de uma cor.

- **Melhor em:** hero mobile, capa de carrossel, campanha.
- **Texto:** faixa superior vazia do fundo, ou sobre a base do objeto.
- **Núcleo:** `Full-body editorial fashion photograph on a seamless {ACCENT_COLOR} studio backdrop. A {PERSON_DESCRIPTION} leans casually on an enormous {OBJECT}, several times larger than them, which dominates the frame. Soft large-source studio light, gentle floor shadow.`
- **Armadilhas:** escala ambígua (objeto parecendo normal), fundo com
  emenda visível, texturas falsas no objeto.

### F · Caminhante solitário (R09)

Vista aérea ou alta; uma figura minúscula numa vastidão de grama ondulada.

- **Melhor em:** hero desktop (texto sobre a grama escura), slide de
  manifesto, slide de transição.
- **Texto:** terço superior, sobre grama em sombra (branco contrasta).
- **Núcleo:** `High aerial view over an endless field of long wind-swept grass forming waves and swirls. A lone {FIGURE} walks along a narrow trodden path, small in the frame, placed in the lower-middle third.`

### G · Um se destaca (R02)

Grupo repetitivo em tons escuros; uma figura em cor de acento.

- **Melhor em:** campanha de diferenciação; capa de carrossel.
- **Variante noturna** do sistema: fora da paleta céu/grama; o acento é o
  único ponto de cor.
- **Núcleo:** `A dense crowd of identical figures in dark suits and dark hats, faces in shadow, filling the frame. Exactly one figure in the upper center wears a vivid {ACCENT} suit and is lit, standing out. Low-key moody lighting.`
- **Armadilhas:** rostos reconhecíveis, multidão sem padrão, mais de um
  elemento colorido.

### H · Alegria na crista (R08, R14)

Pessoas espontâneas — de costas, correndo ou saltando — na linha da crista.

- **Melhor em:** comunidade, educação, eventos, slides internos.
- **Texto:** céu superior; as figuras ficam pequenas e baixas.
- **Núcleo:** `Candid moment on a grassy ridge under a vast deep blue sky: {GROUP} {ACTION: jump with arms and legs outstretched | run away from the camera}, small in the frame, silhouetted on the ridge line.`
- **Armadilhas:** rostos frontais (direito de imagem), poses posadas, membros
  fundidos em salto.

---

## Apêndice A · prompts prontos da Família A

Exemplos completos da Família A, movidos de `prompts.md §15`. Mostram
estrutura (zonas, camadas, luz, exclusões); vários sujeitos são
composições-assinatura das referências. Troque sujeito e cena pelo universo
da marca (`referencias.md §0`). Em carrossel, câmera e cena de cada slide vêm
da linha do storyboard (`variacao-de-layout.md §V.5`), não deste apêndice.

### A-P1 · Hero desktop 16:9 — Monumento (A), texto branco centralizado

```text
A wide 16:9 hyperreal image for a website hero section.
A single {OBJECT, e.g. "sculptural asterisk-shaped symbol made of clear glass with soft internal refractions, one arm in solid coral"} stands alone on the crest of a rounded grassy hill, firmly resting in the grass and casting a soft shadow.
It is set on a hill covered in dense lush grass with individually defined blades and a few small yellow and white wildflowers; the hill fills the lower 30% of the frame and curves out of frame on both sides.
Camera: placed slightly below the crest looking up, 35mm lens, the subject silhouetted against the sky, everything in sharp focus except the nearest grass blades.
Light: clear bright midday sunlight from high above and slightly behind the camera, soft natural shadows, crisp air.
Palette: deep saturated cerulean sky graduating to pale blue near the horizon, lush natural green grass, crisp white clouds, with a single coral (#FF5A3C) accent on the one arm of the symbol; no other strong colors.
Composition: leave the band between 15% and 45% of the frame height, across the central half of the width, as clean uninterrupted deep blue sky reserved for a headline. Keep a few clouds only near the left and right edges. Center the object horizontally, its top at about 45% and its base at about 75% of the frame height.
The top of the object rises slightly into the headline zone; its silhouette is crisp against a smooth sky, with no motion blur, so it can be cleanly cut out.
Finish: hyperreal 3D render with photographic lighting, physically accurate glass and grass, calm and clean, subtle atmospheric haze at the horizon.
Do not include any text, letters, numbers, logos, watermarks, signage, UI elements, borders or frames.
```

### A-P2 · Hero mobile 9:16 — derivado do A-P1 (usar `--ref` do desktop aprovado)

```text
A vertical 9:16 hyperreal image for a mobile website hero.
Use the reference image only for the object, materials, light, palette and finish. Recompose the scene natively for a tall vertical frame; do not crop or stretch the reference.
The same object stands on the crest of the same rounded grassy hill, which now fills the lower 30% of the frame.
Camera: low, slightly below the crest, 28mm lens, looking up.
Composition: keep the top 8% as quiet sky margin; reserve 10% to 38% of the height as clean deep blue sky with no clouds for a headline. Center the object, occupying roughly 40% to 72% of the height and about 60% of the width. The bottom 18% is calm, evenly shaded grass with no bright flowers, reserved for a button.
The top of the object rises slightly into the headline zone, with a crisp silhouette and no motion blur.
Do not include any text, letters, numbers, logos, watermarks, signage, UI elements, borders or frames.
```

### A-P3 · Hero desktop 16:9 — Horizonte (B), texto escuro à esquerda

```text
A wide 16:9 photographic image for a website hero section.
A wide open meadow on a clear day, with small daisies and yellow wildflowers; the nearest blades and flowers are close to the lens and softly blurred.
Camera: just above the grass tips, 24mm lens, horizon placed at 72% of the frame height, perfectly level.
Light: clear bright late-morning sunlight, soft shadows.
Palette: sky graduating from medium cerulean at the top to a smooth pale sky-blue near the horizon, lush natural green grass, white daisies; no other strong colors.
Composition: keep the left 48% of the frame as smooth, evenly lit pale-to-medium blue sky with no clouds and no objects, reserved for dark text. Allow soft cumulus clouds only in the right third. The densest flowers sit in the lower-right corner.
Finish: shot on 35mm color film, fine natural grain, true-to-life color.
Do not include any text, letters, numbers, logos, watermarks, signage, UI elements, borders or frames.
```

### A-P4 · Hero esporte 16:9 — Perspectiva forçada (D), título gigante atrás

```text
A wide 16:9 dynamic sports photograph for a website hero section.
A {ATHLETE, e.g. "tennis player in a plain white polo and cap, no visible brand marks"} leans toward the camera and reaches one open hand toward the lens; the hand is very close and large in frame with five natural fingers, the body receding behind it.
A tennis ball floats in the lower-left foreground, very close to the lens, slightly soft.
It is set outdoors against an open sky; no court lines, fences or spectators visible.
Camera: very low angle, 20mm wide lens, strong perspective, focus on the hand and face.
Light: bright midday sun, crisp highlights, soft shadows.
Palette: bright cerulean sky with a few white clouds, white clothing, the yellow-green ball as the only accent; no other strong colors.
Composition: the athlete's head and hand occupy the center, between 30% and 65% of the width; leave the band between 10% and 60% of the height behind the athlete as open sky, reserved for a giant condensed headline that will pass behind the athlete and in front of the sky.
The athlete's silhouette is crisp with no motion blur, so it can be cleanly cut out.
Finish: high-end editorial sports photography, sharp detail, natural skin texture.
Do not include any text, letters, numbers, logos, brand marks, watermarks, signage or UI elements.
```

### A-P5 · Hero mobile 9:16 — Objeto gigante em estúdio (E)

```text
A vertical 9:16 editorial fashion photograph for a mobile website hero.
A person in a relaxed cream outfit and sunglasses, no visible brand marks, leans casually with folded arms on top of an enormous {OBJECT, e.g. "felt tennis ball"}, which is several times larger than them and dominates the lower half of the frame.
It is set on a seamless warm amber (#E8940F) studio backdrop with no visible seam or floor edge.
Camera: eye level with the object's top, 50mm lens, full body visible.
Light: large soft studio key light from the front-left, subtle fill, soft contact shadow under the object.
Palette: warm amber backdrop, the object's natural color as the only accent, cream clothing; no other strong colors.
Composition: reserve the top 35% as clean, evenly lit backdrop for a headline. The person's head sits at about 40% of the height; the object spans 45% to 92%.
Finish: high-end editorial fashion photography, natural skin texture, minimal retouching, realistic material texture.
Do not include any text, letters, numbers, logos, watermarks, signage or UI elements.
```

### A-P6 · Carrossel 4:5 — capa (A)

```text
A portrait 4:5 {FINISH_SHORT} image for the cover slide of a social carousel.
{SUBJECT_SENTENCE from the series bible, word for word}
It is set on the crest of a rounded grassy hill that fills the lower 35% of the frame.
Camera: {CAMERA from this slide's storyboard row}.
Light: {LIGHT from the series bible}.
Palette: deep saturated cerulean sky graduating to pale blue near the horizon, lush natural green grass, crisp white clouds{ACCENT_CLAUSE}; no other strong colors.
Composition: keep the top 9% and bottom 10% visually calm for small interface text. Reserve 12% to 40% of the height as clean deep blue sky for a large headline. Place the subject centered between 38% and 82% of the height, its top rising slightly into the headline zone with a crisp silhouette.
Finish: {FINISH from the series bible}.
Do not include any text, letters, numbers, logos, watermarks, signage, UI elements, borders or frames.
```

### A-P7 · Carrossel 4:5 — slide de conteúdo (B/H)

```text
A portrait 4:5 image for an inner slide of the same social carousel. Keep the same light, color palette, materials and finish as the reference image; build a new composition, camera and scale.
{SECONDARY_SUBJECT, e.g. "a small group of friends seen from behind, running along the ridge line"} appears small in the frame, between 62% and 80% of the height.
Camera: {CAMERA from this slide's storyboard row}.
Composition: keep the top 9% and bottom 10% calm. Leave 12% to 58% of the height as wide open deep blue sky with no clouds, reserved for several lines of text.
Do not include any text, letters, numbers, logos, watermarks, signage, UI elements, borders or frames.
```

### A-P8 · Carrossel 4:5 — fechamento/CTA (C)

```text
A portrait 4:5 image for the closing slide of the same social carousel. Keep the same light, color palette, materials and finish as the reference image; build a new composition, camera and scale.
Worm's-eye view looking straight up at a clear deep blue sky, framed along the edges by sunlit {FOLIAGE, e.g. "tree canopies with bright green leaves"}.
The foliage forms an irregular frame and leaves a large clean area of sky in the center, about 55% of the frame, with no leaves, sun flare or clouds inside it, reserved for a call to action.
Do not include any text, letters, numbers, logos, watermarks, signage, UI elements, borders or frames.
```

### A-P9 · Panorama 21:9 para carrossel de 3 slides ([formatos-e-composicao.md §7.3](formatos-e-composicao.md))

```text
A very wide 21:9 hyperreal panorama that will be cut into three equal vertical 4:5 slides.
A continuous landscape of rolling grassy hills under a deep saturated cerulean sky; the horizon runs perfectly level and continuous across the full width at about 70% of the frame height.
Place exactly one point of interest centered in each third of the width: in the left third {SUBJECT_1}; in the middle third {SUBJECT_2}; in the right third {SUBJECT_3}. Keep all three small, between 50% and 80% of the frame height.
Keep the vertical lines at 33.3% and 66.7% of the width free of any object, so nothing is split between slides.
In each third, keep 12% to 40% of the height as clean deep blue sky with no clouds, reserved for a headline.
Light: {LIGHT from the series bible}. Finish: {FINISH from the series bible}.
Do not include any text, letters, numbers, logos, watermarks, signage, UI elements, borders or frames.
```

### A-P10 · Story/hero mobile 9:16 — Janela de céu (C), texto central

```text
A vertical 9:16 photographic image for a mobile hero.
Worm's-eye view looking straight up through large sunlit banana leaves that frame the top-left, top-right, bottom-left and bottom-right corners.
The leaves leave an irregular diamond-shaped opening of smooth pale-to-medium blue sky in the center, spanning about 30% to 70% of the height and 15% to 85% of the width, with no leaves, clouds or sun flare inside it, reserved for centered text.
Light: bright midday sun shining through the leaves, translucent green highlights, slightly browned leaf edges for realism.
Finish: shot on 35mm color film, fine natural grain.
Do not include any text, letters, numbers, logos, watermarks, signage, UI elements, borders or frames.
```
