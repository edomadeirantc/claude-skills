# Variação dentro do universo — layouts, vozes tipográficas e referência

Um carrossel aprovado em consistência pode cansar em sequência: todo slide
com foto em cima, título gigante centrado na base e subtítulo embaixo.
**Carrossel = um universo, não uma cena**: fixos na série só luz, paleta,
acento, materiais e pares tipográficos (`repertorio-mercado.md §R.5`);
cena, escala, câmera, densidade de texto e cabeçalho variam por slide e
saem do storyboard (V.5).

## V.0 Diagnóstico do caso Groomy (8 slides gerados, aprovados em consistência)

| Sintoma | Causa | Correção nesta skill |
|---|---|---|
| Todos os slides com a mesma diagramação | Um único prompt-base de layout (F1) aplicado aos 8 | Cada slide recebe um **arquétipo de layout** diferente (V.2) |
| Mesma fonte, mesmo peso, mesmo tamanho, sempre centrado | Uma só "voz" tipográfica na série | Sistema de **3 vozes** (V.3), alternadas por papel do slide |
| Slides 2–8 copiaram a capa | `--ref` da capa com "keep typography and kit exactly" | Referência só de **continuidade**, sem layout (V.4) |
| Mesma distância e mesma câmera | Roteiro sem coluna de enquadramento | Storyboard com movimento, escala, câmera, layout, voz e densidade por slide (V.5) |
| Arquivos 1792×2400 (3:4) apesar do pedido 4:5 | O gerador ignorou a proporção | Conferir a proporção do 1º arquivo; se vier 3:4, reescrever com a tabela de `formatos-e-composicao.md §5.6` |
| **Rodada 2:** contador com 6–7 pontos ou ponto aceso errado em 5 de 8 slides | O gerador não conta elementos pequenos repetidos | Kit em camada, nunca no prompt (`familia-social-conversao.md §F.4`, `scripts/kit_overlay.mjs`) |
| **Rodada 2:** personagem e cenário de banco de imagem | Bíblia genérica (arquétipo de revista, luz dramática, personagem médio) e capa genérica propagada | Ficha de personagem, ambiente vivo, registro documental e portão da capa (`realismo-fotografico.md §R.9–R.13`; detalhes por nicho em `nichos-e-ideias.md §N.5`) |
| **Rodada 2:** tag "BARBEARIAS" no slide 4, fora da recorrência | Herdada da capa | `Nothing on the right` nos slides sem tag |

## V.1 O que fica fixo e o que varia

| Fixo na série (bíblia) | Varia por slide |
|---|---|
| Luz, paleta, um acento, materiais; pessoa só se houver personagem | Arquétipo de layout (V.2) |
| (nada fixo aqui) | Lugar e escala: cenário principal em até 2/3 dos slides; os outros em macro, só tipografia, objeto-herói ou outro lugar do mesmo mundo (R.5) |
| @ em todos os slides, mesma grafia e tamanho (posição pelo movimento: centro do topo por padrão, rodapé na J, microrrótulo no MK13); recorrência dos rótulos (`microtipografia-editorial.md §2.3`) | Voz tipográfica do título (V.3) |
| Kit de sequência: pontos, numeração, "ARRASTE" (em camada) | Posição do bloco de texto: base, topo, esquerda, centro, sobre o objeto |
| Pares tipográficos escolhidos (no máximo 2 famílias + 1 mono) | Câmera (lente · altura · ângulo) e distância: detalhe, meio corpo, plano aberto, de cima. Nunca na bíblia |
| Tratamento da base escura (ou neutro da marca) | Dispositivo de interface: nenhum, tags, balão, legenda, botões, número gigante |

**Regras de variação**
1. Dois slides seguidos nunca usam o mesmo layout.
2. Nenhum layout aparece mais de 2 vezes em 6–10 slides; use pelo menos 4 layouts num carrossel de 8.
3. Capa e final têm layouts próprios; o final é o mais calmo.
4. Um slide de **respiro** (sem foto, ou foto quase sem texto) a cada 4–5 slides.
5. A variação vem do papel do slide, não do acaso: cada escolha tem um motivo na linha do storyboard (V.5).

## V.2 Arquétipos de layout para slides

| ID | Layout | Melhor papel | Ref. de estrutura | Núcleo de prompt (texto exato vai na lista fechada) |
|---|---|---|---|---|
| L1 | **Manchete na base** | capa | IG01, IG02, IG04 | `photo fades into near-black from 50% down; huge headline centered at 52–80%` |
| L2 | **Pilha tipográfica** | stake, virada | N09, E1 | `three stacked lines filling 20–75% of the height: a heavy sans line, a giant serif italic line, a heavy sans line, over the darkened photograph` |
| L3 | **Legenda de cinema** | dor, história | — | `cinematic 2.39:1 frame: solid black letterbox bars cover the top 14% and bottom 22%; the scene lives in the band between; a film subtitle in white sans, centered in the lower bar, two short lines, like a movie subtitle` (legenda branca; amarelo só se não for a cor da marca) |
| L4 | **Balão de mensagem** | dor, objeção, prova de rotina | — | `one or two generic chat message bubbles (rounded, no app logo, no app interface) floating over the scene at 30–50% of the height, with a small timestamp; the headline below` |
| L5 | **Cartão de autor** (sem foto) | respiro, opinião | IG06–IG08, F3 | aplicar em camada (`familia-social-conversao.md §F.5`) ou `plain #0A0A0A background, left-aligned headline and paragraph block` |
| L6 | **Tags de vidro + constelação** | como funciona | G02, V.3–V.4 | `three frosted-glass pill tags linked by 1-px lines placed on the scene` (`interface-vidro.md`) |
| L7 | **Número gigante** | resumo, oferta | — | `a single giant number "{N}" in the accent color filling 35–60% of the frame width, the photograph darkened behind it, a short line under it` |
| L8 | **Coluna lateral** | virada, benefício | §5.2 | `text block left-aligned in the left 48% of the width from 15% to 60% of the height; the subject in the right third` |
| L9 | **Título atrás do sujeito** | capa alternativa | R13, R07 (princípio) | `giant headline behind the subject: the subject's head and shoulders overlap the letters, crisp silhouette` |
| L10 | **Impresso no objeto** | dor, virada (quando o objeto tem papel/tela) | — | `the line of text appears printed on the {paper/receipt/label} in a monospace font, following its curve and perspective` (risco alto de erro: no máximo 4 palavras) |
| L11 | **Fileira de botões/chips** | resumo, oferta | IG01 (pílula), V.7 | `a vertical stack of 3–4 outlined pills, each with a short label and a small check mark, left-aligned at 8% of the width` |
| L12 | **Fechamento liso** | final | IG03, F5 | `plain background of the series, left-aligned headline, subline, one outlined button` |

Composições-assinatura das refs continuam proibidas (`referencias.md §0`);
os layouts acima são estruturas de página, não cenas.

## V.3 Três vozes tipográficas por série

Escolha uma família para cada voz (no máximo 2 famílias + 1 mono) e use a
voz pelo **papel** do texto. Manter a fonte da capa em toda a série é
válido; nesse caso a variação vem de peso, caixa, tamanho, alinhamento e
layout.

| Voz | Uso | Exemplos livres |
|---|---|---|
| **Display** | manchete de capa, número gigante | Archivo Black, Anton, Inter Display Black, Abril Fatface |
| **Contraponto** | palavra emocional, citação, pilha tipográfica | Instrument Serif Italic, Playfair Display Italic, DM Serif Display |
| **Utilitária** | legenda de cinema, balões, rótulos, números, impresso no papel | Inter, IBM Plex Mono, JetBrains Mono |

Pares por tom da marca:
- **Técnico/ofício** (SaaS de serviço, barbearia, oficina): Display geométrica pesada + mono utilitária + serif itálica só em 1–2 slides.
- **Premium/estética**: serif display + sans fina.
- **Saúde leve**: geométrica bold + serif itálica.
- **Notícia/finanças**: grotesca larga + mono.

Mono e itálica nunca no mesmo bloco; cor de acento em no máximo uma linha
ou palavra por slide.

Observado na rodada de segurança eletrônica (25/10/2026): com "very wide extended heavy grotesque" o gerador alternou entre fonte larga e condensada na mesma série. Descreva a voz display pela forma ("tall condensed heavy grotesque, bold condensed headline style") e repita a mesma frase em todos os prompts; quando um slide sair com outra fonte, corrija por edição usando um slide aprovado como amostra de tipo (`edicao-iterativa.md`). Palavra-chave do título nunca fica coberta por objeto: o sanduíche cobre só a ponta de uma letra.

## V.4 Referência de continuidade, nunca de layout

Do slide 2 em diante, a capa aprovada entra como referência de
**continuidade** (lugar, aparência geral e roupa da pessoa, cores), nunca de
layout, e só nas linhas do storyboard marcadas "mesmo lugar da capa? sim".
Slide em outro lugar ou outra escala vai sem a capa, senão o gerador copia
o cenário. Não use as palavras `identity`, `same face` ou `face of the
reference`: num teste da PlantMed, um prompt com essa formulação e imagem
anexada foi bloqueado pelo filtro de política do gerador. Slides sem pessoa
vão sem referência.

```text
Reference image 1 is the approved cover: keep the same place, the same {PERSON_ROLE}'s general look and clothing, and the same colors. Do not copy its layout, text positions, font sizes, headline treatment or composition: this slide uses the "{LAYOUT}" layout described below.
```

Proibido nos slides 2+: `keep the typography exactly`, `match the reference
exactly`. A consistência tipográfica vem da descrição das vozes (V.3)
repetida palavra por palavra na bíblia da série, não da imagem.

## V.5 Storyboard por slide (canônico, antes de copy e prompts)

Esta é a única tabela de roteiro da skill; `briefing-perguntas.md`,
`ganchos-e-copy.md` e os templates apontam para cá. Preencha uma linha por
slide depois do conceito escolhido e antes da copy final e dos prompts.

| # | papel | movimento (MK## + verbo) | escala/cena | câmera (lente · altura · ângulo) | layout L# | voz | nº palavras | cabeçalho | mesmo lugar da capa? (--ref sim/não) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | capa | MK06 transformar | objeto-herói em estúdio | 50mm · altura da mesa · frontal | L9 | display | 5 | 3 âncoras · @ no centro | é a capa (sem --ref) |
| 2 | stake | MK14 literalizar | plano aberto, outro lugar do mesmo mundo | 24mm · altura do peito · leve contra-plongée | L3 | utilitária | 9 | só o @ | não |
| 3 | dor | MK13 recortar com luz | macro de mão no escuro | 100mm macro · rente · lateral | L8 | contraponto | 18 | microrrótulos na cena · @ em microrrótulo | não |
| 4 | respiro | só tipografia (TM2 escala extrema) | sem foto | sem câmera | L5 | display + contraponto | 4 | só o @ | não |
| … | | | | | | | | | |

Regras (conferir antes de escrever prompts):

1. Duas linhas seguidas nunca repetem movimento, câmera ou layout.
2. O objeto-símbolo da família aparece em no máximo 1/3 das linhas.
3. Pelo menos 3 linhas com até 6 palavras, 1 linha só tipográfica, no
   máximo 3 linhas com parágrafo.
4. `--ref` "sim" só quando o slide está no mesmo lugar da capa.
5. Câmeras distintas em pelo menos metade dos slides (arredonde para cima).
6. 4+ layouts distintos, um respiro, capa e final distintos.
7. O cabeçalho varia (3 âncoras, 2 âncoras, microrrótulos, só o @); o @
   está em todas as linhas, com a mesma grafia e o mesmo tamanho. Em
   carrossel de lista (passos, falhas, mitos), o rótulo de passo ocupa a
   âncora lateral nos slides de conteúdo no lugar da terceira âncora; mesmo
   assim um slide de conteúdo pode cair para `— · @ · —` (precedência em
   `microtipografia-editorial.md §2.3`).

A câmera de cada prompt vem da coluna "câmera" desta tabela, nunca da
bíblia da série. Mostre o storyboard e espere aprovação antes dos prompts
(no atalho "decide você", entregue junto e avise que pode ser ajustado).
