# T2 · Pitch deck de 5 minutos em 16:9 (startup, projeto, banca)

**Status:** testado (caso PlantMed, assistência agronômica para pequeno
produtor). Slides gerados pelo usuário; o slide 8 foi bloqueado pelo filtro
de política e passou com o prompt enxuto; resultado aprovado ("ficou bom").
Prompts finais: `casos/plantmed-pitch.md`. Modelo financeiro com fórmulas:
`../../assets/templates/modelo-financeiro-pitch.xlsx`.

**Use quando:** apresentação curta para banca, investidor, parceiro ou
cliente, projetada ou em tela, com custos e retorno.

## T2.1 Formato e estrutura

- **16:9 (1920×1080)**, `--aspect 16:9 --size 2K`. Opções 4:3, 1:1 e 3:4 só para documento impresso ou feed.
- **9 slides ≈ 5 minutos** (~35 s cada, ~390 palavras de fala no total), estrutura da skill `slides` (YC/sales) adaptada:

| # | Seção | Layout | O que prova |
|---|---|---|---|
| 01 | A ideia | monumento na colina, título no céu | a frase de posicionamento |
| 02 | O problema | coluna lateral | dor com fatos do material |
| 03 | A solução | detalhe das mãos + 3 tags de vidro | como funciona em 3 passos |
| 04 | Assinatura | 3 cards de plano | como o cliente paga |
| 05 | Pagamento do especialista | duas metades | fixo + variável por caso |
| 06 | Custos | painel de vidro com tabela | custo fixo mensal linha a linha |
| 07 | Resultado | número gigante | margem por cliente, ponto de equilíbrio, ano 1 |
| 08 | Potencial | pilha de números sobre vista aérea | mercado com fonte oficial |
| 09 | Fechamento | plano calmo, céu aberto | frase final + próximo passo |

## T2.2 Números: do material ao slide

1. Use primeiro o que o usuário informou (meta, equipe, faixa de preço, forma de pagar o especialista).
2. Complete com fonte oficial verificada (IBGE, decreto do salário mínimo, lei de piso) e cite no slide.
3. O que for estimativa vai para a aba **Premissas** da planilha, em azul, com a observação "estimativa"; o slide usa o resultado.
4. Planilha com 3 abas: Premissas → Mensal ano 1 (rampa linear até a meta, churn, custos variáveis por cliente) → Resumo (receita, custo, lucro, margem de contribuição, ponto de equilíbrio, mercado).
5. O número mais defensável na banca é o **ponto de equilíbrio** (no caso: 591 produtores, 0,26% do mercado); diga isso na fala quando a meta for agressiva.

## T2.3 Visual

- Família A (céu e campo) quando o tema é campo, natureza ou território; layouts diferentes por slide (`variacao-de-layout.md`).
- Acento = cor do logo, usado só como preenchimento de pílulas e cards (verde PlantMed `#1F4A20`); títulos em serifa grossa que ecoa o logo.
- **Logo nunca gerado:** cada prompt reserva o canto superior esquerdo (3–16% da largura, 3–12% da altura); aplique o PNG transparente ou branco por cima.
- Lugar e pessoas no padrão da marca (`realismo-fotografico.md §R.11.0`): propriedade bem cuidada, nunca precária.

## T2.4 Referências e política

- Slide 1 sem referência. Slides com as mesmas pessoas: `--ref` do slide 1 com a frase de continuidade (sem `identity`).
- **Slides sem pessoa (vista aérea, números, cards): sem referência, sem bíblia de personagens e sem bloco de pele.** O slide 8 original, com tudo isso, foi bloqueado; a versão enxuta passou.
- Se ainda bloquear: tire a linha de fonte do slide (aplique depois) e use `landscape photograph` na primeira linha.

## T2.5 Checklist

- [ ] Cada número do slide está na planilha ou tem fonte citada.
- [ ] Slides 06 e 07 conferidos número a número; se errar, texto em camada.
- [ ] Logo aplicado por cima em todos os slides.
- [ ] Fala por slide cabe no tempo (≤ 5 min no total).
- [ ] Pedido final (próximo passo) definido a partir do material ou do usuário.
