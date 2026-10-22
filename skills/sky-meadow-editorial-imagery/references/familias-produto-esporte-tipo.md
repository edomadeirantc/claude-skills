# Famílias C, D e E — Produto, esporte lifestyle e tipografia sobre paisagem

Todas seguem a arquitetura de prompt de `prompts.md §6` e o QA de `../SKILL.md §12`.

---

## Família C — Produto em textura e na pele

Fotografia de produto premium em que **a superfície conta a história**:
musgo, pele, gotas, linho. Refs.: N06, N08, N13, N15, N16.

### DNA

- **Um produto, uma textura dominante.** Musgo denso (N08, N15), pele com
  gotas (N16), roupa esportiva de malha (N13), grama + perna (N06).
- **Luz natural recortada:** feixe de janela que cai em faixas ou manchas,
  deixando o resto em sombra profunda (N08 sombra `#070702`; N13 faixas diagonais).
- **Monocromia por família:** verde-musgo `#32331B`–`#454723` ou oliva/terra
  `#432B1A`. O produto ou a embalagem é o único acento (vermelho em N06).
- **Gesto cotidiano** quando há corpo: abrir o sachê, segurar a cápsula,
  encostar o frasco na barriga. O corpo aparece cortado, sem rosto.
- **Tipografia mínima:** serif leve + frase curta com 1–2 palavras itálicas (N06).

### Arquétipos

| ID | Arquétipo | Ref. | Núcleo de prompt |
|---|---|---|---|
| C1 | Produto no musgo, vista de cima | N08 | `A {PRODUCT} lying on a bed of deep green moss, shot top-down; a single shaft of natural window light falls on the product while the edges sink into deep shadow.` |
| C2 | Produto aninhado entre montes de musgo | N15 | `A {PRODUCT} nestled between soft mounds of lush moss, low macro angle, fine water droplets on its surface, raking natural light.` |
| C3 | Produto encostado na pele | N16 | `A hand holds a {PRODUCT} against bare skin of the abdomen, fine droplets of sweat on the skin, a small natural mole, the waistband of blue jeans at the bottom.` |
| C4 | Torso em roupa esportiva com produto | N13 | `A torso in an olive athletic set; one hand holds a single capsule between two fingers, the other hand supports two jars at waist height; warm window light falls in diagonal stripes.` |
| C5 | Gesto à beira da grama | N06 | `A hand opens a {PACKAGE} resting on a bare knee, a glass of water beside it on a white ledge, a lawn softly out of focus behind.` |

### Regras

- **Embalagem real:** use a foto do produto como `--ref` e peça
  `Reproduce the product exactly as in the reference image, including its label; do not invent text.`
  Sem referência, peça embalagem **sem rótulo** e aplique o rótulo depois:
  o modelo inventa letras (N15 saiu com "SKGRAGIND").
- Gotas: `fine natural water droplets, varied sizes, not uniform`.
- Pele: `real skin texture with pores, fine hairs, a few natural marks`.
- Medicamentos e suplementos têm regras próprias de publicidade (ANVISA). Não
  prometa efeito; valide alegações com o cliente.

---

## Família D — Esporte lifestyle

Quadra, sol duro e uma forma gráfica forte. Refs.: R06, R13, N10, N11, N14, N18.

### DNA

- **Quadra azul** de tênis/padel como chão-cor (N11, N14, N18) ou céu azul
  como fundo (R13).
- **Branco esportivo** nas roupas; o acento é **lime** (`#D4FF1A`) nas bolas,
  fitas ou tipografia.
- **Pose sentada no chão da quadra**, relaxada, com raquete e bolas espalhadas
  (N11, N14, N18). Ou ação com perspectiva forçada (R13).
- **Produto ampliado em primeiro plano** e pessoa atrás (N14).
- **Gráfico que entrelaça o sujeito:** laço lime passando atrás e na frente (N11),
  título gigante atrás (R13), texto pintado no piso (N18).

### Arquétipos

| ID | Arquétipo | Ref. | Núcleo de prompt |
|---|---|---|---|
| D1 | Sentada na quadra com laço gráfico | N11 | `A {PERSON} sits on a blue padel court in a white pleated outfit, tennis balls scattered around; giant flat lime ribbons loop behind and in front of her.` |
| D2 | Produto gigante na quadra | N14 | `A huge {PRODUCT} lies on a pale-blue tennis court in the foreground, sharp; behind it a player in white sits by the net holding the same product.` |
| D3 | Tipografia no piso | N18 | `Huge white letters "{WORD}" painted on the court surface, following its perspective, beside a seated player and a racket.` |
| D4 | Corrida em borrão de movimento | N10 | `Runners' legs and arms in strong motion blur over a flat blue surface, heavy film grain, analog color.` |
| D5 | Perspectiva forçada (já descrito) | R13 | Ver `familia-ceu-campo.md`, arquétipo D |

### Regras

- Marcas esportivas: `no visible brand logos on clothing, shoes or rackets`.
- D3 e o laço de D1 com texto erram muito; gere sem texto e aplique depois.
- D4: o borrão é estilo, mas o centro precisa de uma área calma para o título.

---

## Família E — Tipografia sobre paisagem

A paisagem vira cartaz; a tipografia é o assunto. Refs.: N04, N09 (e R09, R10 da Família A).

| ID | Arquétipo | Ref. | Núcleo |
|---|---|---|---|
| E1 | Pilha tipográfica de três registros | N09 | Sans pesada em caixa-alta + serif itálica gigante + sans pesada, empilhadas e centradas; frase pequena espaçada acima e abaixo |
| E2 | Figura mínima na encosta | N04 | `A tiny lone figure walks down a dark grassy slope under a deep teal sky with one huge diagonal cloud`; texto pequeno espalhado como legenda de exposição; marcas de corte nos cantos |

- Escureça a paisagem para texto branco: N09 `#403818` (11,7:1), N04 encosta `#1D1D1B`.
- Céu teal N04 `#146071`: branco 7,1:1.
- E1 tem alto risco de erro de letra; para peças com muitas palavras,
  gere a paisagem limpa e componha a tipografia no design.
