# Groomy · carrossel v4 · realismo documental, padrão mediano bem cuidado, contador em camada

## Fluxo
1. **Capa primeiro (slide 01), sem referência.** Antes de aprovar, passe no portão da capa abaixo. Se reprovar, gere a capa de novo: os outros slides herdam o que ela tiver de genérico.
2. Slides 02, 03, 04, 05 e 07: `--ref capa_aprovada`. Slides 06 e 08: sem referência (não têm pessoa).
3. Todos saem em 3:4 compostos para o corte central em 1080×1350.
4. **Contador fora da IA:** os prompts reservam a faixa de 85–93% da altura vazia. Depois do corte para 1080×1350, aplique por cima `kit-0N` gerado por `scripts/kit_overlay.mjs --total 8 --accent "#C8F028"` (pontos, numeração e "ARRASTE →" exatos).
5. Se você tiver uma foto real de uma barbearia de verdade (de um cliente, com autorização), anexe como imagem 2 na capa com: "Reference image 2 is a real barbershop: use it only for the look of the place, materials and light."

## Portão da capa (reprove se 2 ou mais falharem)
- [ ] Parece foto de um lugar real ou de banco de imagem? Banco de imagem reprova.
- [ ] O barbeiro tem traços próprios (cicatriz na sobrancelha, barba falhada e grisalha, entradas, barriga)? Rosto de modelo reprova.
- [ ] O lugar tem vida e é bem cuidado, de padrão mediano: gente, objetos em uso, potes diferentes, cabelo perto da cadeira? Showroom vazio reprova; lugar pobre, sujo ou precário também reprova.
- [ ] A luz é a do lugar (spots quentes + vitrine), sem lâmpada pendente dramática e sem tubo fluorescente cru?
- [ ] Nada de pele lisa, brilho de propaganda ou cor "cinematográfica".

| # | Papel | Layout | Vozes | Ref |
|---|---|---|---|---|
| 01 | CAPA | L1 · Manchete na base | display + utilitária | nenhuma (capa) |
| 02 | STAKE | L2 · Pilha tipográfica | display + contraponto + utilitária | capa aprovada |
| 03 | DOR | L3 · Legenda de cinema | utilitária + display | capa aprovada |
| 04 | VIRADA | L8 · Coluna lateral | display + contraponto + utilitária | capa aprovada |
| 05 | COMO | L11 · Fileira de botões | display + interface | capa aprovada |
| 06 | RESUMO | L7 · Número gigante | display + utilitária | nenhuma |
| 07 | OBJEÇÃO | L4 · Balões de mensagem | interface + utilitária | capa aprovada |
| 08 | CTA | L12 · Fechamento liso | display + contraponto + utilitária | nenhuma |

## Slide 01 · CAPA · L1 · Manchete na base

```text
A portrait 3:4 documentary photograph for the cover slide (1 of 8) of an Instagram carousel for a barbershop management app.
Evening, 8 pm, after closing: the glass storefront shows the dark street outside and half of the lights are already off. The barber sits sideways in his own barber chair, elbow on the armrest, rubbing his eyes with one hand; across his knee and down to the floor runs a long strip of white paper from the old adding machine on the counter, about two meters, curling into a few loose loops among the hair clippings on the floor. The paper has only faint printed columns, too small and blurred to read.
Camera: 35mm f/2 at eye level, a little to the side, focus on his face and hands.
Composition: his head at about 24% and his hands at about 36% of the height; the paper reaches the floor at about 70%. From 52% downward the photograph itself darkens smoothly into near-black (#0A0A0A).

SERIES BIBLE (same place and same barber in every slide; layout changes per slide)
- Place: a well-kept, mid-market neighborhood barbershop in a Brazilian city, about 5 by 8 meters, successful and organized, the kind of place a regular customer trusts. Warm grey matte walls with one wall of exposed brick, wood-look porcelain floor, a glass storefront facing the street; warm LED spotlights on a ceiling track plus daylight from the storefront; two modern black hydraulic barber chairs in good condition; a long mirror with a simple wooden frame; a wooden counter with neatly arranged pomade jars of different brands, spray bottles, clippers on a charging base with their cords, a hand towel and a cup of coffee; a small waiting area with a fabric bench, a plant and a wall TV. During work there are a few hair clippings around the chair. Framed prints, a price board and a calendar on the wall stay soft, out of focus and unreadable.
- The barber (same man in every slide): Rafael, 38, Brazilian, mixed-race, sturdy build with a small belly, short buzz cut with a receding hairline, a patchy salt-and-pepper beard trimmed a few days ago, a small healed scar through the left eyebrow, a faded black tattoo of a date on the right forearm, slightly crooked lower teeth when he smiles. He wears a clean plain black polo shirt with no logo, dark jeans, clean white sneakers and a simple black watch. Not a model: a real, likable professional who owns his shop.
- Other people, when present: ordinary customers of varied ages, faces not the focus, partly turned away.
- Light: the real light of the place, warm LED spotlights mixed with daylight from the storefront, pleasant and natural, one dominant direction; time of day as stated in each slide. No bare fluorescent tubes, no Edison bulbs, no moody concept lighting.
- Photography: documentary reportage photograph taken during a normal working day for a Brazilian news magazine; full-frame camera, 35mm f/2 lens at eye level, available light, visible ISO grain, slightly imperfect framing, true-to-life color with mixed white balance, no color-grading look.
- Brand treatment lives only in the design layer: lime (#C8F028) never appears on objects in the scene; it appears only in the typography and interface listed for each slide, at most one line or word.
- Type voices: DISPLAY = heavy geometric sans-serif, uppercase, warm white (#F2F2F0). COUNTERPOINT = elegant high-contrast serif in italic, lowercase. UTILITY = clean monospace. Interface labels = neutral sans. Use only the voices the slide names.
- Frame: portrait 3:4, composed to be center-cropped later to 4:5: the top 4% and bottom 4% contain only continuous background.
- Top handle line, baseline at 8.8% of the height: "@groomyoficial" centered, lowercase exactly as written, neutral sans, white at 85%, no verification badge. Only the side labels this slide lists; no other pills, tags or labels at the top.
- Reserved band: from 85% to 93% of the height keep only calm dark background, with no text, dots, squares, numbers or shapes (a page counter is added later as an overlay).

Text, rendered exactly:
- Top line: "@groomyoficial" centered; on the right, a small solid lime (#C8F028) pill ending at 92% of the width with dark uppercase text "BARBEARIAS", same baseline.
- Headline, DISPLAY, centered, 53% to 74% of the height, three lines: "PARE DE FECHAR O CAIXA DE CABEÇA." with "CAIXA DE CABEÇA." in lime.
- Subline at 76–78%, UTILITY, small, white, preceded by a thin lime arrow: "→ AGENDA, CAIXA E CLIENTES EM UM SÓ LUGAR".
- At 80–84%, a solid lime pill with dark uppercase neutral sans "ARRASTE PARA O LADO" and, beside it, a small solid lime circle with a dark right arrow.

Render only the exact text listed above; no additional lettering, dates, credits, logos or watermarks.

REALISM (highest priority)
- It must pass as an unretouched photo of a real place and a real person, not a stock photo, not an advertisement, not a render.
- Skin of a 38-year-old: visible pores, uneven tone, some redness, oily forehead, fine lines around the eyes, the eyebrow scar, individual beard hairs of uneven length with grey hairs and patchy areas.
- Hands: work-worn, small cuts and dry knuckles, exactly five fingers per hand.
- Materials: leather seats with natural creases, wood grain with light marks of daily use, cotton with natural wrinkles, a few hair clippings near the chair, fingerprints on the mirror edge.
- Forbidden: model-like or symmetrical face, perfectly groomed beard, glossy or airbrushed skin, studio lighting, cinematic or moody grading, teal-and-orange, an empty or showroom-clean set, Edison bulbs, CGI look, extra fingers, readable invented text on posters or objects, logos or brand marks, and any run-down, cheap, dirty or precarious look (cracked tiles, patches, stains, bare fluorescent tubes, exposed wiring, broken furniture).
```

## Slide 02 · STAKE · L2 · Pilha tipográfica

```text
A portrait 3:4 documentary photograph for slide 2 of 8 of the same carousel.
Midday, busy: close-up at the counter. A small generic card terminal with no logo prints a receipt; the barber's hand with the simple black watch tears it off. In the soft background a customer waits on the bench looking at his phone. The whole photograph is darkened by about 45% so it reads as texture behind the type.
Camera: 50mm f/2, slightly above counter height, focus on the hand and the receipt.

Reference image 1 is the approved cover: keep the same barbershop, the same barber's general look and clothing, and the same colors. Do not copy its layout, text positions, font sizes, headline treatment or composition: this slide uses the "Pilha tipográfica" layout described below.

SERIES BIBLE (same place and same barber in every slide; layout changes per slide)
- Place: a well-kept, mid-market neighborhood barbershop in a Brazilian city, about 5 by 8 meters, successful and organized, the kind of place a regular customer trusts. Warm grey matte walls with one wall of exposed brick, wood-look porcelain floor, a glass storefront facing the street; warm LED spotlights on a ceiling track plus daylight from the storefront; two modern black hydraulic barber chairs in good condition; a long mirror with a simple wooden frame; a wooden counter with neatly arranged pomade jars of different brands, spray bottles, clippers on a charging base with their cords, a hand towel and a cup of coffee; a small waiting area with a fabric bench, a plant and a wall TV. During work there are a few hair clippings around the chair. Framed prints, a price board and a calendar on the wall stay soft, out of focus and unreadable.
- The barber (same man in every slide): Rafael, 38, Brazilian, mixed-race, sturdy build with a small belly, short buzz cut with a receding hairline, a patchy salt-and-pepper beard trimmed a few days ago, a small healed scar through the left eyebrow, a faded black tattoo of a date on the right forearm, slightly crooked lower teeth when he smiles. He wears a clean plain black polo shirt with no logo, dark jeans, clean white sneakers and a simple black watch. Not a model: a real, likable professional who owns his shop.
- Other people, when present: ordinary customers of varied ages, faces not the focus, partly turned away.
- Light: the real light of the place, warm LED spotlights mixed with daylight from the storefront, pleasant and natural, one dominant direction; time of day as stated in each slide. No bare fluorescent tubes, no Edison bulbs, no moody concept lighting.
- Photography: documentary reportage photograph taken during a normal working day for a Brazilian news magazine; full-frame camera, 35mm f/2 lens at eye level, available light, visible ISO grain, slightly imperfect framing, true-to-life color with mixed white balance, no color-grading look.
- Brand treatment lives only in the design layer: lime (#C8F028) never appears on objects in the scene; it appears only in the typography and interface listed for each slide, at most one line or word.
- Type voices: DISPLAY = heavy geometric sans-serif, uppercase, warm white (#F2F2F0). COUNTERPOINT = elegant high-contrast serif in italic, lowercase. UTILITY = clean monospace. Interface labels = neutral sans. Use only the voices the slide names.
- Frame: portrait 3:4, composed to be center-cropped later to 4:5: the top 4% and bottom 4% contain only continuous background.
- Top handle line, baseline at 8.8% of the height: "@groomyoficial" centered, lowercase exactly as written, neutral sans, white at 85%, no verification badge. Only the side labels this slide lists; no other pills, tags or labels at the top.
- Reserved band: from 85% to 93% of the height keep only calm dark background, with no text, dots, squares, numbers or shapes (a page counter is added later as an overlay).

Text, rendered exactly:
- Top line: "@groomyoficial" centered; on the right, a small solid lime pill ending at 92% of the width with dark uppercase "BARBEARIAS".
- TYPOGRAPHIC STACK, left-aligned at 8% of the width, from 22% to 68% of the height:
  1) DISPLAY, white, two lines: "O QUE PASSOU NA MAQUININHA"
  2) COUNTERPOINT serif italic, very large, white: "não é"
  3) DISPLAY, lime: "O SEU LUCRO."
- UTILITY, small, white at 80%, left-aligned at 8%, at 73%: "Despesas, taxas e fiado também contam."

Render only the exact text listed above; no additional lettering, dates, credits, logos or watermarks.

REALISM (highest priority)
- It must pass as an unretouched photo of a real place and a real person, not a stock photo, not an advertisement, not a render.
- Skin of a 38-year-old: visible pores, uneven tone, some redness, oily forehead, fine lines around the eyes, the eyebrow scar, individual beard hairs of uneven length with grey hairs and patchy areas.
- Hands: work-worn, small cuts and dry knuckles, exactly five fingers per hand.
- Materials: leather seats with natural creases, wood grain with light marks of daily use, cotton with natural wrinkles, a few hair clippings near the chair, fingerprints on the mirror edge.
- Forbidden: model-like or symmetrical face, perfectly groomed beard, glossy or airbrushed skin, studio lighting, cinematic or moody grading, teal-and-orange, an empty or showroom-clean set, Edison bulbs, CGI look, extra fingers, readable invented text on posters or objects, logos or brand marks, and any run-down, cheap, dirty or precarious look (cracked tiles, patches, stains, bare fluorescent tubes, exposed wiring, broken furniture).
```

## Slide 03 · DOR · L3 · Legenda de cinema

```text
A portrait 3:4 documentary photograph in a widescreen letterbox format for slide 3 of 8 of the same carousel.
Solid black letterbox bars cover the top 16% and the bottom 30% of the frame; the scene lives only in the band between them.
Scene in the band, late afternoon: wide shot from inside the shop toward the door. A regular customer in his fifties, wearing a cap, walks out waving over his shoulder; the barber stands at the counter writing in a small spiral notebook with a pen, half-smiling but uneasy. Hair clippings on the floor, a broom against the wall. The notebook shows only illegible scribbles.
Camera: 35mm f/2, eye level, documentary.

Reference image 1 is the approved cover: keep the same barbershop, the same barber's general look and clothing, and the same colors. Do not copy its layout, text positions, font sizes, headline treatment or composition: this slide uses the "Legenda de cinema" layout described below.

SERIES BIBLE (same place and same barber in every slide; layout changes per slide)
- Place: a well-kept, mid-market neighborhood barbershop in a Brazilian city, about 5 by 8 meters, successful and organized, the kind of place a regular customer trusts. Warm grey matte walls with one wall of exposed brick, wood-look porcelain floor, a glass storefront facing the street; warm LED spotlights on a ceiling track plus daylight from the storefront; two modern black hydraulic barber chairs in good condition; a long mirror with a simple wooden frame; a wooden counter with neatly arranged pomade jars of different brands, spray bottles, clippers on a charging base with their cords, a hand towel and a cup of coffee; a small waiting area with a fabric bench, a plant and a wall TV. During work there are a few hair clippings around the chair. Framed prints, a price board and a calendar on the wall stay soft, out of focus and unreadable.
- The barber (same man in every slide): Rafael, 38, Brazilian, mixed-race, sturdy build with a small belly, short buzz cut with a receding hairline, a patchy salt-and-pepper beard trimmed a few days ago, a small healed scar through the left eyebrow, a faded black tattoo of a date on the right forearm, slightly crooked lower teeth when he smiles. He wears a clean plain black polo shirt with no logo, dark jeans, clean white sneakers and a simple black watch. Not a model: a real, likable professional who owns his shop.
- Other people, when present: ordinary customers of varied ages, faces not the focus, partly turned away.
- Light: the real light of the place, warm LED spotlights mixed with daylight from the storefront, pleasant and natural, one dominant direction; time of day as stated in each slide. No bare fluorescent tubes, no Edison bulbs, no moody concept lighting.
- Photography: documentary reportage photograph taken during a normal working day for a Brazilian news magazine; full-frame camera, 35mm f/2 lens at eye level, available light, visible ISO grain, slightly imperfect framing, true-to-life color with mixed white balance, no color-grading look.
- Brand treatment lives only in the design layer: lime (#C8F028) never appears on objects in the scene; it appears only in the typography and interface listed for each slide, at most one line or word.
- Type voices: DISPLAY = heavy geometric sans-serif, uppercase, warm white (#F2F2F0). COUNTERPOINT = elegant high-contrast serif in italic, lowercase. UTILITY = clean monospace. Interface labels = neutral sans. Use only the voices the slide names.
- Frame: portrait 3:4, composed to be center-cropped later to 4:5: the top 4% and bottom 4% contain only continuous background.
- Top handle line, baseline at 8.8% of the height: "@groomyoficial" centered, lowercase exactly as written, neutral sans, white at 85%, no verification badge. Only the side labels this slide lists; no other pills, tags or labels at the top.
- Reserved band: from 85% to 93% of the height keep only calm dark background, with no text, dots, squares, numbers or shapes (a page counter is added later as an overlay).

Text, rendered exactly:
- Top line inside the top black bar: "@groomyoficial" centered; on the left, "A DOR" small uppercase grey sans at 8% of the width, same baseline. Nothing on the right.
- Movie subtitle inside the bottom black bar, centered at 73–77%, UTILITY, white: "— Anota aí, semana que vem eu acerto."
- Centered at 80%, DISPLAY, white with the last two words in lime: "FIADO NO CADERNO É DINHEIRO ESQUECIDO."

Render only the exact text listed above; no additional lettering, dates, credits, logos or watermarks.

REALISM (highest priority)
- It must pass as an unretouched photo of a real place and a real person, not a stock photo, not an advertisement, not a render.
- Skin of a 38-year-old: visible pores, uneven tone, some redness, oily forehead, fine lines around the eyes, the eyebrow scar, individual beard hairs of uneven length with grey hairs and patchy areas.
- Hands: work-worn, small cuts and dry knuckles, exactly five fingers per hand.
- Materials: leather seats with natural creases, wood grain with light marks of daily use, cotton with natural wrinkles, a few hair clippings near the chair, fingerprints on the mirror edge.
- Forbidden: model-like or symmetrical face, perfectly groomed beard, glossy or airbrushed skin, studio lighting, cinematic or moody grading, teal-and-orange, an empty or showroom-clean set, Edison bulbs, CGI look, extra fingers, readable invented text on posters or objects, logos or brand marks, and any run-down, cheap, dirty or precarious look (cracked tiles, patches, stains, bare fluorescent tubes, exposed wiring, broken furniture).
```

## Slide 04 · VIRADA · L8 · Coluna lateral

```text
A portrait 3:4 documentary photograph for slide 4 of 8 of the same carousel.
Late afternoon: the barber stands in the right third of the frame behind the counter, looking at the smartphone in one hand (screen turned away) with a relieved crooked smile, while his other hand tosses the crumpled paper strip into a small trash bin under the counter. The left half of the frame is the softer, darker part of the shop with the waiting bench and the plant out of focus.
Camera: 35mm f/2, eye level, focus on his face.
Composition: the barber occupies 55% to 92% of the width; the left 50% of the width, from 15% to 70% of the height, stays calm for text.

Reference image 1 is the approved cover: keep the same barbershop, the same barber's general look and clothing, and the same colors. Do not copy its layout, text positions, font sizes, headline treatment or composition: this slide uses the "Coluna lateral" layout described below.

SERIES BIBLE (same place and same barber in every slide; layout changes per slide)
- Place: a well-kept, mid-market neighborhood barbershop in a Brazilian city, about 5 by 8 meters, successful and organized, the kind of place a regular customer trusts. Warm grey matte walls with one wall of exposed brick, wood-look porcelain floor, a glass storefront facing the street; warm LED spotlights on a ceiling track plus daylight from the storefront; two modern black hydraulic barber chairs in good condition; a long mirror with a simple wooden frame; a wooden counter with neatly arranged pomade jars of different brands, spray bottles, clippers on a charging base with their cords, a hand towel and a cup of coffee; a small waiting area with a fabric bench, a plant and a wall TV. During work there are a few hair clippings around the chair. Framed prints, a price board and a calendar on the wall stay soft, out of focus and unreadable.
- The barber (same man in every slide): Rafael, 38, Brazilian, mixed-race, sturdy build with a small belly, short buzz cut with a receding hairline, a patchy salt-and-pepper beard trimmed a few days ago, a small healed scar through the left eyebrow, a faded black tattoo of a date on the right forearm, slightly crooked lower teeth when he smiles. He wears a clean plain black polo shirt with no logo, dark jeans, clean white sneakers and a simple black watch. Not a model: a real, likable professional who owns his shop.
- Other people, when present: ordinary customers of varied ages, faces not the focus, partly turned away.
- Light: the real light of the place, warm LED spotlights mixed with daylight from the storefront, pleasant and natural, one dominant direction; time of day as stated in each slide. No bare fluorescent tubes, no Edison bulbs, no moody concept lighting.
- Photography: documentary reportage photograph taken during a normal working day for a Brazilian news magazine; full-frame camera, 35mm f/2 lens at eye level, available light, visible ISO grain, slightly imperfect framing, true-to-life color with mixed white balance, no color-grading look.
- Brand treatment lives only in the design layer: lime (#C8F028) never appears on objects in the scene; it appears only in the typography and interface listed for each slide, at most one line or word.
- Type voices: DISPLAY = heavy geometric sans-serif, uppercase, warm white (#F2F2F0). COUNTERPOINT = elegant high-contrast serif in italic, lowercase. UTILITY = clean monospace. Interface labels = neutral sans. Use only the voices the slide names.
- Frame: portrait 3:4, composed to be center-cropped later to 4:5: the top 4% and bottom 4% contain only continuous background.
- Top handle line, baseline at 8.8% of the height: "@groomyoficial" centered, lowercase exactly as written, neutral sans, white at 85%, no verification badge. Only the side labels this slide lists; no other pills, tags or labels at the top.
- Reserved band: from 85% to 93% of the height keep only calm dark background, with no text, dots, squares, numbers or shapes (a page counter is added later as an overlay).

Text, rendered exactly:
- Top line: "@groomyoficial" centered; on the left, "A VIRADA" small uppercase grey sans at 8% of the width. Nothing on the right.
- Left column, left-aligned at 8% of the width, from 22% to 66% of the height:
  DISPLAY, white, three short lines: "AGENDA," / "CAIXA E" / "CLIENTES"
  COUNTERPOINT serif italic, large, lime: "em uma tela só."
  UTILITY, small, white at 80%: "No balcão e na cadeira. Sem instalar nada."

Render only the exact text listed above; no additional lettering, dates, credits, logos or watermarks.

REALISM (highest priority)
- It must pass as an unretouched photo of a real place and a real person, not a stock photo, not an advertisement, not a render.
- Skin of a 38-year-old: visible pores, uneven tone, some redness, oily forehead, fine lines around the eyes, the eyebrow scar, individual beard hairs of uneven length with grey hairs and patchy areas.
- Hands: work-worn, small cuts and dry knuckles, exactly five fingers per hand.
- Materials: leather seats with natural creases, wood grain with light marks of daily use, cotton with natural wrinkles, a few hair clippings near the chair, fingerprints on the mirror edge.
- Forbidden: model-like or symmetrical face, perfectly groomed beard, glossy or airbrushed skin, studio lighting, cinematic or moody grading, teal-and-orange, an empty or showroom-clean set, Edison bulbs, CGI look, extra fingers, readable invented text on posters or objects, logos or brand marks, and any run-down, cheap, dirty or precarious look (cracked tiles, patches, stains, bare fluorescent tubes, exposed wiring, broken furniture).
```

## Slide 05 · COMO · L11 · Fileira de botões

```text
A portrait 3:4 documentary photograph for slide 5 of 8 of the same carousel.
Busy evening: the barber cuts the hair of a young customer seated in the barber chair, focused, clipper cord trailing; another customer waits in the background. The barber and the chair sit in the right half of the frame; the left edge darkens.
Camera: 50mm f/2, eye level, focus on the barber's hands and clipper; slight motion blur on the clipper.

Reference image 1 is the approved cover: keep the same barbershop, the same barber's general look and clothing, and the same colors. Do not copy its layout, text positions, font sizes, headline treatment or composition: this slide uses the "Fileira de botões" layout described below.

SERIES BIBLE (same place and same barber in every slide; layout changes per slide)
- Place: a well-kept, mid-market neighborhood barbershop in a Brazilian city, about 5 by 8 meters, successful and organized, the kind of place a regular customer trusts. Warm grey matte walls with one wall of exposed brick, wood-look porcelain floor, a glass storefront facing the street; warm LED spotlights on a ceiling track plus daylight from the storefront; two modern black hydraulic barber chairs in good condition; a long mirror with a simple wooden frame; a wooden counter with neatly arranged pomade jars of different brands, spray bottles, clippers on a charging base with their cords, a hand towel and a cup of coffee; a small waiting area with a fabric bench, a plant and a wall TV. During work there are a few hair clippings around the chair. Framed prints, a price board and a calendar on the wall stay soft, out of focus and unreadable.
- The barber (same man in every slide): Rafael, 38, Brazilian, mixed-race, sturdy build with a small belly, short buzz cut with a receding hairline, a patchy salt-and-pepper beard trimmed a few days ago, a small healed scar through the left eyebrow, a faded black tattoo of a date on the right forearm, slightly crooked lower teeth when he smiles. He wears a clean plain black polo shirt with no logo, dark jeans, clean white sneakers and a simple black watch. Not a model: a real, likable professional who owns his shop.
- Other people, when present: ordinary customers of varied ages, faces not the focus, partly turned away.
- Light: the real light of the place, warm LED spotlights mixed with daylight from the storefront, pleasant and natural, one dominant direction; time of day as stated in each slide. No bare fluorescent tubes, no Edison bulbs, no moody concept lighting.
- Photography: documentary reportage photograph taken during a normal working day for a Brazilian news magazine; full-frame camera, 35mm f/2 lens at eye level, available light, visible ISO grain, slightly imperfect framing, true-to-life color with mixed white balance, no color-grading look.
- Brand treatment lives only in the design layer: lime (#C8F028) never appears on objects in the scene; it appears only in the typography and interface listed for each slide, at most one line or word.
- Type voices: DISPLAY = heavy geometric sans-serif, uppercase, warm white (#F2F2F0). COUNTERPOINT = elegant high-contrast serif in italic, lowercase. UTILITY = clean monospace. Interface labels = neutral sans. Use only the voices the slide names.
- Frame: portrait 3:4, composed to be center-cropped later to 4:5: the top 4% and bottom 4% contain only continuous background.
- Top handle line, baseline at 8.8% of the height: "@groomyoficial" centered, lowercase exactly as written, neutral sans, white at 85%, no verification badge. Only the side labels this slide lists; no other pills, tags or labels at the top.
- Reserved band: from 85% to 93% of the height keep only calm dark background, with no text, dots, squares, numbers or shapes (a page counter is added later as an overlay).

Text, rendered exactly:
- Top line: "@groomyoficial" centered; on the left, "COMO FUNCIONA" small uppercase grey sans at 8% of the width. Nothing on the right.
- DISPLAY, white, left-aligned at 8%, from 18% to 30% of the height, two lines: "DO PRIMEIRO HORÁRIO" / "AO FECHAMENTO."
- A vertical stack of three outlined pills (thin white outline, transparent inside, neutral sans white text, each preceded by a small lime check mark), left-aligned at 8% of the width, at 40%, 48% and 56% of the height: "ABRA O DIA COM A AGENDA PRONTA" / "ATENDA COM A COMANDA NA CADEIRA" / "FECHE O CAIXA POR FORMA DE PAGAMENTO". No fill, glow or shadow.

Render only the exact text listed above; no additional lettering, dates, credits, logos or watermarks.

REALISM (highest priority)
- It must pass as an unretouched photo of a real place and a real person, not a stock photo, not an advertisement, not a render.
- Skin of a 38-year-old: visible pores, uneven tone, some redness, oily forehead, fine lines around the eyes, the eyebrow scar, individual beard hairs of uneven length with grey hairs and patchy areas.
- Hands: work-worn, small cuts and dry knuckles, exactly five fingers per hand.
- Materials: leather seats with natural creases, wood grain with light marks of daily use, cotton with natural wrinkles, a few hair clippings near the chair, fingerprints on the mirror edge.
- Forbidden: model-like or symmetrical face, perfectly groomed beard, glossy or airbrushed skin, studio lighting, cinematic or moody grading, teal-and-orange, an empty or showroom-clean set, Edison bulbs, CGI look, extra fingers, readable invented text on posters or objects, logos or brand marks, and any run-down, cheap, dirty or precarious look (cracked tiles, patches, stains, bare fluorescent tubes, exposed wiring, broken furniture).
```

## Slide 06 · RESUMO · L7 · Número gigante

```text
A portrait 3:4 documentary photograph for slide 6 of 8 of the same carousel; the quietest middle slide.
Top-down view of the barbershop counter at the end of the day, organized but in use: pomade jars of different brands, a comb, clippers with their cords, a hand towel, a coffee cup, a smartphone face down, a few hair clippings. The whole photograph is darkened by about 65% so it is only a texture.

SERIES BIBLE (same place and same barber in every slide; layout changes per slide)
- Place: a well-kept, mid-market neighborhood barbershop in a Brazilian city, about 5 by 8 meters, successful and organized, the kind of place a regular customer trusts. Warm grey matte walls with one wall of exposed brick, wood-look porcelain floor, a glass storefront facing the street; warm LED spotlights on a ceiling track plus daylight from the storefront; two modern black hydraulic barber chairs in good condition; a long mirror with a simple wooden frame; a wooden counter with neatly arranged pomade jars of different brands, spray bottles, clippers on a charging base with their cords, a hand towel and a cup of coffee; a small waiting area with a fabric bench, a plant and a wall TV. During work there are a few hair clippings around the chair. Framed prints, a price board and a calendar on the wall stay soft, out of focus and unreadable.
- The barber (same man in every slide): Rafael, 38, Brazilian, mixed-race, sturdy build with a small belly, short buzz cut with a receding hairline, a patchy salt-and-pepper beard trimmed a few days ago, a small healed scar through the left eyebrow, a faded black tattoo of a date on the right forearm, slightly crooked lower teeth when he smiles. He wears a clean plain black polo shirt with no logo, dark jeans, clean white sneakers and a simple black watch. Not a model: a real, likable professional who owns his shop.
- Other people, when present: ordinary customers of varied ages, faces not the focus, partly turned away.
- Light: the real light of the place, warm LED spotlights mixed with daylight from the storefront, pleasant and natural, one dominant direction; time of day as stated in each slide. No bare fluorescent tubes, no Edison bulbs, no moody concept lighting.
- Photography: documentary reportage photograph taken during a normal working day for a Brazilian news magazine; full-frame camera, 35mm f/2 lens at eye level, available light, visible ISO grain, slightly imperfect framing, true-to-life color with mixed white balance, no color-grading look.
- Brand treatment lives only in the design layer: lime (#C8F028) never appears on objects in the scene; it appears only in the typography and interface listed for each slide, at most one line or word.
- Type voices: DISPLAY = heavy geometric sans-serif, uppercase, warm white (#F2F2F0). COUNTERPOINT = elegant high-contrast serif in italic, lowercase. UTILITY = clean monospace. Interface labels = neutral sans. Use only the voices the slide names.
- Frame: portrait 3:4, composed to be center-cropped later to 4:5: the top 4% and bottom 4% contain only continuous background.
- Top handle line, baseline at 8.8% of the height: "@groomyoficial" centered, lowercase exactly as written, neutral sans, white at 85%, no verification badge. Only the side labels this slide lists; no other pills, tags or labels at the top.
- Reserved band: from 85% to 93% of the height keep only calm dark background, with no text, dots, squares, numbers or shapes (a page counter is added later as an overlay).

Text, rendered exactly:
- Top line: "@groomyoficial" centered. No side labels.
- A single giant number "7" in lime, DISPLAY, centered, its height spanning 18% to 50% of the frame.
- DISPLAY, white, centered at 56%: "MÓDULOS NO MESMO PLANO."
- UTILITY, small, white at 80%, centered, two lines at 63% and 67%: "FINANCEIRO · A RECEBER · AGENDA · RADAR" / "DESPESAS · LEMBRETES · EQUIPE"

Render only the exact text listed above; no additional lettering, dates, credits, logos or watermarks.

REALISM
- It must pass as an unretouched photo of a real, used workspace: documentary photograph, available light, visible grain, true-to-life color.
- Materials: wooden counter with visible grain and light marks of use, pomade jars of different brands with unreadable labels, cords, a few hair clippings.
- Forbidden: showroom-clean styling, perfect symmetry of objects, CGI look, moody grading, readable invented text, logos or brand marks, and any run-down, cheap or dirty look.
```

## Slide 07 · OBJEÇÃO · L4 · Balões de mensagem

```text
A portrait 3:4 documentary photograph for slide 7 of 8 of the same carousel.
Night, after closing: the barber sits on the waiting-area bench, legs stretched, looking at his phone with a calm half-smile; half of the lights are off. The phone screen faces away from the camera. He occupies the right 55% of the frame.
Camera: 35mm f/2, eye level, focus on his face.

Reference image 1 is the approved cover: keep the same barbershop, the same barber's general look and clothing, and the same colors. Do not copy its layout, text positions, font sizes, headline treatment or composition: this slide uses the "Balões de mensagem" layout described below.

SERIES BIBLE (same place and same barber in every slide; layout changes per slide)
- Place: a well-kept, mid-market neighborhood barbershop in a Brazilian city, about 5 by 8 meters, successful and organized, the kind of place a regular customer trusts. Warm grey matte walls with one wall of exposed brick, wood-look porcelain floor, a glass storefront facing the street; warm LED spotlights on a ceiling track plus daylight from the storefront; two modern black hydraulic barber chairs in good condition; a long mirror with a simple wooden frame; a wooden counter with neatly arranged pomade jars of different brands, spray bottles, clippers on a charging base with their cords, a hand towel and a cup of coffee; a small waiting area with a fabric bench, a plant and a wall TV. During work there are a few hair clippings around the chair. Framed prints, a price board and a calendar on the wall stay soft, out of focus and unreadable.
- The barber (same man in every slide): Rafael, 38, Brazilian, mixed-race, sturdy build with a small belly, short buzz cut with a receding hairline, a patchy salt-and-pepper beard trimmed a few days ago, a small healed scar through the left eyebrow, a faded black tattoo of a date on the right forearm, slightly crooked lower teeth when he smiles. He wears a clean plain black polo shirt with no logo, dark jeans, clean white sneakers and a simple black watch. Not a model: a real, likable professional who owns his shop.
- Other people, when present: ordinary customers of varied ages, faces not the focus, partly turned away.
- Light: the real light of the place, warm LED spotlights mixed with daylight from the storefront, pleasant and natural, one dominant direction; time of day as stated in each slide. No bare fluorescent tubes, no Edison bulbs, no moody concept lighting.
- Photography: documentary reportage photograph taken during a normal working day for a Brazilian news magazine; full-frame camera, 35mm f/2 lens at eye level, available light, visible ISO grain, slightly imperfect framing, true-to-life color with mixed white balance, no color-grading look.
- Brand treatment lives only in the design layer: lime (#C8F028) never appears on objects in the scene; it appears only in the typography and interface listed for each slide, at most one line or word.
- Type voices: DISPLAY = heavy geometric sans-serif, uppercase, warm white (#F2F2F0). COUNTERPOINT = elegant high-contrast serif in italic, lowercase. UTILITY = clean monospace. Interface labels = neutral sans. Use only the voices the slide names.
- Frame: portrait 3:4, composed to be center-cropped later to 4:5: the top 4% and bottom 4% contain only continuous background.
- Top handle line, baseline at 8.8% of the height: "@groomyoficial" centered, lowercase exactly as written, neutral sans, white at 85%, no verification badge. Only the side labels this slide lists; no other pills, tags or labels at the top.
- Reserved band: from 85% to 93% of the height keep only calm dark background, with no text, dots, squares, numbers or shapes (a page counter is added later as an overlay).

Text, rendered exactly:
- Top line: "@groomyoficial" centered; on the left, "DÚVIDAS" small uppercase grey sans at 8% of the width. Nothing on the right.
- Two generic chat bubbles over the left half of the frame (rounded rectangles, no app logo, no app interface, no avatars):
  first, dark grey (#2A2A2A) with white neutral sans text, left-aligned at 8%, at 30% of the height: "E se eu não gostar? Perco tudo?" with a tiny grey timestamp "21:42";
  second, lime (#C8F028) with dark text, slightly lower and indented, at 40%: "Sem fidelidade. Seus dados ficam." with a tiny dark timestamp "21:43".
- UTILITY, small, white at 80%, left-aligned at 8%, at 70%: "Se o mês vencer, nada é apagado. Pix ou cartão."

Render only the exact text listed above; no additional lettering, dates, credits, logos or watermarks.

REALISM (highest priority)
- It must pass as an unretouched photo of a real place and a real person, not a stock photo, not an advertisement, not a render.
- Skin of a 38-year-old: visible pores, uneven tone, some redness, oily forehead, fine lines around the eyes, the eyebrow scar, individual beard hairs of uneven length with grey hairs and patchy areas.
- Hands: work-worn, small cuts and dry knuckles, exactly five fingers per hand.
- Materials: leather seats with natural creases, wood grain with light marks of daily use, cotton with natural wrinkles, a few hair clippings near the chair, fingerprints on the mirror edge.
- Forbidden: model-like or symmetrical face, perfectly groomed beard, glossy or airbrushed skin, studio lighting, cinematic or moody grading, teal-and-orange, an empty or showroom-clean set, Edison bulbs, CGI look, extra fingers, readable invented text on posters or objects, logos or brand marks, and any run-down, cheap, dirty or precarious look (cracked tiles, patches, stains, bare fluorescent tubes, exposed wiring, broken furniture).
```

## Slide 08 · CTA · L12 · Fechamento liso

```text
A portrait 3:4 closing slide (8 of 8) of the same carousel, the calmest of the series.
Mostly plain near-black (#0A0A0A). In the lower right corner only, a small dim documentary detail of the empty black barber chair in good condition, lit by one remaining warm spotlight, fading into the dark.

SERIES BIBLE (same place and same barber in every slide; layout changes per slide)
- Place: a well-kept, mid-market neighborhood barbershop in a Brazilian city, about 5 by 8 meters, successful and organized, the kind of place a regular customer trusts. Warm grey matte walls with one wall of exposed brick, wood-look porcelain floor, a glass storefront facing the street; warm LED spotlights on a ceiling track plus daylight from the storefront; two modern black hydraulic barber chairs in good condition; a long mirror with a simple wooden frame; a wooden counter with neatly arranged pomade jars of different brands, spray bottles, clippers on a charging base with their cords, a hand towel and a cup of coffee; a small waiting area with a fabric bench, a plant and a wall TV. During work there are a few hair clippings around the chair. Framed prints, a price board and a calendar on the wall stay soft, out of focus and unreadable.
- The barber (same man in every slide): Rafael, 38, Brazilian, mixed-race, sturdy build with a small belly, short buzz cut with a receding hairline, a patchy salt-and-pepper beard trimmed a few days ago, a small healed scar through the left eyebrow, a faded black tattoo of a date on the right forearm, slightly crooked lower teeth when he smiles. He wears a clean plain black polo shirt with no logo, dark jeans, clean white sneakers and a simple black watch. Not a model: a real, likable professional who owns his shop.
- Other people, when present: ordinary customers of varied ages, faces not the focus, partly turned away.
- Light: the real light of the place, warm LED spotlights mixed with daylight from the storefront, pleasant and natural, one dominant direction; time of day as stated in each slide. No bare fluorescent tubes, no Edison bulbs, no moody concept lighting.
- Photography: documentary reportage photograph taken during a normal working day for a Brazilian news magazine; full-frame camera, 35mm f/2 lens at eye level, available light, visible ISO grain, slightly imperfect framing, true-to-life color with mixed white balance, no color-grading look.
- Brand treatment lives only in the design layer: lime (#C8F028) never appears on objects in the scene; it appears only in the typography and interface listed for each slide, at most one line or word.
- Type voices: DISPLAY = heavy geometric sans-serif, uppercase, warm white (#F2F2F0). COUNTERPOINT = elegant high-contrast serif in italic, lowercase. UTILITY = clean monospace. Interface labels = neutral sans. Use only the voices the slide names.
- Frame: portrait 3:4, composed to be center-cropped later to 4:5: the top 4% and bottom 4% contain only continuous background.
- Top handle line, baseline at 8.8% of the height: "@groomyoficial" centered, lowercase exactly as written, neutral sans, white at 85%, no verification badge. Only the side labels this slide lists; no other pills, tags or labels at the top.
- Reserved band: from 85% to 93% of the height keep only calm dark background, with no text, dots, squares, numbers or shapes (a page counter is added later as an overlay).

Text, rendered exactly:
- Top line: "@groomyoficial" centered; on the right, "TESTE 7 DIAS" small uppercase lime sans ending at 92% of the width.
- Left-aligned block at 8% of the width, centered around 45% of the height:
  DISPLAY, white, very large: "SEU DIA,"
  COUNTERPOINT serif italic, very large, lime: "mais leve."
  UTILITY, small, white at 80%: "7 dias para testar. Depois, R$ 79,90/mês, sem fidelidade."
  An outlined pill with a thin crisp white outline, transparent inside, white uppercase neutral sans: "PEÇA O TESTE NO WHATSAPP" followed by a thin lime arrow. No fill, glow or shadow.
  Small grey sans below the button: "Link na bio".

Render only the exact text listed above; no additional lettering, dates, credits, logos or watermarks.

REALISM
- It must pass as an unretouched photo of a real, used workspace: documentary photograph, available light, visible grain, true-to-life color.
- Materials: wooden counter with visible grain and light marks of use, pomade jars of different brands with unreadable labels, cords, a few hair clippings.
- Forbidden: showroom-clean styling, perfect symmetry of objects, CGI look, moody grading, readable invented text, logos or brand marks, and any run-down, cheap or dirty look.
```


## Story · 1080×1920 (9:16)

Gerar com --aspect 9:16 --size 2K e --ref da capa aprovada. A figurinha de link (WhatsApp do teste) entra no app, na faixa vazia entre 70% e 80%.

```text
A vertical 9:16 documentary photograph for an Instagram story (1080×1920) of the same campaign.
Reference image 1 is the approved carousel cover: keep the same barbershop, the same barber's general look and clothing, and the same colors. Recompose natively for a tall vertical frame; do not crop or stretch the reference.
Evening, 8 pm, after closing: the glass storefront shows the dark street outside and half of the lights are already off. The barber sits sideways in his own barber chair, elbow on the armrest, rubbing his eyes with one hand; across his knee and down to the floor runs a long strip of white paper from the old adding machine on the counter, about two meters, curling into a few loose loops near the chair. The paper has only faint printed columns, too small and blurred to read.
Camera: 35mm f/2 at eye level, documentary, focus on his face and hands.
Composition: his head at about 26% and his hands at about 38% of the height; the paper reaches the floor at about 62%. From 52% downward the photograph darkens smoothly into near-black (#0A0A0A). Keep 70% to 80% of the height empty and evenly dark for an Instagram link sticker added later.

SERIES BIBLE (same place and same barber in every slide; layout changes per slide)
- Place: a well-kept, mid-market neighborhood barbershop in a Brazilian city, about 5 by 8 meters, successful and organized, the kind of place a regular customer trusts. Warm grey matte walls with one wall of exposed brick, wood-look porcelain floor, a glass storefront facing the street; warm LED spotlights on a ceiling track plus daylight from the storefront; two modern black hydraulic barber chairs in good condition; a long mirror with a simple wooden frame; a wooden counter with neatly arranged pomade jars of different brands, spray bottles, clippers on a charging base with their cords, a hand towel and a cup of coffee; a small waiting area with a fabric bench, a plant and a wall TV. During work there are a few hair clippings around the chair. Framed prints, a price board and a calendar on the wall stay soft, out of focus and unreadable.
- The barber (same man in every slide): Rafael, 38, Brazilian, mixed-race, sturdy build with a small belly, short buzz cut with a receding hairline, a patchy salt-and-pepper beard trimmed a few days ago, a small healed scar through the left eyebrow, a faded black tattoo of a date on the right forearm, slightly crooked lower teeth when he smiles. He wears a clean plain black polo shirt with no logo, dark jeans, clean white sneakers and a simple black watch. Not a model: a real, likable professional who owns his shop.
- Other people, when present: ordinary customers of varied ages, faces not the focus, partly turned away.
- Light: the real light of the place, warm LED spotlights mixed with daylight from the storefront, pleasant and natural, one dominant direction; time of day as stated in each slide. No bare fluorescent tubes, no Edison bulbs, no moody concept lighting.
- Photography: documentary reportage photograph taken during a normal working day for a Brazilian news magazine; full-frame camera, 35mm f/2 lens at eye level, available light, visible ISO grain, slightly imperfect framing, true-to-life color with mixed white balance, no color-grading look.
- Brand treatment lives only in the design layer: lime (#C8F028) never appears on objects in the scene; it appears only in the typography and interface listed for each slide, at most one line or word.
- Type voices: DISPLAY = heavy geometric sans-serif, uppercase, warm white (#F2F2F0). COUNTERPOINT = elegant high-contrast serif in italic, lowercase. UTILITY = clean monospace. Interface labels = neutral sans. Use only the voices the slide names.
- Frame: vertical 9:16 story, 1080×1920: the top 13% and the bottom 18% stay calm and dark (Instagram interface covers them).
- Top handle line, baseline at 15% of the height: "@groomyoficial" centered, lowercase exactly as written, neutral sans, white at 85%, no verification badge. Only the side labels this slide lists; no other pills, tags or labels at the top.
- No page counter in the story.

Text, rendered exactly:
- Top line: "@groomyoficial" centered; on the right, a small solid lime (#C8F028) pill ending at 92% of the width with dark uppercase "BARBEARIAS", same baseline at 15%.
- Headline, DISPLAY, centered, 50% to 62% of the height, three lines: "PARE DE FECHAR O CAIXA DE CABEÇA." with "CAIXA DE CABEÇA." in lime.
- Subline centered at 65%, UTILITY, small, white: "7 dias para testar. Depois, R$ 79,90/mês, sem fidelidade."
- Nothing between 68% and 100% of the height.

Render only the exact text listed above; no additional lettering, dates, credits, logos or watermarks.

REALISM (highest priority)
- It must pass as an unretouched photo of a real place and a real person, not a stock photo, not an advertisement, not a render.
- Skin of a 38-year-old: visible pores, uneven tone, some redness, oily forehead, fine lines around the eyes, the eyebrow scar, individual beard hairs of uneven length with grey hairs and patchy areas.
- Hands: work-worn, small cuts and dry knuckles, exactly five fingers per hand.
- Materials: leather seats with natural creases, wood grain with light marks of daily use, cotton with natural wrinkles, a few hair clippings near the chair, fingerprints on the mirror edge.
- Forbidden: model-like or symmetrical face, perfectly groomed beard, glossy or airbrushed skin, studio lighting, cinematic or moody grading, teal-and-orange, an empty or showroom-clean set, Edison bulbs, CGI look, extra fingers, readable invented text on posters or objects, logos or brand marks, and any run-down, cheap, dirty or precarious look (cracked tiles, patches, stains, bare fluorescent tubes, exposed wiring, broken furniture).
```
