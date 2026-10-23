# Variação dentro do universo — layouts, vozes tipográficas e referência

Um carrossel aprovado em consistência pode cansar em sequência: todo slide
com foto em cima, título gigante centrado na base e subtítulo embaixo. A
regra de `formatos-e-composicao.md §7.4` continua valendo (**um universo
só**), mas universo é pessoa, lugar, luz, paleta e acento, **não** o mesmo
layout repetido.

## V.0 Diagnóstico do caso Groomy (8 slides gerados, aprovados em consistência)

| Sintoma | Causa | Correção nesta skill |
|---|---|---|
| Todos os slides com a mesma diagramação | Um único prompt-base de layout (F1) aplicado aos 8 | Cada slide recebe um **arquétipo de layout** diferente (V.2) |
| Mesma fonte, mesmo peso, mesmo tamanho, sempre centrado | Uma só "voz" tipográfica na série | Sistema de **3 vozes** (V.3), alternadas por papel do slide |
| Slides 2–8 copiaram a capa | `--ref` da capa com "keep typography and kit exactly" | Referência só de **continuidade**, sem layout (V.4) |
| Mesma distância e mesma câmera | Roteiro sem coluna de enquadramento | Roteiro com colunas layout · voz · distância (V.5) |
| Arquivos 1792×2400 (3:4) apesar do pedido 4:5 | O gerador ignorou a proporção | Conferir a proporção do 1º arquivo; se vier 3:4, reescrever com a tabela de `formatos-e-composicao.md §5.6` |
| **Rodada 2:** contador com 6–7 pontos ou ponto aceso errado em 5 de 8 slides | O gerador não conta elementos pequenos repetidos | Kit em camada, nunca no prompt (`familia-social-conversao.md §F.4`, `scripts/kit_overlay.mjs`) |
| **Rodada 2:** personagem e cenário de banco de imagem | Bíblia genérica (arquétipo de revista, luz dramática, personagem médio) e capa genérica propagada | Ficha de personagem, ambiente vivo, registro documental e portão da capa (`realismo-fotografico.md §R.9–R.13`; detalhes por nicho em `nichos-e-ideias.md §N.5`) |
| **Rodada 2:** tag "BARBEARIAS" no slide 4, fora da recorrência | Herdada da capa | `Nothing on the right` nos slides sem tag |

## V.1 O que fica fixo e o que varia

| Fixo na série (bíblia) | Varia por slide |
|---|---|
| Pessoa(s), lugar, luz, paleta, um acento | Arquétipo de layout (V.2) |
| @ no centro do topo; recorrência dos rótulos (`microtipografia-editorial.md §2.3`) | Voz tipográfica do título (V.3) |
| Kit de sequência: pontos, numeração, "ARRASTE" | Posição do bloco de texto: base, topo, esquerda, centro, sobre o objeto |
| Pares tipográficos escolhidos (no máximo 2 famílias + 1 mono) | Distância e ângulo: detalhe, meio corpo, plano aberto, de cima |
| Tratamento da base escura (ou neutro da marca) | Dispositivo de interface: nenhum, tags, balão, legenda, botões, número gigante |

**Regras de variação**
1. Dois slides seguidos nunca usam o mesmo layout.
2. Nenhum layout aparece mais de 2 vezes em 6–10 slides; use pelo menos 4 layouts num carrossel de 8.
3. Capa e final têm layouts próprios; o final é o mais calmo.
4. Um slide de **respiro** (sem foto, ou foto quase sem texto) a cada 4–5 slides.
5. A variação vem do papel do slide, não do acaso: cada escolha tem um motivo na coluna do roteiro.

## V.2 Arquétipos de layout para slides

| ID | Layout | Melhor papel | Ref. de estrutura | Núcleo de prompt (texto exato vai na lista fechada) |
|---|---|---|---|---|
| L1 | **Manchete na base** | capa | IG01, IG02, IG04 | `photo fades into near-black from 50% down; huge headline centered at 52–80%` |
| L2 | **Pilha tipográfica** | stake, virada | N09, E1 | `three stacked lines filling 20–75% of the height: a heavy sans line, a giant serif italic line, a heavy sans line, over the darkened photograph` |
| L3 | **Legenda de cinema** | dor, história | — | `cinematic 2.39:1 frame: solid black letterbox bars cover the top 14% and bottom 22%; the scene lives in the band between; a film subtitle in white (or pale yellow) sans, centered in the lower bar, two short lines, like a movie subtitle` |
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

## V.4 Referência de continuidade, nunca de layout

Do slide 2 em diante, a capa aprovada entra como referência de
**continuidade** (lugar, aparência geral e roupa da pessoa, cores), nunca de
layout. Não use as palavras `identity`, `same face` ou `face of the
reference`: num teste da PlantMed, um prompt com essa formulação e imagem
anexada foi bloqueado pelo filtro de política do gerador. Slides sem pessoa
vão sem referência.

```text
Reference image 1 is the approved cover: keep the same place, the same {PERSON_ROLE}'s general look and clothing, and the same colors. Do not copy its layout, text positions, font sizes, headline treatment or composition: this slide uses the "{LAYOUT}" layout described below.
```

Proibido nos slides 2+: `keep the typography exactly`, `match the reference
exactly`. A consistência tipográfica vem da descrição das vozes (V.3)
repetida palavra por palavra na bíblia da série, não da imagem.

## V.5 Roteiro com variação (antes dos prompts)

```
#  papel    layout  voz            distância/ângulo     topo (§2.3)
1  capa     L9      display        meio corpo, baixo    — · @ · categoria
2  stake    L2      display+serif  detalhe das mãos     — · @ · categoria
3  dor      L3      utilitária     plano aberto         A DOR · @ · —
...
```

Antes de escrever prompts, confira: 4+ layouts distintos, nenhum repetido
em sequência, um respiro, capa e final distintos.
