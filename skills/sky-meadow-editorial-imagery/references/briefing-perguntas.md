# Rodadas de perguntas (briefing em árvore)

Método de `grilling`: as decisões formam uma **árvore**; a cada rodada
pergunte toda a **fronteira** (decisões cujos pré-requisitos já estão
resolvidos), numeradas, **cada uma com a resposta recomendada**. O usuário
responde, a árvore se reorganiza, a próxima rodada sai. Mantém a regra da
skill: **fatos você descobre; decisões o usuário toma**.

---

## Q.0 Antes de perguntar (trabalho do agente)

Leia todo o material enviado e preencha sozinho, marcando `[INFERIDO]`:

- nicho, subnicho, público e nível de consciência (`nichos-e-ideias.md §N.1`);
- cor de acento (hex amostrado), neutros, fonte, tom de voz (§N.2);
- @handle encontrado no material (bio, site, embalagem, posts);
- alegações permitidas ao público (rótulo e frases já aprovadas pela marca;
  ficha técnica e estudos só informam, `nichos-e-ideias.md §N.1`) e
  restrições do setor;
- produto e textos exatos da embalagem (para não inventar letras);
- padrão do lugar e das pessoas em cena (mediano bem cuidado por padrão;
  premium ou popular digno só se preço, site ou público indicarem;
  `realismo-fotografico.md §R.11.0`). Nunca pobre ou precário sem pedido;
- referências do acervo a consultar (`acervo-visual.md`).

Nunca pergunte o que o material responde. Pergunte só o que é **escolha**.

## Q.1 Formato da pergunta

Use a ferramenta de perguntas disponível (opções clicáveis, recomendada
marcada). Sem ela, use no chat:

```
❓ **Q1** - **Ação única do post**: o carrossel pede uma ação. (a) Salvar (b) Comentar palavra-chave (c) Chamar no direct (d) Seguir (e) Teste/demo (SaaS)

➡️ (c) Chamar no direct — produto de compra considerada; a legenda e o último slide repetem o pedido.
```

Máximo de 6 perguntas por rodada. Uma pergunta que depende de outra ainda
aberta vai para a rodada seguinte.

## Q.2 Rodada 1 — fundação (fronteira inicial)

1. **Objetivo e ação única** (salvar, comentar PALAVRA, direct, seguir, teste/demo).
2. **@handle exato** (vai em todos os slides; centro do topo por padrão), e
   se a conta é verificada.
3. **Entregas e gerador**: feed 1080×1350 e/ou story 1080×1920; nº de
   slides (6–10). O gerador entrega 4:5 nativo, só 3:4 ou ChatGPT 2:3
   (1024×1536)? (3:4 ou 2:3 → compor para o corte com a tabela de
   `formatos-e-composicao.md §5.6`.) Precisa de hero web junto?
4. **Texto**: na imagem (gerado) ou em camada (Figma/Canva/HTML) — recomende
   camada para miolos com muito texto e cartão de autor.
5. **Confirmações do `[INFERIDO]`**: nicho, público, acento, alegações
   permitidas. Peça correção só do que estiver errado.
6. **Saúde** (só se o nicho for saúde): nome do profissional, conselho, UF
   e nº de registro (ex.: `Dra. {Nome} · CD · CRO-{UF} {nº}`). Sem eles a
   peça sai com placeholder e não é publicável.

A linguagem visual (família) **não** é perguntada aqui: ela nasce do
conceito e é confirmada na rodada 2.

SaaS: acrescente as perguntas de `saas.md §S.1` que o material não respondeu.

## Q.3 Rodada 2 — ideia e capa

1. **Conceito**: apresente os 3 conceitos (seguro, ousado, fora da curva) de
   `nichos-e-ideias.md §N.4`, cada um com os movimentos MK, e a recomendação.
2. **Linguagem visual**: confirmada aqui, junto do conceito (a família nasce
   da ideia). Para cada conceito, diga a família que ele pede (G–J, F, A–E
   ou K) e recomende a do conceito recomendado.
3. **Capa**: 3 ganchos (dos 6 ângulos de `ganchos-e-copy.md §G.2`), cada um
   com a fórmula nomeada.
4. **Pessoa em cena**: modelo gerado sem rosto, rosto gerado, ou foto real
   fornecida (nunca pessoa real gerada).

## Q.4 Rodada 3 — storyboard

Mostre o storyboard por slide na tabela canônica de
`variacao-de-layout.md §V.5` (movimento, escala, câmera, layout, voz, nº de
palavras, cabeçalho, `--ref`), com título e texto de apoio de cada slide, e
a legenda. Pergunte só o que mudar. **Nenhum prompt antes da aprovação do
storyboard.**

## Q.5 Encerramento

A sessão de perguntas termina quando a fronteira está vazia: nada ficou
assumido em silêncio. Registre as decisões no topo da entrega (`SKILL.md
§14`, item 1) e siga para os prompts.

Atalho: se o usuário disser "decide você" ou já trouxer brief completo,
aplique as recomendações de **todas** as rodadas (conceito, linguagem
visual, capa e storyboard inclusive), declare cada uma como decisão tomada
e entregue storyboard + prompts juntos, avisando que o storyboard ainda
pode ser ajustado.
Sem resposta sobre verificação da conta, trate como **não verificada**.
