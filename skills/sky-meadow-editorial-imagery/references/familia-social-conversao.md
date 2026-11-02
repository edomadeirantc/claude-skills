# Família F — Social de conversão (carrossel de feed)

Carrossel de Instagram com capa forte, copy integrada e navegação discreta.
Refs. IG01–IG10 ensinam hierarquia e papéis; os pontos/losangos observados
não fazem parte do kit atual. Seguir `prompts.md §6` para arte completa,
`microtipografia-editorial.md` para o topo e `direcao-por-pedido.md` para seleção.

No pacote público, IG são fichas sem imagens; na instalação local de
treinamento, consultar pixels somente quando o catálogo os declarar presentes.
Usar MKs disponíveis para completar a consulta visual; ver `acervo-visual.md`.

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
- **Título gigante na base**, 3–4 linhas, ocupando 52–76% da altura, centrado
  (IG01, IG02, IG04, IG09, IG10) ou alinhado à esquerda (IG03, IG05).
- **Um acento por série**, repetido no botão, no losango dos pontos, na tag
  e numa palavra/linha do título (IG04: a última linha inteira no acento).
- **Selo de identidade:** @handle no topo (ver §F.3) e, opcional, selo de
  perfil acima do título (avatar redondo + nome + verificado, IG01) ou pílula
  de vidro escuro com o @ (IG04).
- **Sinais de sequência:** pílula de CTA "ARRASTE PARA O LADO" (80–84%),
  pontos com losango ativo (90%), "01/0N" à esquerda e "ARRASTE →" à direita
  (92%). No último slide: pontos (losango no último) e numeração ficam; sai
  só o "ARRASTE →"; entra o CTA final.
- **Arraste:** as refs escrevem "ARRASTA →" (coloquial); a skill usa
  "ARRASTE →". Escolha um pelo tom da marca no briefing e repita igual em
  todos os slides; nunca misture.

As medidas acima descrevem o kit observado nas referências. Para a peça
nova, substituir a navegação pela §F.4; não reproduzir seus marcadores.

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
- Na capa e slide 2, usar três âncoras: tema/série à esquerda, @ ao centro,
  categoria à direita. Texto direto na imagem; pílula apenas se o projeto pedir.
- O @ aparece em todos os slides, na mesma posição. As laterais reaparecem
  em retomadas de capítulo e saem quando não ajudam a orientação, conforme
  `microtipografia-editorial.md §2.3`. A recorrência é planejada, não sorteada.
- Grafia exata: minúsculas, com o ponto/sublinhado da conta real. Confirmar
  no briefing. Nada de @ inventado ou de marca de outra conta.
- **Selo verificado** (✓ azul) só se a conta for verificada. Caso contrário,
  não desenhe: simular verificação engana o público.
- Quando houver selo de perfil acima do título (F1), o @ do topo continua;
  o selo mostra nome + avatar, o topo mostra o @.

Detalhes de grade, escala e contraste em `microtipografia-editorial.md §2–§4`.

---

## F.4 Navegação editorial (fonte canônica)

Substituir os pontos/losangos do corpus por **fração legível**, como
`03 / 08`, em sans utilitária, sem caixa. Uma régua fina de progresso é
opcional na produção por camada; nunca um marcador por página.

| Elemento | Posição no 4:5 | Regra |
|---|---|---|
| Fração | x=6%, linha-base y=92% | `01 / 08` até `08 / 08`; alto contraste, cerca de 28 px |
| Régua opcional | x=37–63%, y=92% | trilha neutra fina + trecho no acento proporcional à página |
| Arraste discreto | x=94%, y=92%, alinhado à direita | `ARRASTE →`; omitir no último e quando já houver chamada de avanço |
| CTA final | zona de conteúdo | uma ação, a do briefing; não competir com o contador |

**Prompts prontos para colar — padrão integrado:** incluir a fração literal
e sua posição no bloco `Text, rendered exactly:` de cada slide. A fração
é texto simples; não pedir contagem de elementos repetidos. Manter o restante
do rodapé calmo. A régua pode ser omitida no prompt integrado.

**Produção por camada — quando combinada ou para corrigir lettering:** reservar
86–96% da altura sem lettering; não gerar outro contador nessa faixa.
Depois do corte final aplicar o kit abaixo, substituindo a navegação incorreta.
Entregar o SVG e sua aplicação, não só uma promessa de “adicionar depois”.

```bash
node scripts/kit_overlay.mjs --total 8 --accent "#C8F028" --out ./kit
node scripts/kit_overlay.mjs --total 8 --h 1920 --out ./kit-story
```

Gera `kit-01.svg … kit-NN.svg` transparentes, sem dependências: fração,
régua proporcional e arraste que desaparece no final. Usar `--grey` e
`--accent` conforme contraste e identidade da série. Em story isolado não
há contador; em série de stories, respeitar as áreas da interface.

Aplicar o mesmo sistema em qualquer família. Na J, omitir o rodapé autoral
redundante: o @ permanece no topo. Não empilhar kit sobre fração já existente.
Se a arte foi gerada em 3:4, converter as posições antes do corte
(`formatos-e-composicao.md §5.6`); o SVG final entra depois do corte.

---

## F.5 Cartão de autor (F3) em camada de design

Gerar texto corrido por IA não é confiável. Monte no Figma/Canva/HTML:

- Fundo liso da série (branco `#FFFFFF` ou preto `#0A0A0A`).
- Bloco centrado verticalmente (≈ 38–65% da altura), margem esquerda 8%.
- Avatar circular 110 px real do autor (foto fornecida, nunca gerada como se
  fosse a pessoa), nome em sans 600, verificado só se for verdade, @ em cinza.
- Título sans 700 (~44 px), corpo sans 400 (~34 px), 1–2 palavras do corpo no
  acento da marca.
- Mesma fração editorial e avanço discreto da §F.4, sem pontos.

Use F3 como **slide de respiro** dentro de um carrossel F1/F4 (opinião do
especialista, passo a passo) ou como série inteira de autoridade.

---

## F.6 Prompt base (capa F1, entrega 1080×1350)

Só a capa usa este bloco; o miolo usa o layout do storyboard
(`variacao-de-layout.md §V.5`). A linha `Camera:` vem da linha do slide no
storyboard, nunca da bíblia.

Gerado em 4:5. Se o gerador só der 3:4, troque a primeira linha por
`A portrait 3:4 photograph…`, acrescente `Keep the top 4% and bottom 4% as
plain continuous background with nothing important; they will be cropped.`
e substitua cada porcentagem pela coluna 3:4 de `formatos-e-composicao.md
§5.6`.

```text
A portrait 4:5 documentary photograph for the cover slide of an Instagram carousel.
{SUBJECT_SENTENCE: the person from the character sheet (realismo-fotografico.md §R.10) doing a real gesture of the trade, in the living place (§R.11)}
Camera: {CAMERA from this slide's storyboard row: lens · height · angle}, documentary reportage, focus on the nearest eye or the product label.
Light: the real available light of the place ({LIGHT_OF_THE_PLACE}, time of day), one dominant direction, natural uneven exposure; no spotlight, no moody grading.
Palette: {BRAND_NEUTRALS}; {ACCENT_NAME} ({ACCENT_HEX}) appears only in the typography and interface, never on objects in the scene.
Composition: the subject occupies 5% to 72% of the height. From 50% downward the photograph itself fades smoothly into near-black (#0A0A0A), fully dark from 85%; no box, card or band. Keep 4–9% calm for the top handle line.
Text, rendered exactly:
- "{@handle}" centered at the top, neutral sans, about 30 px, baseline at 6%.
- "{TEMA}" left-aligned at x=6% and "{CATEGORIA}" right-aligned at x=94%, same baseline, discreet neutral sans.
- Headline in a heavy condensed uppercase sans, warm white, centered, 52% to 76% of the height: "{TÍTULO}", with "{PALAVRA_OU_LINHA}" in {ACCENT_HEX}.
- {Optional subline in small uppercase sans with a thin right arrow, 77–79%: "{APOIO}".}
- Page fraction "{01 / TOTAL}" at x=6%, baseline y=92%, small neutral sans. Keep the rest of the footer calm; no repeated page markers.
Render only the exact text listed above; no additional lettering, dates, credits, logos or watermarks.
[REALISM BLOCK — realismo-fotografico.md §R.6 + §R.12; character sheet §R.10]
```

Miolo: manter luz, paleta, material, tipografia e @; variar estado, escala
e layout para desenvolver a tese (`variacao-de-layout.md §V.5`). Usar a
fração da §F.4, sem pílula de arraste. Final F5/L12: um CTA, sem arraste.

Ordem dos `--ref` nos slides depois da capa: **IMAGE 1 = capa aprovada**,
só para continuidade (lugar, aparência e roupa da pessoa, cores; nunca layout ou tipografia,
`variacao-de-layout.md §V.4`), **IMAGE 2 = foto real do produto** (rótulo),
como em `edicao-iterativa.md`. Corpo sem rosto: use o bloco R.6 sem as
linhas de rosto, olhos e lábios, com foco no rótulo ou na pele mais próxima
(`realismo-fotografico.md §R.6`).
