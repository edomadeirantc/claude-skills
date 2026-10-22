# Realismo fotográfico — pessoas, texturas e nitidez

Feedback do cliente (caso de telemedicina, após o carrossel C4): as peças estavam
certas de ideia, composição e copy, mas **faltava realismo nas pessoas, nas
texturas e no pixel**. Este módulo é obrigatório em toda peça com pessoas ou
superfícies em close.

O "visual de IA" vem de quatro causas, e cada uma tem um antídoto:

| Causa | Como aparece | Antídoto |
|---|---|---|
| Palavras que puxam para render/retoque | Pele de cera, brilho uniforme, tudo "limpo" | Vocabulário de **câmera e lente reais**; proibir render, retoque e beleza |
| Ausência de imperfeição | Rostos simétricos, pele sem poro, tecido sem ruga | Pedir **imperfeições específicas**, por idade e por material |
| Luz sem física | Rosto iluminado de todos os lados, sombra rasa | Uma fonte principal com direção, **luz rasante** que revela textura |
| Pouca resolução no detalhe | Fios de cabelo e poros "pintados" | Gerar em 2K **com o bloco de realismo**, e finalizar com o passe de realismo em 4K |

---

## R.1 Palavras proibidas (puxam para o visual artificial)

Remova de todos os prompts de peças com pessoas:

`hyperreal 3D render`, `CGI`, `octane`, `unreal engine`, `render`,
`clean retouching`, `flawless`, `perfect skin`, `beautiful`, `gorgeous`,
`glowing skin`, `smooth`, `airbrushed`, `porcelain`, `dreamy`, `ethereal`,
`8K`, `ultra HD`, `masterpiece`, `trending`.

`hyperreal 3D render` (F1) só é aceitável em peça **sem pessoas** com objeto
de material (vidro, cromo). Com pessoas, use sempre F2/F4.

## R.2 Vocabulário de câmera (o que puxa para fotografia)

| Elemento | Frase |
|---|---|
| Câmera | `shot on a full-frame digital camera` ou `shot on medium format` |
| Lente retrato | `85mm f/1.8 prime lens` (close) · `50mm f/2` (meio corpo) · `35mm f/2.8` (ambiente) |
| Foco | `focus locked on the nearest eye`, `natural falloff of focus behind` |
| Exposição | `natural exposure, highlights not clipped, deep but readable shadows` |
| Grão | `fine natural sensor grain, visible at 100% zoom` |
| Cor | `true-to-life color, no color grading filter, no teal-and-orange look` |
| Pós | `minimal retouching, editorial magazine standard: skin texture left intact` |

Acabamento **F4 · Fotografia editorial real** (padrão para pessoas):
`A real photograph, shot on a full-frame camera with an 85mm f/1.8 prime lens, natural light, minimal retouching to editorial magazine standard, skin texture left intact, fine natural sensor grain, true-to-life color.`

## R.3 Pele, rosto e cabelo (por idade)

Base para todos:
```text
Real human skin: visible pores across the nose, cheeks and forehead, fine vellus hair catching the light, subtle redness around the nose and eyes, uneven natural skin tone, small moles and marks, natural oil sheen on the T-zone. Slight natural facial asymmetry. Eyes with detailed iris texture, moist lower lash line, natural catchlights from the real light source, a few visible blood vessels in the whites. Lips with fine vertical lines and natural dryness. Eyebrows and lashes with individual hairs.
```

| Idade | Acrescente |
|---|---|
| 20–30 | `occasional tiny blemish, faint under-eye shadows` |
| 30–45 | `fine lines at the outer corners of the eyes and on the forehead, light expression lines when smiling, slight under-eye texture` |
| 45–60 | `defined crow's feet, nasolabial folds, some sun spots, slightly thinner skin on the eyelids, a few grey hairs` |
| Barba | `individual beard hairs with varied direction and thickness, visible skin between them, a few stray hairs` |
| Pele negra/morena | `rich warm undertones, natural highlights on cheekbones and forehead, no ashy or grey cast, pores and texture as visible as on any skin` |

Cabelo: `individual strands with natural flyaways and baby hairs at the hairline, varied thickness, real shine only where the light hits`.
Mãos: `visible knuckle creases, fine lines on the fingers, natural nail beds with slight unevenness, subtle veins on the back of the hand, exactly five fingers`.

## R.4 Materiais e superfícies

| Material | Frase |
|---|---|
| Linho | `visible slubby linen weave, irregular thread thickness, deep natural creases and soft wrinkles, slightly matte surface` |
| Algodão/lençol | `fine cotton weave visible up close, soft wrinkles, slight sheen on the folds` |
| Grama | `individual blades of varied width, color and direction, some dry or bent blades, tiny seeds and dew drops` |
| Musgo | `dense moss with individual fronds, tiny sporophytes, damp highlights, darker soil showing through` |
| Nuvem | `volumetric clouds with soft internal shadows and wispy edges, varied density, no repeated shapes` |
| Céu | `smooth sky gradient with fine natural grain, no banding` |
| Vidro | `real refraction and reflection of the surroundings, faint fingerprints and micro-scratches` |
| Madeira | `visible wood grain, slight wear on the edges` |

## R.5 Luz que revela textura

- **Uma fonte principal com direção declarada** (`low sunrise light from the right`).
- **Luz rasante** sobre a superfície que deve mostrar textura (`raking light across the linen reveals every crease`).
- **Sombras de contato** onde pele toca tecido, cabelo toca travesseiro, pé toca grama.
- **Luz de preenchimento natural**, não estúdio: `soft bounce light from the bright clouds below`.
- Proíba: `no flat even lighting, no beauty dish look, no glow around the subject`.

## R.6 Bloco de realismo (cole em todo prompt com pessoas)

```text
REALISM (highest priority)
- A real photograph, not a render or illustration: shot on a full-frame camera with an {85mm f/1.8 | 50mm f/2 | 35mm f/2.8} prime lens, natural light, focus locked on the nearest eye, minimal retouching to editorial magazine standard.
- Real human skin: visible pores, fine vellus hair, uneven natural skin tone, small moles and marks, subtle redness around the nose and eyes, natural oil sheen on the T-zone, {AGE DETAILS}. Slight natural facial asymmetry. Detailed irises, moist lower lash line, real catchlights. Lips with fine lines. Individual hairs in brows, lashes, beard and hair, with natural flyaways.
- Hands: visible knuckle creases, natural nail beds, subtle veins, exactly five fingers per hand.
- Materials: {MATERIAL PHRASES FROM §R.4}.
- Light: {ONE MAIN SOURCE WITH DIRECTION}, raking light that reveals texture, contact shadows where skin meets fabric.
- Image quality: tack-sharp micro-detail at 100% zoom, natural sensor grain, highlights not clipped, true-to-life color.
- Forbidden: plastic or waxy skin, airbrushing, beauty filter, symmetrical doll-like faces, glowing skin, CGI or 3D-render look, over-sharpening halos, HDR, oversaturated color.
```

## R.7 Pipeline de nitidez

1. **Gerar em 2K com o bloco R.6** (nunca 1K para peças finais).
2. Aprovar composição, pessoas e texto.
3. **Passe de realismo em 4K** (`edicao-iterativa.md §E.5`) sobre a aprovada.
4. Conferir a 100% e 200% de zoom: poros, cílios, trama do tecido, letras.
5. Exportar a partir do 4K para o tamanho final (1080×1350 para carrossel),
   com `scale=…:flags=lanczos` — reduzir de 4K concentra o detalhe e aumenta
   a nitidez percebida no feed.
6. Se o passe 4K alterar rostos, use um upscaler não generativo no lugar.

## R.8 QA de realismo (100% de zoom)

- [ ] Poros e pelos finos visíveis no rosto em close.
- [ ] Pele com variação de tom e pequenas marcas; nada uniforme.
- [ ] Rostos levemente assimétricos, olhos com textura de íris.
- [ ] Mãos com dobras, unhas reais e cinco dedos.
- [ ] Tecido com trama e rugas reais; superfícies sem aspecto de plástico.
- [ ] Luz com direção única e sombras de contato.
- [ ] Sem halos de nitidez, sem HDR, sem brilho em volta das pessoas.
