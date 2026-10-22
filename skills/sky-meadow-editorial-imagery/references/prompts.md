# Arquitetura de prompt e biblioteca

## 6. Arquitetura do prompt

### 6.1 Ordem dos slots

Para Gemini/Nano Banana, escreva **frases descritivas**, não listas de
palavras-chave. Siga esta ordem:

| # | Slot | Pergunta que responde |
|---|---|---|
| 1 | FORMATO E PROPÓSITO | Que peça é e para quê |
| 2 | SUJEITO | O que é o monumento, material, pose |
| 3 | CENÁRIO | Colina, campo, estúdio, janela de céu |
| 4 | CÂMERA | Altura, ângulo, lente, profundidade de campo |
| 5 | LUZ | Hora, direção, qualidade |
| 6 | PALETA | Céu, grama, acento único |
| 7 | COMPOSIÇÃO E ESPAÇO NEGATIVO | Zonas da [formatos-e-composicao.md §5](formatos-e-composicao.md) em porcentagem |
| 8 | CAMADAS | Se o sujeito invade a zona do título |
| 9 | ACABAMENTO | CGI limpo ou filme 35 mm |
| 10 | EXCLUSÕES | Sem texto, logos, artefatos |

### 6.2 Template mestre

```text
A {FORMAT} {FINISH_SHORT} image for a website {USE}.
{SUBJECT_SENTENCE}
It is set {SETTING_SENTENCE}.
Camera: {CAMERA_SENTENCE}.
Light: {LIGHT_SENTENCE}.
Palette: deep saturated cerulean sky graduating to pale blue near the horizon, lush natural green grass, crisp white clouds{ACCENT_CLAUSE}; no other strong colors.
Composition: {SAFE_ZONE_SENTENCE}
{LAYER_SENTENCE}
Finish: {FINISH_SENTENCE}.
Do not include any text, letters, numbers, logos, watermarks, signage, UI elements, borders or frames.
```

### 6.3 Banco de frases por slot

**Câmera**
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
- Com texto atrás: `The top of the subject rises about 10% into the headline zone; its silhouette is crisp and sharply defined against a smooth sky, with no motion blur, so it can be cleanly cut out.`
- Sem texto atrás: `The subject stays fully below the headline zone with clear sky between them.`

### 6.4 Regras de escrita

- Um sujeito por frase; um monumento por imagem.
- Posições em **porcentagem ou terços**, nunca "à esquerda" sozinho.
- Diga o que deve estar **vazio** com tanta precisão quanto o que deve
  aparecer.
- Proporção vai no **parâmetro** do modelo, não só no texto.
- Não cite fotógrafos ou artistas vivos, celebridades, personagens ou marcas
  ([SKILL.md §13](../SKILL.md)). Descreva as qualidades visuais.
- Prompt em inglês; texto que for aparecer na imagem, entre aspas, no idioma
  final.

---

## 15. Prompts prontos

Substitua os campos `{...}`. Cada exemplo segue o template da §6.2.

> **Atenção:** estes prompts demonstram **estrutura** (zonas, camadas, luz,
> exclusões). Vários sujeitos aqui (P10 folhas de bananeira, P5 objeto
> gigante em estúdio, cadeira/símbolo no morro) são composições-assinatura
> das referências. Não os use como estão em peça de cliente: troque o
> sujeito e a cena por algo do universo da marca (`referencias.md §0`).

### P1 · Hero desktop 16:9 — Monumento (A), texto branco centralizado

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

### P2 · Hero mobile 9:16 — derivado do P1 (usar `--ref` do desktop aprovado)

```text
A vertical 9:16 hyperreal image for a mobile website hero.
Use the reference image only for the object, materials, light, palette and finish. Recompose the scene natively for a tall vertical frame; do not crop or stretch the reference.
The same object stands on the crest of the same rounded grassy hill, which now fills the lower 30% of the frame.
Camera: low, slightly below the crest, 28mm lens, looking up.
Composition: keep the top 8% as quiet sky margin; reserve 10% to 38% of the height as clean deep blue sky with no clouds for a headline. Center the object, occupying roughly 40% to 72% of the height and about 60% of the width. The bottom 18% is calm, evenly shaded grass with no bright flowers, reserved for a button.
The top of the object rises slightly into the headline zone, with a crisp silhouette and no motion blur.
Do not include any text, letters, numbers, logos, watermarks, signage, UI elements, borders or frames.
```

### P3 · Hero desktop 16:9 — Horizonte (B), texto escuro à esquerda

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

### P4 · Hero esporte 16:9 — Perspectiva forçada (D), título gigante atrás

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

### P5 · Hero mobile 9:16 — Objeto gigante em estúdio (E)

```text
A vertical 9:16 editorial fashion photograph for a mobile website hero.
A person in a relaxed cream outfit and sunglasses, no visible brand marks, leans casually with folded arms on top of an enormous {OBJECT, e.g. "felt tennis ball"}, which is several times larger than them and dominates the lower half of the frame.
It is set on a seamless warm amber (#E8940F) studio backdrop with no visible seam or floor edge.
Camera: eye level with the object's top, 50mm lens, full body visible.
Light: large soft studio key light from the front-left, subtle fill, soft contact shadow under the object.
Palette: warm amber backdrop, the object's natural color as the only accent, cream clothing; no other strong colors.
Composition: reserve the top 35% as clean, evenly lit backdrop for a headline. The person's head sits at about 40% of the height; the object spans 45% to 92%.
Finish: high-end editorial fashion photography, clean retouching, realistic material texture.
Do not include any text, letters, numbers, logos, watermarks, signage or UI elements.
```

### P6 · Carrossel 4:5 — capa (A)

```text
A portrait 4:5 hyperreal image for the cover slide of a social carousel.
{SUBJECT_SENTENCE from the series bible, word for word}
It is set on the crest of a rounded grassy hill that fills the lower 35% of the frame.
Camera: {CAMERA from the series bible}.
Light: {LIGHT from the series bible}.
Palette: deep saturated cerulean sky graduating to pale blue near the horizon, lush natural green grass, crisp white clouds{ACCENT_CLAUSE}; no other strong colors.
Composition: keep the top 9% and bottom 10% visually calm for small interface text. Reserve 12% to 40% of the height as clean deep blue sky for a large headline. Place the subject centered between 38% and 82% of the height, its top rising slightly into the headline zone with a crisp silhouette.
Finish: {FINISH from the series bible}.
Do not include any text, letters, numbers, logos, watermarks, signage, UI elements, borders or frames.
```

### P7 · Carrossel 4:5 — slide de conteúdo (B/H)

```text
A portrait 4:5 image for an inner slide of the same social carousel; match the reference image exactly in light, palette, grass, sky and finish.
{SECONDARY_SUBJECT, e.g. "a small group of friends seen from behind, running along the ridge line"} appears small in the frame, between 62% and 80% of the height.
Camera: {CAMERA from the series bible}, horizon at the same height as the reference.
Composition: keep the top 9% and bottom 10% calm. Leave 12% to 58% of the height as wide open deep blue sky with no clouds, reserved for several lines of text.
Do not include any text, letters, numbers, logos, watermarks, signage, UI elements, borders or frames.
```

### P8 · Carrossel 4:5 — fechamento/CTA (C)

```text
A portrait 4:5 image for the closing slide of the same social carousel; match the reference image in light, palette and finish.
Worm's-eye view looking straight up at a clear deep blue sky, framed along the edges by sunlit {FOLIAGE, e.g. "tree canopies with bright green leaves"}.
The foliage forms an irregular frame and leaves a large clean area of sky in the center, about 55% of the frame, with no leaves, sun flare or clouds inside it, reserved for a call to action.
Do not include any text, letters, numbers, logos, watermarks, signage, UI elements, borders or frames.
```

### P9 · Panorama 21:9 para carrossel de 3 slides ([formatos-e-composicao.md §7.3](formatos-e-composicao.md))

```text
A very wide 21:9 hyperreal panorama that will be cut into three equal vertical 4:5 slides.
A continuous landscape of rolling grassy hills under a deep saturated cerulean sky; the horizon runs perfectly level and continuous across the full width at about 70% of the frame height.
Place exactly one point of interest centered in each third of the width: in the left third {SUBJECT_1}; in the middle third {SUBJECT_2}; in the right third {SUBJECT_3}. Keep all three small, between 50% and 80% of the frame height.
Keep the vertical lines at 33.3% and 66.7% of the width free of any object, so nothing is split between slides.
In each third, keep 12% to 40% of the height as clean deep blue sky with no clouds, reserved for a headline.
Light: {LIGHT from the series bible}. Finish: {FINISH from the series bible}.
Do not include any text, letters, numbers, logos, watermarks, signage, UI elements, borders or frames.
```

### P10 · Story/hero mobile 9:16 — Janela de céu (C), texto central

```text
A vertical 9:16 photographic image for a mobile hero.
Worm's-eye view looking straight up through large sunlit banana leaves that frame the top-left, top-right, bottom-left and bottom-right corners.
The leaves leave an irregular diamond-shaped opening of smooth pale-to-medium blue sky in the center, spanning about 30% to 70% of the height and 15% to 85% of the width, with no leaves, clouds or sun flare inside it, reserved for centered text.
Light: bright midday sun shining through the leaves, translucent green highlights, slightly browned leaf edges for realism.
Finish: shot on 35mm color film, fine natural grain.
Do not include any text, letters, numbers, logos, watermarks, signage, UI elements, borders or frames.
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
