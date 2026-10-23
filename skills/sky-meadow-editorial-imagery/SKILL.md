---
name: sky-meadow-editorial-imagery
description: Use para criar, dirigir, editar e finalizar imagens editoriais de nível profissional para hero desktop (16:9), hero mobile (9:16), carrossel de Instagram 1080×1350 (4:5, gerado em 4:5 ou em 3:4 composto para corte) e story 1080×1920 — céu e campo com objeto monumental, saúde premium com detalhe do corpo e interface de vidro fosco, produto em textura e na pele, esporte lifestyle, tipografia sobre paisagem e carrossel social de conversão (@handle no centro do topo, recorrência estratégica dos rótulos, ganchos, roteiro, legenda). Identifica o nicho e o branding pelo material, faz rodadas de perguntas com resposta recomendada e propõe conceitos fora da caixa; inclui preset para SaaS e apps. Cobre conceito com metáfora, copy aplicada na imagem, zonas seguras, prompts prontos, edição iterativa com duas referências, conversão entre formatos com as mesmas pessoas, realismo e upscale 4K, e montagem web (hero em tela cheia, botões, exportação AVIF). Não use para ícones, diagramas, UI de produto ou ilustração plana.
---

# Editorial Imagery — hero e carrossel de nível de mercado

Sistema para gerar imagens a partir de um acervo visual catalogado de
referências de mercado e peças aprovadas (caso de telemedicina). A imagem nunca é
decoração atrás do texto: ela é **composta para o texto**, nasce de **uma
ideia forte** e é **lapidada por edições cirúrgicas** até ficar pronta.

---

> **Versão pública:** inclui as gerações próprias autorizadas pelo usuário (G01/G02), os 10 carrosséis de referência IG01–IG10 (publicados a pedido do usuário, só para consulta), seus índices visuais e `assets/catalogo.json`. As 34 referências de terceiros R/N e seus originais permanecem no pacote local; no público, suas fichas são descritivas e os arquivos são marcados como não distribuídos. Não alegue consulta visual a uma imagem ausente.

---

## 0. Fluxo obrigatório

1. **Brief em rodadas:** leia todo o material (produto, PDF, site, @, posts)
   e preencha sozinho o que for fato, marcando `[INFERIDO]`. Depois pergunte
   só as decisões, em rodadas numeradas com resposta recomendada
   (`references/briefing-perguntas.md`): ação única, @handle, formato e nº de
   slides, linguagem visual, texto na imagem ou em camada. Pergunte só o que
   não puder deduzir.
2. **Template, nicho, branding, família e consulta visual:** se o pedido
   combina com um template testado (carrossel de conversão, pitch 16:9,
   produto na pele), comece por ele (`references/templates/README.md`).
   Identifique nicho, público, acento da marca, padrão do lugar e
   restrições legais
   (`references/nichos-e-ideias.md §N.1–N.3`; SaaS: `references/saas.md`).
   Escolha a família pela tabela e leia seu arquivo. Antes de **cada novo
   prompt**, inclusive quando a entrega for só texto, siga
   `references/acervo-visual.md`: abra o índice visual disponível e 2–4
   imagens pertinentes em tamanho integral (carrossel de feed: também IG).
   Registre IDs, o que extrair e o que mudar. Consulta não é envio
   automático ao gerador. Para as letrinhas no topo, leia
   `references/microtipografia-editorial.md` e confira R08/R10/R14 quando
   disponíveis. Um arquétipo por peça. **Carrossel = um universo só**: mesma
   família, pessoas, luz, paleta e acabamento; varie gesto, distância e
   interface (`references/formatos-e-composicao.md §7.4`).
3. **Conceito com ideia:** antes de escrever prompt, responda "qual é a ideia
   que faz alguém parar?" (metáfora, escala, ponto de vista ou entrelaçamento
   de texto e imagem). Sem ideia, a peça vira banco de imagem. Leve **3
   conceitos** (seguro, ousado, fora da curva) com as alavancas de
   `nichos-e-ideias.md §N.4` e o teste anti-réplica contra R/N/IG e contra o
   clichê do nicho.
4. **Copy:** título de 3–7 palavras com uma palavra em itálico, subtítulo de
   uma frase, CTA com verbo (capa da Família F: limite próprio em
   `ganchos-e-copy.md §G.1`). Sem promessa que a marca não confirmou. Capa de
   carrossel: 6 ganchos em ângulos diferentes, 3 levados ao usuário, roteiro
   em uma linha por slide aprovado antes dos prompts, legenda e alt text
   (`references/ganchos-e-copy.md`). **Instagram: o @handle exato vai no
   centro do topo de todos os slides** (`microtipografia-editorial.md §2.1`);
   os demais rótulos do topo seguem a **recorrência por função** (§2.3):
   categoria na capa e no slide 2, passo só no miolo, ação só no final,
   gatilho só na capa. Defina a recorrência no YAML da série antes dos
   prompts; não adicionar data ou autor das referências. **Entregas:**
   1080×1350 (feed) e 1080×1920 (story); gerador sem 4:5 → 3:4 composto
   para corte (`formatos-e-composicao.md §5.6`).
5. **Prompt do formato mestre** (geralmente 9:16 ou 4:5; em carrossel, o
   mestre é a **capa**) com a arquitetura de `references/prompts.md §6`
   **e o bloco de realismo** de `references/realismo-fotografico.md §R.6` em
   toda peça com pessoas ou close. Carrossel: cada slide recebe um
   **arquétipo de layout e uma voz tipográfica** do roteiro, e a capa entra
   nos slides seguintes só como referência de continuidade, nunca de layout
   (`references/variacao-de-layout.md`). Confira a proporção do primeiro
   arquivo gerado; se vier 3:4, reescreva as posições pela tabela de
   `formatos-e-composicao.md §5.6`.
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
| Fichas das 34 referências R/N, dos 10 carrosséis IG e das peças aprovadas | `references/referencias.md` |
| Consulta obrigatória, permissões e catálogo das imagens | `references/acervo-visual.md` e `assets/catalogo.json` |
| Letrinhas no topo: esquerda, centro (@handle no Instagram) e direita | `references/microtipografia-editorial.md` |
| Rodadas de perguntas do briefing, com resposta recomendada | `references/briefing-perguntas.md` |
| Nicho, branding e gerador de ideias fora da caixa | `references/nichos-e-ideias.md` |
| Ganchos (26 fórmulas), roteiro, CTA, anti-IA e legenda | `references/ganchos-e-copy.md` |
| SaaS e apps: metáforas, carrossel, hero, o que não afirmar | `references/saas.md` |
| Família F — carrossel social de conversão, kit de sequência | `references/familia-social-conversao.md` |
| Variar layout, fontes e dispositivos sem trocar de universo (L1–L12, 3 vozes) | `references/variacao-de-layout.md` |
| Família A — céu & campo, objeto monumental | `references/familia-ceu-campo.md` |
| Família B — saúde com detalhe do corpo e interface de vidro | `references/familia-saude-vidro.md` |
| Famílias C, D e E — produto, esporte, tipografia sobre paisagem | `references/familias-produto-esporte-tipo.md` |
| Vidro em degradê, cards, tags, constelação, botões | `references/interface-vidro.md` |
| Zonas seguras por formato, séries, carrossel panorâmico, tipografia | `references/formatos-e-composicao.md` |
| Arquitetura de prompt, banco de frases, prompts prontos P1–P13 | `references/prompts.md` |
| Método de edição, diagnóstico de erros, upscale, conversão | `references/edicao-iterativa.md` |
| Modelos (Gemini, Midjourney), texto atrás do sujeito, hero web, exportação | `references/modelos-e-producao.md` |
| Realismo de pessoas, pele, texturas e nitidez; antídoto do banco de imagem, ficha de personagem, ambiente vivo, portão da capa | `references/realismo-fotografico.md` (detalhes por nicho em `nichos-e-ideias.md §N.5`) |
| Contador do carrossel (pontos, numeração, "ARRASTE") em camada | `scripts/kit_overlay.mjs` |
| Templates testados por tipo de peça (T1 carrossel de conversão, T2 pitch 16:9, T3 produto na pele), com prompts finais dos casos | `references/templates/README.md` |
| Caso real completo com prompts aprovados | `references/caso-telemedicina.md` |
| Imagens e índices visuais distribuídos | Caminhos e permissões em `assets/catalogo.json`: G01/G02 em `assets/aprovadas/`, IG01–IG10 em `assets/carrosseis/`, rodadas de teste e planilha de pitch em `assets/templates/`, índices em `assets/indices/`; R/N não distribuídos |

**Precedência quando dois arquivos discordam:** (1) restrições legais e de
ética (§13) e "nenhum dado inventado"; (2) arquivo do nicho específico
(`saas.md`, linha do nicho em `nichos-e-ideias.md`); (3) arquivo da família
escolhida (zonas, tipografia, rodapé, paleta); (4) regras genéricas de
`formatos-e-composicao.md` e `prompts.md`. Família A–E com o kit da F: a
foto, a paleta e a tipografia seguem a família A–E; posição e desenho de
pontos, numeração e pílula seguem `familia-social-conversao.md §F.4`.
Todos os caminhos de `assets/` são relativos à **raiz da skill** (a pasta
deste `SKILL.md`).

---

## Famílias

| Família | Assinatura | Melhor para | Refs. |
|---|---|---|---|
| **A · Céu & Campo** | Céu cerúleo, colina, um objeto ou figura monumental, um acento | Marca, lançamento, bem-estar, "fora da caixa" | R01–R16, N04, G01 |
| **B · Saúde & Vidro** | Detalhe do corpo (mãos, perfis) contra céu aço liso, tags de vidro e constelação | Saúde, telemedicina, cuidado a dois | N07, N12, N17, G02 |
| **C · Produto em textura** | Produto sobre musgo ou na pele, luz recortada, monocromia | Suplemento, cosmético, kit | N06, N08, N13, N15, N16 |
| **D · Esporte lifestyle** | Quadra azul, branco esportivo, lime, forma gráfica que entrelaça o sujeito | Esporte, energia, protetor solar | R06, R13, N10, N11, N14, N18 |
| **E · Tipografia sobre paisagem** | Paisagem escurecida virando cartaz, pilha tipográfica | Manifesto, evento, capa | N04, N09, R09, R10 |
| **F · Social de conversão** | Foto que escurece na base, título gigante, um acento, @ no topo, pontos e pílula de arraste | Feed de alcance: salvar, comentar, direct, teste/demo | IG01–IG10 |
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
- [ ] Não reproduz nenhuma composição-assinatura das referências R/N/IG nem o clichê do nicho sem subvertê-lo.
- [ ] Instagram: @handle exato no centro do topo, idêntico em todos os slides;
      selo verificado só se a conta for verificada; rótulos laterais só nos
      slides definidos pela recorrência (`microtipografia-editorial.md §2.3`).
- [ ] Entrega final exatamente 1080×1350 (feed) ou 1080×1920 (story); se
      gerado em 3:4, conferido o PNG cortado: nada essencial perdido.
- [ ] Ganchos, provas e números só com dado fornecido pela marca; sem urgência falsa.
- [ ] Carrossel: mesmo universo em todos os slides, narrativa legível na
      sequência; pontos, numeração e "ARRASTE →" aplicados em camada
      (`scripts/kit_overlay.mjs`), nunca pedidos ao gerador.
- [ ] Capa aprovada no portão da capa antes de virar referência; nada de
      banco de imagem: personagem com ficha, lugar vivo, luz do lugar
      (`realismo-fotografico.md §R.9–R.13`, `nichos-e-ideias.md §N.5`).
- [ ] Lugar e pessoas no padrão da marca (mediano bem cuidado por padrão):
      nada pobre, sujo, quebrado ou precário, salvo pedido do cliente ou do
      produto (`realismo-fotografico.md §R.11.0`).
- [ ] Carrossel: 4+ layouts distintos em 8 slides, nenhum repetido em
      sequência, um slide de respiro; vozes tipográficas pelo papel do texto.
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

1. **Conceito**: família, arquétipo e a ideia em uma frase; nicho detectado
   e decisões das rodadas de perguntas.
   **Referências consultadas:** IDs, qualidades extraídas, diferenças propostas
   e arquivos ausentes; registrar separadamente as imagens anexadas ao gerador.
2. **Copy** aplicada (título, subtítulo, CTA, tags, @handle) e alternativas
   avaliadas; carrossel: roteiro, legenda e alt text.
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
