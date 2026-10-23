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

Variante **corpo sem rosto** (mãos, pernas, torso com produto): retire do
bloco as linhas de rosto, olhos, lábios e "focus on the nearest eye"; use
`focus locked on the product label` ou `on the nearest knuckles`, e mantenha
pele, mãos, materiais, luz e proibições. Pessoa pequena no quadro (plano
aberto): mantenha só `real photograph`, materiais, luz e proibições.

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

## R.9 Antídoto do "banco de imagem" (caso Groomy, rodada 2)

O bloco R.6 resolve a **pele**, mas não resolve o **mundo**. Na rodada 2 do
carrossel Groomy, pele e mãos saíram corretas e o resultado ainda parecia
falso: barbeiro de comercial (rosto simétrico, barba perfeita, avental de
couro, relógio caro), "barbearia de IA" (concreto escuro, lâmpada Edison,
bancada de madeira vazia) e luz dramática igual em todos os slides.

| Sintoma | Causa no prompt | Antídoto |
|---|---|---|
| Personagem genérico | Descrição média ("early thirties, clean fade, neatly trimmed beard") | Ficha de personagem com 3–5 traços marcantes (R.10) |
| Cenário sem vida | Bíblia descrevendo um arquétipo de revista (concreto, Edison, couro) e proibindo tudo que tem texto | Lugar específico, bem cuidado e em uso, com 5 camadas de vida (R.11); cartazes permitidos fora de foco e ilegíveis |
| Cara de propaganda | "premium", "cinematic", "moody", "editorial", "low-key" na bíblia | Registro documental (R.12) e luz real do lugar |
| Todos os slides iguais na luz | Uma só fonte dramática para a série | Hora do dia diferente por slide, com a mesma luz física do lugar |
| O genérico se espalha | A capa genérica vira referência dos demais | Portão da capa antes de usá-la como referência (R.13) |

Palavras que puxam o banco de imagem e só entram se a marca pedir:
`premium`, `cinematic`, `moody`, `dramatic`, `luxury`, `sleek`, `stylish`,
`Edison bulb`, `industrial concrete`, `leather apron`, `perfectly groomed`,
`model`, `handsome`, `beautiful`.

**Rodada 3 do Groomy (o erro oposto):** para fugir do banco de imagem, o
prompt pediu azulejo trincado, assento remendado, porta de enrolar e tubos
de LED frios. Saiu uma barbearia pobre e precária, que rebaixa a marca e o
cliente. Realismo vem de **vida e uso**, nunca de **dano e pobreza** (R.11.0).

## R.10 Ficha de personagem (pessoa recorrente)

Uma pessoa por ficha, repetida **palavra por palavra** em todo prompt:

```text
{NOME}, {idade exata}, {nacionalidade/origem}, {tipo físico real: peso, postura},
{cabelo real: entradas, fios brancos, corte de alguns dias},
{2–3 marcas únicas: cicatriz, dente torto, tatuagem, sardas, óculos},
{roupa limpa do dia a dia, coerente com o padrão do lugar (R.11.0)},
{um acessório comum, coerente com o perfil}. Not a model: a real, likable {papel}.
```

- Nome próprio ajuda o modelo a manter a mesma pessoa; não use nome de pessoa real conhecida.
- Nunca escreva `identity`, `same face` ou `face of the reference` em prompt com imagem anexada: pode disparar o filtro de política (bloqueio observado no caso PlantMed). Use `the same {papel}'s general look and clothing`.
- Coadjuvantes (clientes, família) em segundo plano, rosto parcial, idades variadas.

## R.11 Ambiente vivo — padrão e cinco camadas

### R.11.0 Padrão do lugar (regra)

O lugar nunca é pobre, precário, sujo ou malcuidado, a menos que o cliente
peça ou que a análise do produto exija (campanha social, antes/depois de
reforma, denúncia). O padrão vem da análise da marca e do público
(`briefing-perguntas.md` Q.0):

| Padrão | Quando | Como descrever |
|---|---|---|
| **Mediano bem cuidado** (padrão) | Pequeno negócio, SaaS para PME, serviço de bairro, produto de preço médio | `well-kept, mid-market, successful and organized`; materiais simples e bons, luz agradável, móveis em bom estado |
| Premium | Marca ou preço premium, público A | materiais nobres, design autoral, poucas peças, luz cuidada (sem cair no banco de imagem: mantenha as cinco camadas) |
| Popular digno | Público C/D, quando a marca fala com ele | lugar simples, limpo e organizado, com orgulho do dono; nunca sujo ou quebrado |

Na dúvida, mediano bem cuidado. Nunca abaixo do posicionamento da marca.
Sempre proibir no bloco de realismo: `any run-down, cheap, dirty or
precarious look (cracked tiles, patches, stains, bare fluorescent tubes,
exposed wiring, broken furniture)`.

### R.11.1 Cinco camadas de vida

Descreva o lugar como ele **é usado**, não como seria fotografado para vender:

1. **Estrutura com personalidade:** materiais e cores reais do padrão escolhido (parede de tijolo, piso amadeirado, bancada de madeira), com sinais leves de uso diário; nunca dano.
2. **Objetos de uso real, variados:** marcas diferentes, quantidades irregulares, fios, copo de café; organizado, não cenográfico.
3. **Rastros de trabalho do momento:** cabelo perto da cadeira durante o corte, papel na bancada, terra na bota no campo; não sujeira acumulada.
4. **Gente e movimento:** cliente esperando, alguém saindo, uma mão em movimento com leve desfoque.
5. **Regionalidade:** o que só existe naquele país e segmento (banco de espera, TV na parede, planta, vitrine para a rua), escolhido dentro do padrão.

Texto no ambiente: cartazes, preços e calendários existem, mas `soft, out of focus and unreadable`. Proibir só texto **legível** inventado e logotipos.

## R.12 Registro documental (vocabulário)

```text
Documentary reportage photograph taken during a normal day for a {país} news magazine; full-frame camera, 35mm f/2 at eye level, available light, visible ISO grain, slightly imperfect framing, true-to-life color with mixed white balance, no color-grading look. It must pass as an unretouched photo of a real place and a real person, not a stock photo, not an advertisement.
```

Variantes: `phone snapshot taken by a coworker, slight tilt, direct light` (UGC);
`35mm color film, slightly soft highlights` (memória/afeto). A família
visual da marca (fade, tipografia, acento) continua na camada de design,
não na luz da cena.

## R.13 Portão da capa (antes de virar referência)

A capa aprovada é a referência dos demais slides; o que ela tiver de genérico
se repete em todos. Reprove e gere de novo se 2 ou mais falharem:

- [ ] Passaria como foto de lugar real, não de banco de imagem.
- [ ] A pessoa tem os traços únicos da ficha (R.10) visíveis.
- [ ] O lugar tem as cinco camadas de vida (R.11.1) e o padrão definido (R.11.0): nem showroom vazio, nem lugar pobre ou precário.
- [ ] A luz é a do lugar, não um efeito de propaganda.
- [ ] Sem pele lisa, brilho, simetria ou grading de cinema.

Quando houver foto real autorizada do lugar ou do tipo de pessoa (cliente,
parceiro), anexe como imagem 2 só para `the look of the place, materials and
light`: é a alavanca de realismo mais forte disponível.
