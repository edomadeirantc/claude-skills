# Família F — Social de conversão (carrossel de feed)

Carrossel de Instagram feito para **parar o polegar e levar ao arraste**:
foto emocional que escurece na base, título enorme, um acento de cor, selo
do perfil e sinais claros de sequência (pontos, "ARRASTE", botão). Refs.:
IG01–IG10 (`referencias.md §1.3`). Segue a arquitetura de `prompts.md §6`, o
bloco de realismo de `realismo-fotografico.md §R.6` e o QA de `../SKILL.md §12`.

A Família F não substitui A–E: use-a quando o objetivo é **alcance e
conversão no feed** (salvar, comentar, seguir, chamar no direct) e o
público responde mais a manchete que a contemplação. Quando a marca pede
atmosfera premium, mantenha A–E e aplique só o **kit de sequência** (§F.4).

---

## F.1 DNA observado (medido nas refs, 1080×1440)

- **Formato das refs:** 3:4, 1080×1440. **Entrega da skill: 1080×1350**
  (feed) e 1080×1920 (story). As porcentagens desta família são do layout
  4:5. Gerador que só entrega 3:4: componha para o corte e converta as
  posições pela tabela de `formatos-e-composicao.md §5.6`.
- **Foto que vira fundo de texto:** sujeito nos 75% superiores; a própria
  foto escurece em gradiente para quase preto (`#000000`–`#0A0A0A`) a partir
  de ~50% da altura, preto pleno por volta de 85%. Não é card nem tarja.
- **Título gigante na base**, 3–4 linhas, ocupando 52–80% da altura, centrado
  (IG01, IG02, IG04, IG09, IG10) ou alinhado à esquerda (IG03, IG05).
- **Um acento por série**, repetido no botão, no losango dos pontos, na tag
  e numa palavra/linha do título (IG04: a última linha inteira no acento).
- **Selo de identidade:** @handle no topo (ver §F.3) e, opcional, selo de
  perfil acima do título (avatar redondo + nome + verificado, IG01) ou pílula
  de vidro escuro com o @ (IG04).
- **Sinais de sequência:** pílula de CTA "ARRASTE PARA O LADO" (83–88%),
  pontos com losango ativo (90%), "01/0N" à esquerda e "ARRASTE →" à direita
  (92%). No último slide: pontos (losango no último) e numeração ficam; sai
  só o "ARRASTE →"; entra o CTA final.
- **Arraste:** as refs escrevem "ARRASTA →" (coloquial); a skill usa
  "ARRASTE →". Escolha um pelo tom da marca no briefing e repita igual em
  todos os slides; nunca misture.

### Acentos medidos (amostragem de área)

| Ref. | Acento | Uso |
|---|---|---|
| IG01 | dourado `#C8A063` | pílula de CTA, círculo da seta, losango |
| IG02, IG03, IG05 | vermelho `#E0312E` | pílula, tag "AGORA"/"URGENTE", losango |
| IG04 | laranja-vermelho `#EE451A` | linha final do título, seta da linha de apoio, losango |
| IG06–IG08 | azul `#219BEE` | palavras destacadas no corpo, losango |
| IG09 | verde `#5FBF6E` | tag "NUTRIÇÃO", losango |
| IG10 | bege `#D9B994` | tag "CLÍNICA", losango |

Na peça nova o acento vem **da marca**, não da tabela. Marca com duas cores
fortes: em post de produto, o acento é a cor da **embalagem**; em post
institucional/SaaS, a cor principal do logo. A segunda cor não entra. Sem
material visual para amostrar, pergunte na rodada 1 e, até a resposta, use
um acento marcado `PROVISÓRIO` no prompt e na entrega.

**Marca de foto clara (high-key):** a base não precisa ser preta. Escureça
a foto para o neutro mais escuro da própria marca (ex.: marrom-café em vez
de preto) com texto claro, ou mantenha a base clara contínua e use texto
escuro (variante clara de IG06–IG08). Luz direcional e "um acento" valem
nos dois casos; troque `low-key`/`near-black` do prompt §F.6 pelo neutro
escolhido.

### Tipografia observada (famílias livres equivalentes)

| Ref. | Desenho | Alternativa livre |
|---|---|---|
| IG01–IG04 | condensada pesada, caixa-alta | Anton, Bebas Neue, Oswald 700 |
| IG05 | grotesca larga pesada, minúsculas | Archivo Black, Archivo Expanded 800 |
| IG09 | geométrica bold, minúsculas | Inter Display 700, Manrope 800 |
| IG10 | serif display de alto contraste | Abril Fatface, Playfair Display Black |
| IG06–IG08 | sans neutra (estilo app) | Inter |

Escolha o desenho pelo **nicho e tom** (`nichos-e-ideias.md`): condensada
para urgência/negócio, serif display para estética/luxo, geométrica para
saúde leve/nutrição/SaaS amigável, grotesca larga para notícia/finanças.

---

## F.2 Arquétipos

| ID | Arquétipo | Ref. | Núcleo de prompt |
|---|---|---|---|
| F1 | Retrato-capa com manchete | IG01, IG02, IG04 | `A close portrait of {PERSON} looking {DIRECTION}, low-key directional light, the photograph itself fading smoothly into near-black from 50% of the height downward, reserved for a giant headline.` |
| F2 | Manchete de notícia | IG05 | `{PERSON} small in a {PLACE}, lit by {LOCAL_LIGHT}, surrounded by motion-blurred passers-by and bokeh; the bottom 40% falls into deep shadow for a left-aligned headline.` |
| F3 | Cartão de autor (post de texto) | IG06–IG08 | **Não gerar.** Montar no design: fundo liso, avatar, nome, @, título e corpo (§F.5) |
| F4 | Especialista do nicho com tag | IG09, IG10 | `{PROFESSIONAL} of the niche, {NICHE_GESTURE_OR_OBJECT}, warm natural light; a small category pill top-right; optional dotted constellation on the area being explained.` |
| F5 | Fechamento salvar/agir | IG03, IG08 | Fundo liso da série (preto ou branco), título curto, subtítulo, botão de contorno com ícone de marcador "SALVAR ESTE POST" ou CTA da marca |

Composições-assinatura que **não** se repetem (`referencias.md §0`): retrato
frontal de pessoa pública com selo de outro perfil (IG01); modelo em jaqueta
de couro olhando de cima (IG04); jovem de capuz olhando o celular na multidão
noturna (IG05); profissional de jaleco segurando uma tigela de salada para a
câmera (IG09); retrato 3/4 com linhas pontilhadas sobre o rosto (IG10). Tire
delas a **estrutura** (zonas, hierarquia, acento, sinais de sequência) e crie
a cena a partir do produto.

---

## F.3 @handle no centro do topo (regra da série)

Onde as referências põem o nome da marca, a skill põe o **@ do Instagram**:

- **Centro do topo, x = 50%**, linha-base a 6% no 4:5 (8,8% se gerado em 3:4 para corte; ~15% no story), sans
  neutra 500–600, ~28–32 px a 1080 px de largura, sem fundo. Ex.: `@suamarca`.
- Esquerda (x = 6%) e direita (x = 94%) são opcionais: tema/capítulo à
  esquerda e **tag de categoria** em pílula à direita (IG03/IG05/IG09/IG10)
  *ou* um rótulo de texto, nunca os dois do mesmo lado.
- O @ aparece **em todos os slides**, na mesma posição; é a assinatura que
  identifica o post quando ele é compartilhado. Tag de categoria, gatilho,
  passo e rótulo de ação **não** repetem em todos: seguem a tabela de
  recorrência de `microtipografia-editorial.md §2.3` (nas refs, a tag
  aparece só na capa e "AGORA" só no fechamento).
- Grafia exata: minúsculas, com o ponto/sublinhado da conta real. Confirmar
  no briefing. Nada de @ inventado ou de marca de outra conta.
- **Selo verificado** (✓ azul) só se a conta for verificada. Caso contrário,
  não desenhe: simular verificação engana o público.
- Quando houver selo de perfil acima do título (F1), o @ do topo continua;
  o selo mostra nome + avatar, o topo mostra o @.

Detalhes de grade, escala e contraste em `microtipografia-editorial.md §2–§4`.

---

## F.4 Kit de sequência (aplicável a qualquer família)

| Elemento | Posição (altura) | Frase de prompt ou regra |
|---|---|---|
| Pílula de CTA de arraste | 83–88%, centrada | `a solid {ACCENT} pill button with dark uppercase sans text "ARRASTE PARA O LADO", next to a small solid {ACCENT} circle containing a dark right arrow` (só na capa) |
| Pontos de página | 90%, centrados | `{N} small grey squares in a row with ONLY the {k}th replaced by a small {ACCENT} diamond; all other squares plain grey` (N = nº de slides) |
| Numeração | 92%, x = 6% | `"01/06" small grey sans` (sem espaços) |
| Arraste | 92%, terminando em x = 94% | `"ARRASTE →" small grey uppercase sans` (some no último slide) |
| Tag de categoria | 6–9%, terminando em x = 94% | `a small solid {ACCENT} pill with dark uppercase label "{CATEGORIA}"` |
| Salvar (último slide) | após o subtítulo | `an outlined white pill with a bookmark icon and the text "SALVAR ESTE POST"` |

Cor do kit: cinza claro (~`#A0A0A0`) sobre base escura; cinza médio
(~`#6E6E6E`) sobre fundo claro; confira contraste no fundo real.

**Kit aplicado às famílias A–E:** foto, paleta e tipografia continuam da
família; posições e desenho de pontos, numeração e pílula seguem esta
tabela (substituem o rodapé a 94% de `formatos-e-composicao.md §7.4` para
toda a série). O botão final continua o **de contorno**
(`interface-vidro.md §V.7`); a pílula sólida de arraste só aparece na capa.
Sempre: um único CTA por slide, a mesma ação pedida no briefing.

Texto pequeno gerado pela IA erra com frequência: se a numeração, os pontos
ou a tag saírem errados, gere sem eles e aplique em camada (caminho B de
`microtipografia-editorial.md §4`).

Erros observados no caso Groomy (8 slides gerados): (1) o gerador entregou
3:4 (1792×2400) apesar de `4:5`, com o @ a ~4% e o rodapé a ~96%, o que um
corte para 4:5 cortaria; (2) com `--ref` da capa, o primeiro ponto ficou
lime em vários slides além do ponto atual; (3) com "keep typography
exactly", os 8 slides saíram com a mesma diagramação. Correções: conferir a
proporção do primeiro arquivo (`formatos-e-composicao.md §5.6`), frase
"ONLY the current one" nos pontos, e referência só de identidade
(`variacao-de-layout.md §V.4`).

---

## F.5 Cartão de autor (F3) em camada de design

Gerar texto corrido por IA não é confiável. Monte no Figma/Canva/HTML:

- Fundo liso da série (branco `#FFFFFF` ou preto `#0A0A0A`).
- Bloco centrado verticalmente (≈ 38–65% da altura), margem esquerda 8%.
- Avatar circular 110 px real do autor (foto fornecida, nunca gerada como se
  fosse a pessoa), nome em sans 600, verificado só se for verdade, @ em cinza.
- Título sans 700 (~44 px), corpo sans 400 (~34 px), 1–2 palavras do corpo no
  acento da marca.
- Mesmos pontos, numeração e "ARRASTE →" do kit (§F.4).

Use F3 como **slide de respiro** dentro de um carrossel F1/F4 (opinião do
especialista, passo a passo) ou como série inteira de autoridade.

---

## F.6 Prompt base (capa F1, entrega 1080×1350)

Gerado em 4:5. Se o gerador só der 3:4, troque a primeira linha por
`A portrait 3:4 photograph…`, acrescente `Keep the top 4% and bottom 4% as
plain continuous background with nothing important; they will be cropped.`
e substitua cada porcentagem pela coluna 3:4 de `formatos-e-composicao.md
§5.6`.

```text
A portrait 4:5 photograph for the cover slide of an Instagram carousel.
{SUBJECT_SENTENCE: person or product from the brand universe, gesture, wardrobe}
Camera: {50mm f/2 | 85mm f/1.8}, eye level, focus on the nearest eye or the product label.
Light: one low-key directional light from {SIDE}, deep natural shadows, no flat light.
Palette: {BRAND_NEUTRALS}; {ACCENT_NAME} ({ACCENT_HEX}) is the only accent; no other strong colors.
Composition: the subject occupies 5% to 72% of the height. From 50% downward the photograph itself fades smoothly into near-black (#0A0A0A), fully dark from 85%; no box, card or band. Keep 4–9% calm for the top identity line.
Text, rendered exactly:
- "{@handle}" centered at the top, small neutral sans, white at 80% opacity, baseline at 6% of the height.
- Headline in a heavy condensed uppercase sans, warm white, centered, 52% to 80% of the height: "{TÍTULO}", with "{PALAVRA_OU_LINHA}" in {ACCENT_HEX}.
- {Optional subline in small uppercase sans with a thin right arrow, 81–84%: "{APOIO}".}
- A solid {ACCENT_HEX} pill at 85% with dark uppercase sans "ARRASTE PARA O LADO" and a small {ACCENT_HEX} circle with a dark right arrow beside it.
- At 90%, {N} tiny grey squares with the first replaced by a {ACCENT_HEX} diamond.
- At 92%: "01/0{N}" small grey at 6% of the width; "ARRASTE →" small grey ending at 94%.
Render only the exact text listed above; no additional lettering, dates, credits, logos or watermarks.
[REALISM BLOCK — realismo-fotografico.md §R.6]
```

Miolo: mesma luz, paleta e kit, com **layout e voz tipográfica diferentes a
cada slide** (`variacao-de-layout.md`); troque distância/gesto (§7.4 de
`formatos-e-composicao.md`), tire a pílula de arraste, mantenha pontos e
numeração. Fechamento: F5/L12 ou o plano mais calmo da série com o CTA da marca.

Ordem dos `--ref` nos slides depois da capa: **IMAGE 1 = capa aprovada**,
só para identidade (pessoa, lugar, luz, paleta; nunca layout ou tipografia,
`variacao-de-layout.md §V.4`), **IMAGE 2 = foto real do produto** (rótulo),
como em `edicao-iterativa.md`. Corpo sem rosto: use o bloco R.6 sem as
linhas de rosto, olhos e lábios, com foco no rótulo ou na pele mais próxima
(`realismo-fotografico.md §R.6`).
