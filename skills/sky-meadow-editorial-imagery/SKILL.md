---
name: sky-meadow-editorial-imagery
description: Use para criar, dirigir, editar e finalizar arte de alto impacto em nível de mercado — post único, carrossel de Instagram 1080×1350, story 1080×1920, anúncio (feed, Stories/Reels, display), slide 16:9 e hero web — a partir de um acervo de referências validadas (padrão de mercado MK, carrosséis IG, peças aprovadas) que ensina o movimento da ideia sem copiar a cena. Identifica nicho e branding pelo material, faz rodadas de perguntas, propõe 3 conceitos fora da caixa e entrega prompts para o CLI/API desta skill (Gemini), para outras IAs (ChatGPT/GPT Image, Midjourney, Flux, Ideogram) e copy aplicada. Inclui templates testados (carrossel de conversão, pitch, produto na pele, clínica premium em fundo preto com regras CFO/CFM, segurança eletrônica), tipografia de contraste, realismo, edição iterativa, conversão entre formatos e exportação web. Não use para ícones, diagramas, UI de produto ou ilustração plana.
---

# Editorial Imagery — arte de alto impacto em nível de mercado

Sistema para gerar imagens a partir de um acervo visual catalogado de
referências de mercado e peças aprovadas (caso de telemedicina). A imagem nunca é
decoração atrás do texto: ela é **composta para o texto**, nasce de **uma
ideia forte** e é **lapidada por edições cirúrgicas** até ficar pronta.

---

> **Versão pública:** inclui as gerações próprias autorizadas pelo usuário (G01/G02), os 10 carrosséis IG01–IG10 e as 26 referências de mercado MK01–MK26 (publicados a pedido do usuário, só para consulta), seus índices visuais e `assets/catalogo.json`. As 34 referências R/N e as artes de cliente com pacientes (RC) ficam só no pacote local; no público, os registros delas não têm caminho. Não alegue consulta visual a uma imagem ausente.

---

## 0. Fluxo obrigatório

A ideia vem antes da família, e a variação é planejada antes do prompt.

0. **Preflight**, uma vez por sessão: `python "<raiz-da-skill>/scripts/check_assets.py"`
   (pasta da instalação). Erro bloqueia: informe o ID. O `generate.py`
   repete a checagem antes de gerar. **Material de cliente fica desligado:**
   só se o usuário **nomear** um cliente que tenha pasta em `clientes/`,
   leia a `ficha.md` dele e rode com `--cliente <pasta>`. Sem o nome no chat,
   não liste, procure nem abra `clientes/`; nicho parecido usa T4/T5.
1. **Brief em rodadas:** leia todo o material e preencha sozinho os fatos
   (`[INFERIDO]` quando deduzido). Pergunte só as decisões, com resposta
   recomendada (`references/briefing-perguntas.md`): ação única, @handle,
   formato e nº de slides. Nicho, público, acento da marca e restrições
   legais: `references/nichos-e-ideias.md §N.1–N.3` (SaaS: `saas.md`).
2. **Salto + 3 conceitos:** abra referências reais conforme
   `references/acervo-visual.md` (até 4 por peça; carrossel: índice MK
   obrigatório e 1–2 IG do papel da capa). Rode o salto de
   `references/repertorio-mercado.md §R.3` (verbo de cada MK, inventário do
   cliente, busca fora do nicho) e leve **3 conceitos** (seguro, ousado,
   fora da curva) com as alavancas de `nichos-e-ideias.md §N.4`. As
   referências são a régua, não o molde: a cena nasce do cliente; teste
   anti-réplica contra R/N/IG/MK e contra o clichê do nicho.
3. **Família e template a partir do conceito escolhido:** só agora escolha
   a família (tabela abaixo) e, se o pedido combinar, um template
   (`references/templates/README.md`). A família fixa luz, paleta, acento,
   materiais e par tipográfico. **Ela não fixa cena, escala nem câmera.**
4. **Storyboard por slide** (`references/variacao-de-layout.md §V.5`): uma
   linha por slide com movimento MK, escala/cena, câmera (lente · altura ·
   ângulo), layout, voz, nº de palavras, cabeçalho e se repete o lugar da
   capa. **Carrossel = um universo, não uma cena** (`repertorio-mercado.md §R.5`).
   Post único e anúncio: uma linha, com 2–3 variações para teste.
5. **Copy:** título de 3–7 palavras; o contraste tipográfico vem do
   movimento (`repertorio-mercado.md §R.2`), não de itálico obrigatório.
   CTA com verbo; nada que a marca não confirmou. Ganchos, legenda e alt
   text: `references/ganchos-e-copy.md`. **@handle** exato em todos os
   slides, no centro do topo por padrão (o movimento pode levá-lo ao rodapé
   ou a um microrrótulo, sem mudar grafia nem tamanho); demais rótulos pela
   recorrência de `microtipografia-editorial.md §2.3`. Entregas 1080×1350 e
   1080×1920 (`formatos-e-composicao.md §5.6–§5.7`).
6. **Prompts:** um por linha do storyboard, na ordem de slots de
   `references/prompts.md §6`; paleta e materiais da bíblia, câmera da
   linha do storyboard; bloco de realismo (`realismo-fotografico.md §R.6`)
   em peças com pessoas ou close. A capa aprovada entra como `--ref` só nos
   slides do mesmo lugar, para continuidade, nunca para layout. Prompts
   para outras IAs: pacote multi-IA (`modelos-e-producao.md §9.5`).
7. **Autochecagem antes de entregar** (§12.1): responda os 6 itens na
   entrega. Reprovou um, refaça o storyboard ou o prompt antes de mostrar.
8. **Gerar em 2K**, aprovar a capa, **editar** com 1–3 mudanças
   (`edicao-iterativa.md`), **4K** na final (`§E.5`, `realismo-fotografico.md §R.7`),
   **converter formatos** recompondo (`§E.6`), **QA** (§12), produção web
   (`modelos-e-producao.md`) e **entrega** (§14). Ideia reprovada: volte ao 2.

---

## Mapa dos arquivos

| Precisa de… | Leia |
|---|---|
| Fichas das 34 referências R/N, dos 10 carrosséis IG, das 26 referências de mercado MK e das peças aprovadas | `references/referencias.md` |
| Famílias G–J (metáfora de objeto, cinema com contraponto, janela de interface, caderno), tipografia de contraste e o salto fora da caixa | `references/repertorio-mercado.md` |
| Consulta obrigatória, permissões e catálogo das imagens | `references/acervo-visual.md` e `assets/catalogo.json` |
| Verificar arquivos e hashes (uma vez por sessão) | `python "<raiz-da-skill>/scripts/check_assets.py"` (`--json`, `--detalhe`; `--cliente <pasta>` só com o cliente nomeado) |
| Letrinhas no topo: esquerda, centro (@handle no Instagram) e direita | `references/microtipografia-editorial.md` |
| Rodadas de perguntas do briefing, com resposta recomendada | `references/briefing-perguntas.md` |
| Nicho, branding e gerador de ideias fora da caixa | `references/nichos-e-ideias.md` |
| Ganchos (26 fórmulas), roteiro, CTA, anti-IA e legenda | `references/ganchos-e-copy.md` |
| SaaS e apps: metáforas, carrossel, hero, o que não afirmar | `references/saas.md` |
| Família F — carrossel social de conversão, kit de sequência | `references/familia-social-conversao.md` |
| Storyboard por slide (tabela canônica), layouts L1–L12, 3 vozes, referência de continuidade | `references/variacao-de-layout.md` |
| Família A — céu & campo, objeto monumental | `references/familia-ceu-campo.md` |
| Família B — saúde com detalhe do corpo e interface de vidro | `references/familia-saude-vidro.md` |
| Famílias C, D e E — produto, esporte, tipografia sobre paisagem | `references/familias-produto-esporte-tipo.md` |
| Vidro em degradê, cards, tags, constelação, botões | `references/interface-vidro.md` |
| Zonas seguras por formato (feed, story, post único, anúncio, display, slide), séries, carrossel panorâmico, tipografia | `references/formatos-e-composicao.md` |
| Arquitetura de prompt e banco de frases (prompts prontos da Família A no apêndice de `familia-ceu-campo.md`) | `references/prompts.md` |
| Método de edição, diagnóstico de erros, upscale, conversão | `references/edicao-iterativa.md` |
| Modelos (Gemini, Midjourney, outras IAs), pacote multi-IA, texto atrás do sujeito, hero web, exportação | `references/modelos-e-producao.md` |
| Realismo de pessoas, pele, texturas e nitidez; antídoto do banco de imagem, ficha de personagem, ambiente vivo, portão da capa | `references/realismo-fotografico.md` (detalhes por nicho em `nichos-e-ideias.md §N.5`) |
| Contador do carrossel (pontos, numeração, "ARRASTE") em camada | `scripts/kit_overlay.mjs` |
| Templates por tipo de peça (T1 carrossel de conversão, T2 pitch 16:9, T3 produto na pele, T4 clínica premium em fundo preto, T5 segurança eletrônica), com prompts | `references/templates/README.md` |
| Cliente com ficha, diagnóstico e prompts prontos (só na instalação local, fora do Git; **só quando o usuário nomear o cliente**) | `clientes/{cliente}/ficha.md` |
| Protocolo de teste: rubrica, briefs de teste e registro de rodadas | `references/testes.md` |
| Caso real completo com prompts aprovados | `references/caso-telemedicina.md` |
| Imagens e índices visuais distribuídos | Caminhos e permissões em `assets/catalogo.json`: G01/G02 em `assets/aprovadas/`, IG01–IG10 em `assets/carrosseis/`, MK01–MK26 em `assets/mercado/`, planilha de pitch em `assets/templates/`, índices em `assets/indices/`; R/N e RC não distribuídos |

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
| **G · Metáfora de objeto** | Um objeto do ofício transformado diz a frase; fundo limpo; um acento | Serviço abstrato, anúncio, post único, carrossel (um movimento por slide) | MK03, MK06, MK10, MK11, MK13, MK24 |
| **H · Cinema com contraponto** | Foto de cinema em que a tipografia atravessa, é engolida ou literaliza a cena | Manifesto, capa, autoridade, carrossel | MK01, MK02, MK08, MK09, MK14, MK19, MK21, MK22 |
| **I · Janela de interface** | Paisagem calma com a tela real do cliente flutuando | SaaS, app, monitoramento, ferramentas | MK07, MK12, MK15, MK17, MK18, MK20, MK23, MK26 |
| **J · Caderno editorial** | Papel com textura, título serif itálico com dois-pontos, miniaturas e setas manuscritas | Passo a passo, bastidor, estudo de caso, carrossel | MK04, MK05, MK16, MK25 |
| **K · Clínica premium no preto** | Preto, contorno fino no perfil, dourado discreto, foto real | Clínica, HOF, odonto, estética | `templates/t4-clinica-premium-fundo-preto.md` |
| **F · Social de conversão** | Foto que escurece na base, título gigante, um acento, @ no topo, pontos e pílula de arraste | Feed de alcance: salvar, comentar, direct, teste/demo | IG01–IG10 |
| **A · Céu & Campo** | Céu cerúleo, colina, um objeto ou figura monumental, um acento | Natureza, bem-estar, território | R01–R16, N04, G01 |
| **B · Saúde & Vidro** | Detalhe do corpo contra céu aço liso, tags de vidro e constelação | Saúde, telemedicina | N07, N12, N17, G02 |
| **C · Produto em textura** | Produto sobre musgo ou na pele, luz recortada, monocromia | Suplemento, cosmético, kit | N06, N08, N13, N15, N16 |
| **D · Esporte lifestyle** | Quadra azul, branco esportivo, lime, forma gráfica que entrelaça o sujeito | Esporte, energia, protetor solar | R06, R13, N10, N11, N14, N18 |
| **E · Tipografia sobre paisagem** | Paisagem escurecida virando cartaz, pilha tipográfica | Manifesto, evento, capa | N04, N09, R09, R10 |
| *Vidro sobre paisagem* (transversal) | Paisagem desfocada atrás de painel de vidro | Slides de conteúdo, stories | N01, N02, N03, N05 |

Nenhuma família é padrão: ela sai do conceito escolhido no passo 2. Ao
combinar famílias, mantenha **uma** luz, **uma** paleta e **um** acabamento.

---

## Princípios de nível de mercado

1. **Uma ideia, um herói, um acento.** Tudo o mais é silêncio.
2. **O texto tem lugar reservado.** Zona limpa em porcentagem no prompt;
   contraste calculado para a cor do texto (`formatos-e-composicao.md`).
3. **Texto e imagem se entrelaçam** quando possível: título atrás da cabeça,
   tag sobre a pele, fita passando atrás e na frente.
4. **Realismo fotográfico acima de tudo:** câmera e lente reais, pele com
   poros e imperfeições, tecido com trama, luz com direção. Nada de render,
   retoque ou "pele perfeita" (`realismo-fotografico.md`).
5. **Mesmas pessoas em todos os formatos**, convertidas da peça aprovada.
6. **Interface só quando o movimento pede** (1 px, pontilhado, vidro fosco);
   nunca como ornamento padrão.
7. **Edite, não regenere.** Composição aprovada se preserva; corrige-se o resto.
8. **Prompt diz o que fica vazio** com a mesma precisão do que aparece, e
   proíbe por nome os erros já vistos (card, halo, linhas, textos que vazam).
9. **Referência é vocabulário, não composição.** Das R/N/IG/MK tire o
   movimento, a luz, a tipografia e o acabamento; o **sujeito e a cena
   nascem do universo da marca**. Nunca reproduza uma composição-assinatura
   (`references/referencias.md §0`). Teste: lado a lado com a referência,
   alguém diria "é a mesma foto com outro texto"? Então descarte.
10. **Carrossel conta uma história em cenas diferentes.** Cada slide é uma
    etapa (gancho → desenvolvimento → virada → ação) e um movimento próprio;
    o fio é a luz, a paleta e o acento, não a cena (`repertorio-mercado.md §R.5`).

---

## 12. QA

### 12.1 Autochecagem antes de entregar prompts (responda na entrega)

1. Storyboard lado a lado: três linhas seguidas parecem "a mesma foto com
   outro texto"? Refaça.
2. Linhas `Camera:` distintas nos prompts: pelo menos metade do nº de slides.
3. Densidade: 3+ slides com até 6 palavras, 1 só tipográfico, no máximo 3
   com parágrafo (carrossel de 7+ slides).
4. Busca nos prompts por `cerulean|grassy hill|35mm f/2 at eye level|identity|same face|match the reference exactly`:
   cada ocorrência justificada ou removida.
5. Cada prompt traz, fora do texto do prompt, o movimento MK que o originou.
6. Anti-réplica contra a MK citada: a cena não é a cena dela.

### 12.2 Rubrica de teste (0–2 por critério; passa com 9/12 e sem 0 nos dois primeiros)

Ideia em 2 s · variação da série · assinatura do cliente (o logo de um
concorrente não serviria) · contraste tipográfico do movimento · realismo ·
texto e regras legais exatos. Registro de rodadas: `references/testes.md`.

### 12.3 Checklist de aprovação da peça

Reprove a peça se qualquer item **crítico** falhar.

**Crítico**
- [ ] A peça tem uma ideia legível em 2 segundos.
- [ ] Zona do texto limpa e contraste do texto dentro do planejado no pior ponto.
- [ ] Anatomia correta: mãos, dedos, rostos, membros.
- [ ] Texto **exatamente** o especificado, com acentos corretos; nenhum texto
      extra (marca, ano, meta-linha que vazou, letras inventadas em embalagem).
- [ ] Nenhuma pessoa real, celebridade, personagem ou logotipo de terceiros.
      Exceção: o próprio cliente ou profissional, gerado a partir da foto real
      dele como `--ref` e com o rosto conferido lado a lado com essa foto.
- [ ] Rostos idênticos aos da peça aprovada (em edições, conversões e upscale).
- [ ] Não reproduz nenhuma composição-assinatura das referências R/N/IG/MK nem o clichê do nicho sem subvertê-lo.
- [ ] Instagram: @handle exato em todos os slides (centro do topo por padrão;
      rodapé ou microrrótulo quando o movimento pede); selo verificado só se a
      conta for verificada; rótulos laterais pela recorrência
      (`microtipografia-editorial.md §2.3`).
- [ ] Entrega final exatamente 1080×1350 (feed) ou 1080×1920 (story); se
      gerado em 3:4, conferido o PNG cortado: nada essencial perdido.
- [ ] Ganchos, provas e números só com dado fornecido pela marca; sem urgência falsa.
- [ ] Carrossel: mesmo universo (luz, paleta, acento, materiais), cenas
      diferentes, narrativa legível na sequência; pontos, numeração e
      "ARRASTE →" aplicados em camada (`scripts/kit_overlay.mjs`), nunca
      pedidos ao gerador.
- [ ] Capa aprovada no portão da capa antes de virar referência; nada de
      banco de imagem: personagem com ficha, lugar vivo, luz do lugar
      (`realismo-fotografico.md §R.9–R.13`, `nichos-e-ideias.md §N.5`).
- [ ] Lugar e pessoas no padrão da marca (mediano bem cuidado por padrão):
      nada pobre, sujo, quebrado ou precário, salvo pedido do cliente ou do
      produto (`realismo-fotografico.md §R.11.0`).
- [ ] Carrossel: 4+ layouts distintos em 8 slides, nenhum repetido em
      sequência, um slide de respiro; vozes tipográficas pelo papel do texto.
- [ ] Série com movimento (`repertorio-mercado.md §R.5`): um movimento MK por
      slide, objeto-símbolo da família em no máximo 1/3 dos slides, 3+ slides
      com até 6 palavras, cabeçalho variando (3 âncoras, 2, espalhado, só @).
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
  telemedicina. Antes/depois e preço seguem o conselho do profissional
  (médico: CFM 2.336/2023; cirurgião-dentista: CFO 196/2019 e Código de
  Ética Odontológica art. 44, que veda preço) — `nichos-e-ideias.md §N.3`.
  Antes/depois é sempre foto real do paciente com autorização, **nunca**
  gerado ou retocado por IA. Recomende revisão jurídica da peça final.
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
   (modelo, `--aspect`, `--size`, ordem dos `--ref`); quando o usuário pedir
   prompts para outras IAs, o pacote multi-IA (`modelos-e-producao.md §9.5`).
5. **QA** (§12): itens aprovados e correções feitas.
6. **Produção web**, quando houver: hero, HTML/CSS, exportações.
7. **Limitações**: o que não foi gerado ou verificado, e riscos restantes.

Gerar pelo script da skill:

```bash
uv run ~/.claude/skills/sky-meadow-editorial-imagery/scripts/generate.py \
  --prompt-file peca.txt --out peca.png --aspect 9:16 --size 2K [--ref aprovada.png] [--ref fonte.png]
```

`--dry-run` valida sem chamar a API. Chave em `GEMINI_API_KEY`.
