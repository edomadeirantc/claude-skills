# Caso real — telemedicina para ele e para ela

Registro do trabalho que gerou as peças aprovadas G01 e G02. Os arquivos
saíram do acervo em 29/10/2026; ficam o processo e os prompts aprovados, como
modelo de processo e ponto de partida para novas peças da marca. Os `--ref`
citados abaixo são do histórico do caso e não existem mais na skill.

## Brief

- **Marca:** marca de telemedicina (anonimizada nesta versão pública); cor de marca não informada (prompts usaram `{BRAND_ACCENT}`).
- **Público:** homem e mulher; as peças devem falar com os dois ao mesmo tempo.
- **Entregas:** hero mobile 9:16, hero desktop 16:9, carrossel 4:5.
- **Nível:** editorial, "fora da caixa", à altura das referências R e N.

## Decisões que funcionaram

1. **Primeira rodada genérica foi rejeitada** (pessoa sorrindo para o celular
   no gramado). O salto veio de ideias com **metáfora, escala e ponto de vista**
   (`familia-ceu-campo.md §2` e princípios em `../SKILL.md`). O conceito aprovado: o casal visto de cima, olhando
   para a lente, "como se a câmera fosse o celular".
2. **Família B** (N12) foi aprovada de primeira pelo cliente: perfis frente a
   frente, olhos fechados, tags de vidro.
3. **Botão de contorno branco** em todas as peças; o cliente rejeitou fundo
   sólido e qualquer desfoque em volta.
4. **Título sem moldura**, solto sobre o céu ou sobre o vidro.
5. **Produção web:** o cliente preferiu a **imagem dominando a hero inteira** e
   o texto + botão numa seção logo abaixo (`modelos-e-producao.md §11.1`).

## Copy aprovada

| Peça | Título | Subtítulo | Botão | Tags |
|---|---|---|---|---|
| G01 | *Saúde a dois,* / **sem sala de espera.** | Consultas por vídeo para ele e para ela, de onde vocês estiverem. | AGENDAR CONSULTA → | — |
| G02 | Escutar *também* é cuidar. | — | AGENDAR CONSULTA → | Ansiedade · Estresse · Sono |

Banco de alternativas avaliadas:
- *Para ele, para ela,* / **um médico a um toque.**
- *Cuidar de vocês* / **ficou mais simples.**
- Sem sair de casa. *Literalmente.*
- A fila ficou para trás.
- O cuidado cabe na sua mão.
- Seu corpo fala. *A gente* escuta.

Regras de copy da marca: sem promessa clínica, sem citar receita, prazo ou
especialidade não confirmados; títulos de 3–7 palavras; uma palavra em itálico.

---

## G01 — Casal na grama (cadeia de edições)

1. **Geração** (mobile 9:16): mulher deitada na grama, vista de cima, olhando
   para a lente; título "Saúde feminina, no seu tempo." sobre bloco verde.
2. **Edição 1:** adicionar o homem + vidro + remover textos do topo →
   o modelo fez um **card** de vidro (rejeitado).
3. **Edição 2:** vidro em **degradê progressivo**, copy para os dois, botão →
   vidro aprovado, mas o **homem sumiu** e o botão saiu sólido.
4. **Edição 3:** duas referências (base nova + versão com o homem), camisa dele
   grafite, botão de contorno → casal correto; restou véu verde no botão.
5. **Edição 4:** copy final + remover véu → **aprovado**.
6. **Realismo/upscale 4K:** `edicao-iterativa.md §E.5`.

Prompt da edição 3 (duas referências), base do processo:

```text
You are given two images.
IMAGE 1 is the base image to edit. IMAGE 2 is a reference used only to take the man.
The result must remain a single full-bleed vertical 9:16 photograph with typography, shot from directly above.

PRESERVE FROM IMAGE 1 EXACTLY
- The progressive frosted-glass gradient at the top: strong soft frost at the very top, fading smoothly to fully sharp, with no edges, boxes or lines.
- The typography, unchanged in wording, accents, fonts, sizes, color and position.
- The woman: unchanged: facial features, expression, gaze into the lens, skin tone, dark wavy hair and olive linen top.
- The real grass texture, soft natural light and muted natural color grade.

ADD THE MAN FROM IMAGE 2
- Add the man shown in IMAGE 2, keeping his facial features, short dark hair, trimmed beard, skin tone and calm gentle expression exactly as in IMAGE 2.
- He lies on his back in the grass on the left, shoulder to shoulder with the woman, who moves to the right. Both heads are at the same height, tilted very slightly toward each other, both looking straight into the lens.
- Change his shirt to a plain deep charcoal linen shirt with no logos.
- Pull the view back slightly so both fit naturally: the pair is centered horizontally, the tops of their heads at about 44% of the image height, their faces between about 48% and 62%, their shoulders and chests extending to the bottom edge. Both heads stay fully below the frosted gradient.
- Match light, shadows, sharpness, skin texture and grain on both people.

BUTTON
- At about 91% of the image height, centered: a thin white outlined pill button with a transparent interior, and the text "AGENDAR CONSULTA →" in small white uppercase sans-serif.
- No fill, no white background, no blur, no green tint, no glow, no shadow, no halo and no vignette.

BOTTOM OF THE IMAGE
- The lower half is a clean, sharp, natural photograph all the way to the bottom edge.

DO NOT
- Do not add "{MARCA}", "{ANO}" or any other text, logos, watermarks, icons or UI elements.
- Do not add cards, panels, boxes, borders or frames.
- Do not change the woman's face or the man's face from IMAGE 2.
```

Prompt da edição 4 (aprovada):

```text
Edit the provided image. Change only the text and the area around the button. Keep everything else identical: both people, their faces, expressions, hair and clothing, the grass, the frosted-glass gradient at the top, the light, the colors and the composition.

TEXT
Replace the existing headline and subline with exactly this text (correct Brazilian Portuguese accents, no other text):
- Line 1: "Saúde a dois," in the same elegant italic serif, white, same size and position as the current first line.
- Line 2: "sem sala de espera." in the same bold sans-serif, white, same size and position as the current second line.
- Subline: "Consultas por vídeo para ele e para ela, de onde vocês estiverem." in the same small white sans-serif, centered on two lines, same position as the current subline.

BUTTON AREA
- Remove the soft dark green haze, blur, tint and vignette over the lower part of the image, around and behind the "AGENDAR CONSULTA →" button.
- Restore the sharp, natural photograph there, with the same brightness, contrast and true colors as the faces.
- Keep the button exactly as it is: a thin white outlined pill with a transparent interior. Only the sharp photograph is visible inside and around it.
- No darkening, gradient or vignette at the bottom edge or in the corners.

DO NOT
- Do not add any other text, logos, watermarks, icons or UI elements.
- Do not add cards, panels, boxes, borders or frames.
- Do not alter the faces or the frosted gradient at the top.
```

---

## G02 — Perfis frente a frente (Família B)

1. **Geração** (template N12): perfis, caixa pontilhada no título, 3 tags,
   constelação, rodapé com marca → aprovado como estilo.
2. **Edição:** remover moldura do título, linhas verticais e rodapé; botão de
   contorno copiado de G01 (IMAGE 2) → **aprovado** (G02).
3. **Conversão desktop 16:9** com `--ref` de G02 → **aprovada**.

Prompt de geração **consolidado**: já incorpora as correções da edição (sem moldura, sem linhas extras, botão de contorno), para chegar ao resultado de G02 numa geração só. É 4:5; para 9:16 troque a primeira linha e use as faixas de `familia-saude-vidro.md §B.4`.

```text
A vertical 4:5 health-brand social poster: a real, sunlit editorial photograph with a refined, minimal interface overlay.

PHOTO
- A close-up of two side profiles facing each other against the sky: a man on the left with a short beard, and a woman on the right with dark curly hair loosely tied. Their foreheads almost touch, eyes closed, calm, serene expressions.
- The faces sit between 32% and 68% of the height; only the heads and necks are visible, cropped at the left and right edges.
- Background: a clear, flat, muted dusty steel-blue sky, #546D8C at the top easing to #667E9F at the bottom, no clouds.
- Warm natural late-afternoon sun from the upper left, a soft golden rim light on their profiles.
- Real skin with pores and fine facial hair; individual hair strands.
- 85mm lens, subtle film grain, natural muted color grade.

OVERLAY (thin, precise, minimal)
- Headline centered at 9% to 25% of the height: "Escutar também é cuidar." in a refined light serif, white, with only the word "também" in italic serif. No box or outline around it.
- Three frosted-glass pill tags with soft backdrop blur and a thin semi-transparent white edge, picking up the warm skin tones where they overlap. White sans-serif labels: "Ansiedade" at the upper left (~36% of the height), "Estresse" at the right (~50%), "Sono" at the lower left (~64%).
- Next to each tag, a small solid white dot. Thin 1-pixel white lines connect the three dots to each other. No other lines.

BUTTON
- Centered at about 89% of the height, about 38% of the width: a pill drawn only with a thin, crisp, solid white outline, fully transparent inside, containing "AGENDAR CONSULTA →" in a clean white uppercase sans-serif with slight letter spacing and a thin right arrow. No fill, blur, tint, glow or shadow.
- Nothing else at the bottom: no box, no frame, no logo, no other text.

TEXT RULES
Render all text exactly as written, with correct Brazilian Portuguese accents. No other text anywhere.

AVOID
Saturated blue, clouds, HDR, plastic skin, distorted faces, boxes or frames, vertical lines, logos, watermarks.
```

Prompt de conversão desktop (aprovado):

```text
Convert the provided image into a wide 16:9 website hero. Recompose it natively for a wide frame; do not crop, stretch or squeeze the reference.

PRESERVE FROM THE REFERENCE EXACTLY
- Both people: the same people, unchanged: facial features, profiles, closed eyes, serene expressions, skin texture, hair, light and colors. Do not retouch, beautify or change them.
- The muted dusty steel-blue sky (#546D8C at the top easing to #667E9F at the bottom), the warm late-afternoon sunlight from the upper left, the soft golden rim light, the subtle film grain and the natural color grade.
- The typography style, the frosted-glass tags and the outlined button style.

COMPOSITION
- The two side profiles face each other, centered in the frame, with their foreheads touching exactly at the horizontal center: the man on the left facing right, the woman on the right facing left.
- Their heads are fully visible: the back of his head at about 12% of the width, her curly hair bun at about 88% of the width. Open sky on both outer sides.
- Their faces fill the vertical space between about 24% and 84% of the height. Below their chins, their necks diverge, leaving a V-shaped area of open sky at the bottom center.
- Keep the top 9% of the frame as plain sky for the website navigation bar.

TEXT AND OVERLAY
- Headline on ONE line, centered, at about 12% to 19% of the height: "Escutar também é cuidar." in the same refined light serif, white, with only "também" in italic serif. No outline, box or frame around it.
- Three frosted-glass pill tags: "Ansiedade" over the man's hair near his temple (~30% of the width, ~36% of the height); "Estresse" over the woman's cheek (~72%, ~54%); "Sono" below the man's chin (~34%, ~76%).
- Next to each tag, a small solid white dot; thin 1-pixel white lines connect the three dots to each other. No other lines.
- Button at the bottom center, in the open sky between their necks, at about 92% of the height, about 20% of the image width: a thin white outlined pill, fully transparent inside, with "AGENDAR CONSULTA →". No fill, blur, tint, glow or shadow.

TEXT RULES
Render all text exactly as written, with correct Brazilian Portuguese accents. No other text: no logo, no wordmark, no navigation, no supporting text.

AVOID
Changing the faces, boxes or frames around the text, vertical lines, extra lines, saturated blue, clouds, HDR, plastic skin, logos, watermarks.
```

---

## Carrosséis Instagram 4:5

| Versão | Abordagem | Resultado |
|---|---|---|
| C1 | Família B inteira: mesmo casal, mesmo céu aço; slides variando gesto (perfis, mãos, celular, ombros, mãos pequenas) | **Preferido**: "seguiu um sentido" |
| C2 | Um mundo por slide (cadeira no morro, relógio gigante, campo aéreo, card de vidro, guarda-chuvas, folhas) | **Rejeitado**: bagunçado e repetiu as referências |
| C3 | Família B, mesmo universo, roteiro narrativo, gestos novos (não repete G02 nem N12), paginação "0N / 06 · ARRASTE →" | Proposto após a lição de C2 |
| C4 | Tema sono. Universo novo: cama de linho sobre mar de nuvens ao amanhecer, casal novo, um coral (fronha). Texto branco só no céu alto (`#4A6F96`, 5,24:1); rodapé e botão azul-escuro sobre nuvem/linho | Proposto |

Lição: o cliente quer **variedade dentro de um universo**, não variedade de
universos. Regras gravadas em `formatos-e-composicao.md §7.4` e `referencias.md §0`.

## Pendências da marca

- Cor de marca e logo oficiais (substituir `{BRAND_ACCENT}` e aplicar logo na finalização).
- Lista real de especialidades/atendimentos para as tags.
- Revisão jurídica das peças finais (publicidade médica — CFM).
