# Família B — Saúde editorial com interface de vidro

Linguagem de marcas de saúde premium (N07, N12, N17): **um detalhe do corpo**
fotografado contra um **céu liso**, com uma **camada de interface fina** por cima.
É a família das peças aprovadas G02 (perfis frente a frente) do caso de telemedicina.

Componentes de interface (tags, constelação, caixas, botões): `interface-vidro.md`.
Prompts aprovados completos: `caso-telemedicina.md`.

---

## B.1 DNA — 7 pilares

1. **Detalhe, não retrato.** Mãos, perfis, ombros, pulso, nuca, cabelo. O corpo
   aparece cortado pelas bordas; a pessoa inteira quase nunca.
2. **Ele e ela.** O par masculino/feminino aparece pelo contraste de textura:
   pelos e pele mais grossa de um lado, pele lisa e traço fino do outro (N12).
3. **Céu como fundo de estúdio.** Liso, sem nuvens, em azul acinzentado ou
   aço. Nunca o cerúleo saturado da Família A.
4. **Sol quente de fim de tarde vindo do alto à esquerda**, com rim light
   dourado no contorno. Pele quente contra céu frio: é todo o contraste da peça.
5. **Duas famílias de cor e nada mais:** azul do céu e tons de pele. Acento
   só se vier do próprio objeto (N07: cápsula laranja).
6. **Interface fina e silenciosa:** linhas de 1 px, pontilhados, vidro fosco,
   texto branco. Ela comenta a foto; não compete com ela.
7. **Tipografia em dois registros:** título em serifa leve com **uma palavra
   em itálico**; rótulos e botão em sans-serif limpa.

---

## B.2 Paleta medida

| Token | Hex | Onde | Branco sobre ele | Uso |
|---|---|---|---|---|
| `steel-top` | `#546D8C` | Topo do céu (N12) | 5,33:1 ✔ | Fundo da zona de título |
| `steel-mid` | `#607B99` | Meio do céu (N12) | 4,38:1 · só texto grande | Tags e rótulos |
| `steel-base` | `#667E9F` | Base do céu (N12) | 4,16:1 · só texto grande/caixa-alta | Zona do botão |
| `soul-blue` | `#3C6B94` | Céu N07 | 5,64:1 ✔ | Variante mais saturada |
| `sky-light` | `#7CA0BC` | Céu N17 | 2,76:1 ✘ | Só com texto bold grande ou card |
| `skin-light` | `#B79A7A` | Mão N12 | — | Tom de pele de referência |
| `skin-deep` | `#977C61` | Mão N12 | — | Tom de pele de referência |
| `glass-smoke` | `#475E7C` | Vidro fumê sobre `steel-top` | 6,65:1 ✔ | Botão/tag de vidro com leitura garantida |
| `glass-clear` | `#6C819C` | Vidro claro sobre `steel-top` | 3,99:1 ✘ | Evitar para texto pequeno |

Frase de paleta para prompt (aprovada):
`a clear, flat, muted dusty steel-blue sky, #546D8C at the top easing to #667E9F at the bottom, no clouds`

---

## B.3 Arquétipos

| ID | Arquétipo | Ref. | Melhor uso | Risco principal |
|---|---|---|---|---|
| B1 | **Mãos que se encontram** | N12 | Capa, hero, cuidado a dois | Dedos fundidos ou extras |
| B2 | **Perfis frente a frente** ★ aprovado | G02 | Hero mobile e desktop, saúde mental, escuta | Rostos mudarem entre formatos |
| B3 | **Ombros lado a lado, de costas** | — | Privacidade, parceria; sem rostos | Nudez além dos ombros |
| B4 | **Gesto de cuidado** (pulso, testa, mão no ombro) | — | Coração, rotina, acompanhamento | Sugerir exame/diagnóstico |
| B5 | **Cabelo ao vento contra o céu** | — | Dermatologia, queda de cabelo | Cabelo de peruca/plástico |
| B6 | **Objeto erguido contra o céu** | N07, N17 | Produto, kit, embalagem | Rótulo ilegível; texto inventado na embalagem |

### Núcleos de prompt

- **B1:** `A close-up of two hands meeting in the air: from the left, a man's hand with visible fine arm hair and slightly rougher skin; from the right, a woman's slender hand. Their little fingers hook gently together, the other fingers relaxed and open.`
- **B2:** `Two side profiles facing each other against the sky: a man with a short beard on the left, facing right, and a woman with dark curly hair loosely tied on the right, facing left. Their foreheads almost touch, eyes closed, calm, serene expressions.`
- **B3:** `A close-up from behind and slightly below of a man's and a woman's bare shoulders and upper backs, side by side, leaning lightly against each other. Only the shoulders, necks and the backs of their heads are visible. No faces.`
- **B4:** `A man's forearm and open hand enter from the left, palm slightly up. A woman's hand comes from the right, two fingertips resting gently on the inside of his wrist.`
- **B5:** `From behind, a man's and a woman's heads side by side against the sky; her long wavy hair lifted and flowing in the wind across the frame, backlit strand by strand.`
- **B6:** `Two hands rise from the bottom edge holding {OBJECT} up against the sky, the object sharp and centered.`

Bloco de foto comum (aprovado):

```text
- Background: a clear, flat, muted dusty steel-blue sky, #546D8C at the top easing to #667E9F at the bottom, no clouds.
- Warm natural late-afternoon sun from the upper left, a soft golden rim light on the edges.
- Real skin with pores, fine hairs, knuckle creases and natural nail texture; individual hair strands.
- 85mm lens, subtle film grain, natural muted color grade.
```

---

## B.4 Layouts por formato

### 4:5 (carrossel/feed) — layout empilhado da referência

| Faixa da altura | Conteúdo |
|---|---|
| 9–25% | Título (com ou sem caixa pontilhada) |
| 30–70% | Detalhe do corpo + 3 tags de vidro + constelação |
| 73–89% | Rodapé (marca + frase) **ou** um botão único |

### 9:16 (hero mobile) — aprovado em G02

| Faixa | Conteúdo |
|---|---|
| 0–9% | Céu livre (barra de navegação) |
| 12–21% | Título em 2 linhas, sem moldura |
| 24–84% | Perfis, cortados nas bordas laterais |
| ~91% | Botão de contorno "AGENDAR CONSULTA →" |

### 16:9 (hero desktop) — conversão aprovada de G02

- Testas se tocando **no centro exato**; nuca dele em ~12% e coque dela em ~88% da largura (céu livre nas laterais = corte seguro em telas 16:10).
- Rostos entre 24% e 84% da altura; abaixo dos queixos, um V de céu aberto onde fica o botão.
- Título em **uma linha**, centrado, 12–19% da altura; topo 0–9% livre para a navegação.
- Tags: uma no cabelo dele perto da têmpora, uma na bochecha dela, uma abaixo do queixo dele.

Alternativa quando a imagem precisa dominar: **hero só com a foto** (sem texto)
e título + botão em HTML numa seção abaixo. Ver `modelos-e-producao.md §11.1`.

---

## B.5 Regras específicas

- **Mesmas pessoas em todos os formatos:** gere o formato mestre, aprove e
  converta os demais com `--ref` da peça aprovada (ver `edicao-iterativa.md §E.6`).
- **Tags são promessa de serviço.** Use só temas que a marca realmente atende.
- **Saúde e medicamento:** cápsulas, frascos e embalagens (N07, N16, N17)
  servem a marcas de suplemento/produto. Em telemedicina, prefira gestos e
  detalhes do corpo; não mostre medicamentos nem prometa resultado clínico.
- **Contraste na base:** o céu clareia embaixo (`#667E9F`, 4,16:1). Botão e
  rodapé ali pedem texto em caixa-alta/medium ou vidro fumê.
