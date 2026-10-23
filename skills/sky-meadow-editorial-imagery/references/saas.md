# SaaS e apps — hero, carrossel e lançamento

SaaS não tem embalagem nem procedimento para fotografar: o que se vende é
**tempo, controle, dinheiro ou tranquilidade**. Por isso a peça de SaaS
depende ainda mais da regra da skill: **uma ideia, um monumento, um acento**.
A metáfora carrega o benefício; a interface real do produto, quando aparece,
entra como camada de design.

Regras de base (descrição do `SKILL.md`: "não use para UI de produto"): a skill não gera UI de produto. Tela do
software = **screenshot real** fornecido pelo cliente, aplicada no
Figma/HTML (dentro de um aparelho, de um painel de vidro ou recortada), nunca
desenhada pelo modelo. `landing-page-design` confirma: o hero mostra o
**resultado**, não o dashboard.

---

## S.1 Brief específico de SaaS (acrescente à rodada 1)

- Categoria e cliente: B2B (cargo de quem compra) ou B2C.
- O trabalho que o cliente "contrata" o produto para fazer (JTBD), nas
  palavras literais do cliente (reviews, DMs, calls).
- As quatro forças: o que **empurra** para fora da solução atual, o que
  **puxa** para o produto, o **hábito** que segura, a **ansiedade** de trocar.
- Oferta real: teste de N dias, plano grátis, demo, sem cartão (só se for verdade).
- Provas disponíveis: métricas medidas, clientes que autorizam nome/logo,
  screenshots reais, prêmios. Sem prova → sem número na peça.
- Cor e fonte da marca; modo claro ou escuro do produto.

## S.2 Famílias que funcionam

| Objetivo | Família / arquétipo | Por quê |
|---|---|---|
| Hero de landing, lançamento | A · Monumento na colina (metáfora da feature) | calma, premium, espaço para título |
| Feature com dados/insight | B · detalhe do corpo + tags de vidro | humaniza o dado; tags = métricas do produto |
| Manifesto, posicionamento | E1 pilha tipográfica | opinião forte da categoria |
| Feed de alcance | F1/F2 manchete; F3 cartão do fundador | linguagem nativa do Instagram |
| Prova | F3 + screenshot real em camada | a tela real é a evidência |

## S.3 Banco de metáforas por categoria

Uma por peça; o objeto vira o monumento da Família A ou o "objeto erguido"
de B6. Material sugerido entre parênteses.

| Categoria | Dor | Metáfora-monumento |
|---|---|---|
| Gestão / ERP | caos de planilhas | uma única mesa limpa no topo da colina, um só papel sobre ela (madeira, linho) |
| Financeiro / cobrança | dinheiro escapando | uma ampulheta de vidro em que a areia sobe (vidro, latão) |
| CRM / vendas | lead esquecido | um farol aceso sobre o campo ao entardecer (pedra, vidro) |
| Marketing / automação | tarefa repetida | um dominó gigante ainda de pé, os outros já deitados em fila (cerâmica fosca) |
| RH / pessoas | time disperso | cadeiras de mesmo modelo em círculo na grama, uma no acento |
| Segurança / dados | medo de vazamento | uma chave de vidro monumental cravada na grama (vidro com refração) |
| IA / produtividade | tempo perdido | um relógio de parede deitado na grama, ponteiros parados no fim do expediente |
| Saúde-tech / gestão de clínica, academia ou estúdio | agenda e cobrança manuais | dezenas de fichas de papel levadas pelo vento sobre o campo, enquanto uma mão segura o celular em primeiro plano (dor literal + escala; sem objeto isolado no topo do morro) |
| Educação-tech | aluno que some | uma escada de livros subindo até o céu |
| Dev tools | deploy que quebra | uma ponte de vidro limpa sobre um vão |

Composições-assinatura continuam proibidas: mesa+notebook na colina (R07),
cadeira no topo (R05/R12), relógio gigante como cenário inteiro. Mude
objeto, terreno ou ângulo até passar no teste anti-réplica.

## S.4 Carrossel SaaS (8 slides)

```
1 CAPA      gancho de dor ou colapso de tempo (#5, #4, #7 de ganchos-e-copy.md)
2 STAKE     o custo da dor em uma frase (tempo, dinheiro, cliente perdido) — dado real ou qualitativo
3 DOR       a cena da dor no universo da série (mesma luz, mesma paleta)
4 VIRADA    o monumento/metáfora do produto; título com o resultado
5 COMO      3 passos em tags/cards de vidro (interface-vidro.md V.3/V.5)
6 PROVA     screenshot real em camada OU depoimento atribuído OU métrica com fonte;
            sem prova disponível → RESUMO dos recursos (nunca placeholder)
7 OBJEÇÃO   a ansiedade de trocar, respondida (migração, preço, curva de aprendizado)
8 CTA       uma ação: teste de N dias / agendar demo / comente PALAVRA
```

Kit de sequência e @handle no topo como em `familia-social-conversao.md
§F.3–F.4`. Este esqueleto tem precedência sobre `ganchos-e-copy.md §G.4`
e `formatos-e-composicao.md §7.4` em peças de SaaS.

## S.5 Hero de landing SaaS (16:9 e 9:16)

- Título de 6–12 palavras com o resultado ("[Resultado] sem [dor]",
  "[Resultado] em [prazo]"); subtítulo de 15–25 palavras com o "como".
- CTA específico ("Comece o teste de {N} dias", "Ver demonstração"); um
  principal, o secundário vira link de texto.
- Prova social logo abaixo do hero, só com número/logos reais.
- Layout: P1 (centralizado) ou P3 (texto à esquerda) de `prompts.md`. O
  screenshot, se houver, vai em HTML à direita ou abaixo, nunca gerado.
- Mobile: CTA de largura total, fonte ≥ 16 px, alvo ≥ 48 px.

## S.6 Prompt base (hero 16:9, metáfora de segurança)

```text
A wide 16:9 hyperreal image for a SaaS website hero section.
A single monumental key made of clear glass with soft internal refractions, its bow in solid {ACCENT_NAME} ({ACCENT_HEX}), stands upright, pushed into the crest of a rounded grassy hill as if locking it, casting a soft shadow.
It is set on a hill covered in dense lush grass with individually defined blades; the hill fills the lower 30% of the frame.
Camera: slightly below the crest looking up, 35mm lens, everything in sharp focus except the nearest grass blades.
Light: clear bright midday sunlight from high above and slightly behind the camera, soft natural shadows.
Palette: deep saturated cerulean sky graduating to pale blue near the horizon, lush natural green grass, crisp white clouds, with a single {ACCENT_HEX} accent on the key's bow; no other strong colors.
Composition: keep the left 48% of the frame as calm open sky with no clouds and no objects, reserved for text. Place the key in the right third, centered around 72% of the width, its top at about 30% and its base at about 75% of the height.
Finish: hyperreal 3D render with photographic lighting, physically accurate glass and grass, calm and clean.
Do not include any text, letters, numbers, logos, watermarks, signage, UI elements, borders or frames.
```

Sem pessoas, o acabamento F1 (CGI) é permitido (`realismo-fotografico.md
§R.1`). Com pessoas, F4 e o bloco de realismo.

## S.7 O que não afirmar

- "Usado por 10.000+ empresas", "aumente suas vendas em 300%" sem dado real.
- "Grátis para sempre", "sem cartão", "teste de 14 dias" se não for a oferta.
- Logos de clientes sem autorização; depoimento anônimo como prova.
- Urgência falsa ("só hoje") e comparação nominal com concorrente sem base.
- Dashboard gerado por IA como se fosse o produto.
