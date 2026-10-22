---
name: sky-meadow-editorial-imagery
description: Use para criar, dirigir, editar e finalizar imagens editoriais de nível profissional para hero desktop (16:9), hero mobile (9:16) e carrosséis (4:5, 1:1) — céu e campo com objeto monumental, saúde premium com detalhe do corpo e interface de vidro fosco, produto em textura e na pele, esporte lifestyle e tipografia sobre paisagem. Cobre conceito com metáfora, copy aplicada na imagem, zonas seguras, prompts prontos, edição iterativa com duas referências, conversão entre formatos com as mesmas pessoas, realismo e upscale 4K, e montagem web (hero em tela cheia, botões, exportação AVIF). Não use para ícones, diagramas, UI de produto ou ilustração plana.
---

# Editorial Imagery — hero e carrossel de nível de mercado

Sistema para gerar imagens a partir de um acervo visual catalogado de
referências de mercado e peças aprovadas (caso de telemedicina). A imagem nunca é
decoração atrás do texto: ela é **composta para o texto**, nasce de **uma
ideia forte** e é **lapidada por edições cirúrgicas** até ficar pronta.

---

> **Versão pública:** inclui as gerações próprias autorizadas pelo usuário, seus índices visuais e `assets/catalogo.json`. As 34 referências de terceiros R/N e seus originais permanecem no pacote local; no público, suas fichas são descritivas e os arquivos são marcados como não distribuídos. Não alegue consulta visual a uma imagem ausente.

---

## 0. Fluxo obrigatório

1. **Brief:** marca, público, mensagem, formatos (desktop, mobile, carrossel
   e nº de slides), cor de marca, se o texto vai na imagem ou em HTML.
   Pergunte só o que não puder deduzir; marque o que for inferido.
2. **Família e consulta visual:** escolha a família pela tabela e leia seu
   arquivo. Antes de **cada novo prompt**, inclusive quando a entrega for só
   texto, siga `references/acervo-visual.md`: abra o índice visual disponível
   e 2–4 imagens pertinentes em tamanho integral. Registre IDs, o que extrair
   e o que mudar. Consulta não é envio automático ao gerador. Para as
   letrinhas no topo, leia `references/microtipografia-editorial.md` e confira
   R08/R10/R14 quando disponíveis. Um arquétipo por peça. **Carrossel = um
   universo só**: mesma família, pessoas, luz, paleta e acabamento; varie
   gesto, distância e interface (`references/formatos-e-composicao.md §7.4`).
3. **Conceito com ideia:** antes de escrever prompt, responda "qual é a ideia
   que faz alguém parar?" (metáfora, escala, ponto de vista ou entrelaçamento
   de texto e imagem). Sem ideia, a peça vira banco de imagem.
4. **Copy:** título de 3–7 palavras com uma palavra em itálico, subtítulo de
   uma frase, CTA com verbo. Sem promessa que a marca não confirmou. Se o
   cabeçalho editorial for ativado em alguns slides, definir os três textos
   exatos, suas âncoras e quais slides o recebem; não adicionar data ou autor
   das referências.
5. **Prompt do formato mestre** (geralmente 9:16 ou 4:5) com a arquitetura de
   `references/prompts.md §6` **e o bloco de realismo** de
   `references/realismo-fotografico.md §R.6` em toda peça com pessoas ou close.
6. **Gerar em 2K** e apresentar. Se a ideia não for aprovada, volte ao passo 3.
7. **Editar** a peça aprovada com edições de 1 a 3 mudanças
   (`references/edicao-iterativa.md`), sempre a partir da última versão aprovada.
8. **Realismo + upscale 4K** da versão final (`edicao-iterativa.md §E.5`),
   seguindo o pipeline de nitidez de `realismo-fotografico.md §R.7`.
9. **Converter formatos** com `--ref` da aprovada, recompondo nativamente
   (`edicao-iterativa.md §E.6`). Nunca recorte o mobile para fazer o desktop.
10. **QA** (§12), **produção web** (`references/modelos-e-producao.md`) e
    **entrega** (§14).

---

## Mapa dos arquivos

| Precisa de… | Leia |
|---|---|
| Fichas das 34 referências e das peças aprovadas | `references/referencias.md` |
| Consulta obrigatória, permissões e catálogo das imagens | `references/acervo-visual.md` e `assets/catalogo.json` |
| Letrinhas no topo: esquerda, centro e direita | `references/microtipografia-editorial.md` |
| Família A — céu & campo, objeto monumental | `references/familia-ceu-campo.md` |
| Família B — saúde com detalhe do corpo e interface de vidro | `references/familia-saude-vidro.md` |
| Famílias C, D e E — produto, esporte, tipografia sobre paisagem | `references/familias-produto-esporte-tipo.md` |
| Vidro em degradê, cards, tags, constelação, botões | `references/interface-vidro.md` |
| Zonas seguras por formato, séries, carrossel panorâmico, tipografia | `references/formatos-e-composicao.md` |
| Arquitetura de prompt, banco de frases, prompts prontos P1–P10 | `references/prompts.md` |
| Método de edição, diagnóstico de erros, upscale, conversão | `references/edicao-iterativa.md` |
| Modelos (Gemini, Midjourney), texto atrás do sujeito, hero web, exportação | `references/modelos-e-producao.md` |
| Realismo de pessoas, pele, texturas e nitidez | `references/realismo-fotografico.md` |
| Caso real completo com prompts aprovados | `references/caso-telemedicina.md` |
| Imagens e índices visuais distribuídos | Caminhos e permissões em `assets/catalogo.json`; R/N não distribuídos |

---

## Famílias

| Família | Assinatura | Melhor para | Refs. |
|---|---|---|---|
| **A · Céu & Campo** | Céu cerúleo, colina, um objeto ou figura monumental, um acento | Marca, lançamento, bem-estar, "fora da caixa" | R01–R16, N04, G01 |
| **B · Saúde & Vidro** | Detalhe do corpo (mãos, perfis) contra céu aço liso, tags de vidro e constelação | Saúde, telemedicina, cuidado a dois | N07, N12, N17, G02 |
| **C · Produto em textura** | Produto sobre musgo ou na pele, luz recortada, monocromia | Suplemento, cosmético, kit | N06, N08, N13, N15, N16 |
| **D · Esporte lifestyle** | Quadra azul, branco esportivo, lime, forma gráfica que entrelaça o sujeito | Esporte, energia, protetor solar | R06, R13, N10, N11, N14, N18 |
| **E · Tipografia sobre paisagem** | Paisagem escurecida virando cartaz, pilha tipográfica | Manifesto, evento, capa | N04, N09, R09, R10 |
| *Vidro sobre paisagem* (transversal) | Paisagem desfocada atrás de painel de vidro | Slides de conteúdo, stories | N01, N02, N03, N05 |

Ao combinar famílias, mantenha **uma** luz, **uma** paleta e **um** acabamento.

---

## Princípios de nível de mercado

1. **Uma ideia, um monumento, um acento.** Tudo o mais é silêncio.
2. **O texto tem lugar reservado.** Zona limpa em porcentagem no prompt;
   contraste calculado para a cor do texto (`formatos-e-composicao.md`).
3. **Texto e imagem se entrelaçam** quando possível: título atrás da cabeça,
   tag sobre a pele, fita passando atrás e na frente.
4. **Realismo fotográfico acima de tudo:** câmera e lente reais, pele com
   poros e imperfeições, tecido com trama, luz com direção. Nada de render,
   retoque ou "pele perfeita" (`realismo-fotografico.md`).
5. **Mesmas pessoas em todos os formatos**, convertidas da peça aprovada.
6. **Interface fina:** 1 px, pontilhado, vidro fosco; ela comenta a foto.
7. **Edite, não regenere.** Composição aprovada se preserva; corrige-se o resto.
8. **Prompt diz o que fica vazio** com a mesma precisão do que aparece, e
   proíbe por nome os erros já vistos (card, halo, linhas, textos que vazam).
9. **Referência é vocabulário, não composição.** Das referências R e N tire
   luz, paleta, material, ponto de vista e interface; o **sujeito e a cena
   nascem do universo da marca**. Nunca reproduza uma composição-assinatura
   (`references/referencias.md §0`). Teste: lado a lado com a referência,
   alguém diria "é a mesma foto com outro texto"? Então descarte.
10. **Carrossel conta uma história.** Cada slide é uma etapa (gancho →
    desenvolvimento → virada → ação), não um pôster solto. "Totalmente
    diferente" significa outra cena dentro do mesmo universo.

---

## 12. QA — checklist de aprovação

Reprove a peça se qualquer item **crítico** falhar.

**Crítico**
- [ ] A peça tem uma ideia legível em 2 segundos.
- [ ] Zona do texto limpa e contraste do texto dentro do planejado no pior ponto.
- [ ] Anatomia correta: mãos, dedos, rostos, membros.
- [ ] Texto **exatamente** o especificado, com acentos corretos; nenhum texto
      extra (marca, ano, meta-linha que vazou, letras inventadas em embalagem).
- [ ] Nenhuma pessoa real, celebridade, personagem ou logotipo de terceiros.
- [ ] Rostos idênticos aos da peça aprovada (em edições, conversões e upscale).
- [ ] Não reproduz nenhuma composição-assinatura das referências R/N.
- [ ] Carrossel: mesmo universo em todos os slides, narrativa legível na
      sequência, paginação e "ARRASTE →" idênticas e legíveis no celular.
- [ ] Imagens pertinentes realmente abertas antes do prompt; IDs e qualidades
      utilizadas registrados. Arquivos ausentes declarados, não imaginados.
- [ ] Cabeçalho opcional: três textos exatos, âncoras consistentes, sem crédito
      alheio; leitura e contraste verificados na exportação.

**Alto**
- [ ] Um único acento; luz, paleta e acabamento iguais aos da série.
- [ ] Nenhum card, caixa ou moldura que não foi pedido.
- [ ] Nenhum véu, desfoque, halo ou vinheta em volta de botões ou na base.
- [ ] Nenhuma linha extra além das especificadas.
- [ ] Realismo a 100% de zoom: poros, pelos finos, íris, trama do tecido,
      mãos com cinco dedos, luz com direção (`realismo-fotografico.md §R.8`).
- [ ] Desktop, mobile e slides parecem o mesmo momento fotográfico.
- [ ] Sujeito dentro das margens de 5%, salvo corte intencional.

**Médio**
- [ ] Degradês sem banding (grão fino presente).
- [ ] Sem HDR, glow artificial, roxo/índigo ou neon fora da paleta.
- [ ] Ponto focal anotado para `object-position`.

Correção: diagnóstico e micro-prompts em `edicao-iterativa.md §E.4`.

---

## 13. Ética, licença e procedência

- Consulte as permissões em `assets/catalogo.json` antes de compartilhar ou
  anexar imagens. R/N são apenas estudo visual local, não entradas `--ref`
  nem material de redistribuição pública. G são peças geradas aprovadas
  autorizadas pelo usuário como referência; histórico não é alvo final.
- Não cite artistas ou fotógrafos vivos no prompt; descreva as qualidades
  visuais. Não gere pessoas reais, celebridades, personagens (R15), bandeiras
  e insígnias (R11), nem logotipos de terceiros (R01, R12, N10).
- Embalagens: use a foto real do produto como `--ref` ou gere sem rótulo;
  o modelo inventa letras.
- Saúde: sem promessa de resultado, sem medicamento em destaque em
  telemedicina; publicidade de medicamento e serviço médico segue regras da
  ANVISA e do CFM — recomende revisão jurídica da peça final.
- Registre prompt, modelo, data e referências de cada peça (§14).

---

## 14. Contrato de entrega

1. **Conceito**: família, arquétipo e a ideia em uma frase.
   **Referências consultadas:** IDs, qualidades extraídas, diferenças propostas
   e arquivos ausentes; registrar separadamente as imagens anexadas ao gerador.
2. **Copy** aplicada (título, subtítulo, CTA, tags) e alternativas avaliadas.
3. **Tabela de peças**: arquivo, formato, proporção, ponto focal, cor do texto.
4. **Prompts finais** exatos de geração e de cada edição, com parâmetros
   (modelo, `--aspect`, `--size`, ordem dos `--ref`).
5. **QA** (§12): itens aprovados e correções feitas.
6. **Produção web**, quando houver: hero, HTML/CSS, exportações.
7. **Limitações**: o que não foi gerado ou verificado, e riscos restantes.

Gerar pelo script da skill:

```bash
uv run ~/.claude/skills/sky-meadow-editorial-imagery/scripts/generate.py \
  --prompt-file peca.txt --out peca.png --aspect 9:16 --size 2K [--ref aprovada.png] [--ref fonte.png]
```

`--dry-run` valida sem chamar a API. Chave em `GEMINI_API_KEY`.
