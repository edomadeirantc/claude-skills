# Família A — Céu & Campo editorial

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
| Software, criação, trabalho, educação | A (mesa/cadeira/notebook) | B · Horizonte de campo |
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
- **Objetos que funcionam:** cadeira de madeira de design, mesa com notebook,
  sofá estofado, símbolo 3D de vidro/cromo, escultura, produto real ampliado,
  figura sentada lendo.
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
