---
name: sky-meadow-editorial-imagery
description: Use when o pedido mencionar Meadow, prompts prontos para imagens, capa ou carrossel editorial de Instagram, anúncio, story, slide ou hero fotográfico; especialmente quando faltar copy na arte, relação entre assunto e efeito visual, cabeçalho com @ central ou continuidade entre slides. Não usar para ícones, diagramas, UI de produto ou ilustração plana.
---

# Meadow — direção editorial que explica o assunto

**Estudar o pedido → selecionar referências pertinentes → construir uma narrativa → entregar arte com texto.** O acervo ensina operações visuais, não uma coleção de cenários para sortear. Céu, campo, vidro e brilho entram quando ajudam a mensagem. Um prompt pronto contém a peça inteira, não apenas a fotografia de fundo.

## 0. Fluxo obrigatório

1. **Conferir o acervo uma vez por sessão:** `python "<raiz-da-skill>/scripts/check_assets.py"`. Restaurar arquivos declarados presentes se a checagem falhar; informar os IDs. Catálogo público com `caminho=null` significa referência sem pixels, não arquivo perdido. Material em `clientes/` fica desligado: não listar, procurar ou abrir sem o usuário nomear esse cliente. Só nesse caso consultar a ficha e usar `--cliente <pasta>`.
2. **Estudar o pedido antes da estética.** Extrair tema, público, tese, ação única, formato, quantidade, textos obrigatórios, identidade e dados comprovados. Usar os fatos fornecidos; marcar deduções `[INFERIDO]`. Perguntar apenas o que impede uma entrega correta. Pedido de prompt pronto/“decide você”: recomendar uma direção e seguir; não impor rodadas de aprovação ou três conceitos. Identidade e oferta reais ausentes não podem ser inventadas; em demonstração, declarar a marca fictícia.
3. **Selecionar pelo significado e pelo papel.** Ler `references/direcao-por-pedido.md` e a tabela de `references/leitura-do-acervo.md`; consultar índices e abrir as referências candidatas conforme `references/acervo-visual.md`. Para cada referência escolhida registrar ID, observações, operação, ligação com a tese e diferença da nova cena. Só afirmar “aberta” após ver os pixels. Escolher as melhores para capa, explicação e final; é permitido reutilizar uma referência. Não impor uma MK diferente por slide.
4. **Fixar a bíblia e o roteiro.** Uma luz, paleta, acento, materiais e par tipográfico; @ e âncoras estáveis. Usar a tabela canônica de `references/variacao-de-layout.md §V.5`, acrescentando a frase “este visual explica X por Y”. Planejar gancho → desenvolvimento → síntese → ação. Variar câmera, escala e layout para servir a progressão, preservando objetos/relações reconhecíveis. Não trocar de universo apenas para cumprir variedade. Oferecer três conceitos somente quando o usuário pedir alternativas ou a decisão for materialmente aberta.
5. **Escrever a copy e o cabeçalho.** Seguir `references/ganchos-e-copy.md` e `references/microtipografia-editorial.md`. Instagram com @ informado: centro do topo em todos os slides. Na capa, usar três âncoras reais: tema/série à esquerda · @ exato ao centro · categoria à direita. Repetir o trio no slide 2 e em retomadas de capítulo; nos outros, manter @ e somente laterais úteis. Planejar as strings por slide. O trio é preferência editorial desta Meadow, não propriedade de todas as referências. Não inventar ano, crédito, selo verificado ou urgência.
6. **Entregar prompts de ARTE COMPLETA como padrão.** Ler `references/prompts.md §6`: um bloco independente por slide, com cena, função do efeito, composição, fontes, copy literal, três posições do topo e navegação conforme o roteiro. Repetir em cada bloco a paleta, o @ e as constantes necessárias; “igual ao anterior” não basta. Para prompt pronto, incluir o contador literal `01 / 06` na lista fechada; nunca pontinhos/losangos. Só gerar foto/fundo sem texto quando o usuário pedir isso explicitamente ou quando uma produção em camadas for combinada, com a copy e sua aplicação entregues juntas.
7. **Revisar antes de mostrar (§12).** Rodar o linter nos `.txt` e verificar manualmente semântica, continuidade, cabeçalho e copy. Corrigir o que falhar. Exemplo completo: `references/exemplo-agenda-editorial.md`; critérios e cenários: `references/testes.md`.
8. **Gerar somente quando solicitado.** Usar `scripts/generate.py` (Gemini) ou entregar o pacote para a IA pedida (`references/modelos-e-producao.md §9.5`). Teste 2K, aprovar a capa; corrigir por edição, final 4K quando necessário. Conferir o arquivo real, cortar/recompor para 1080×1350 ou 1080×1920 e revisar letras/contraste. Se o contador falhar, corrigir por camada limpa com `scripts/kit_overlay.mjs`, substituindo o anterior, sem duplicá-lo. Não alegar geração ou aprovação visual com base apenas no prompt ou `--dry-run`.

## Consulta por necessidade

| Necessidade | Fonte |
|---|---|
| Relação assunto–efeito, seleção de capa/miolo/final, contrato de entrega | `references/direcao-por-pedido.md` |
| Leitura visual dos 70 originais MK/IG/R/N e limites de transferência | `references/leitura-do-acervo.md` |
| Caminhos, hashes, permissões e consulta dos pixels | `assets/catalogo.json`, `references/acervo-visual.md`, `assets/NOTICE.md` |
| Fichas históricas e teste anti-réplica | `references/referencias.md` |
| Três âncoras, @ central e recorrência | `references/microtipografia-editorial.md` |
| Navegação editorial sem pontinhos; retrato-capa e final | `references/familia-social-conversao.md §F.4` |
| Storyboard, layouts L1–L12 e vozes | `references/variacao-de-layout.md` |
| Famílias G–J, operações e ritmo impacto/leitura | `references/repertorio-mercado.md` |
| Briefing; nicho, restrições e ideias; SaaS | `references/briefing-perguntas.md`, `references/nichos-e-ideias.md`, `references/saas.md` |
| Céu/campo; saúde/vidro; produto/esporte/tipografia | `references/familia-ceu-campo.md`, `references/familia-saude-vidro.md`, `references/familias-produto-esporte-tipo.md` |
| Materiais de vidro e chamadas explicativas | `references/interface-vidro.md` |
| Formatos, margens, recorte e sobreposição | `references/formatos-e-composicao.md` |
| Arquitetura de prompt e exemplo completo | `references/prompts.md`, `references/exemplo-agenda-editorial.md` |
| Realismo, edição cirúrgica e produção | `references/realismo-fotografico.md`, `references/edicao-iterativa.md`, `references/modelos-e-producao.md` |
| Templates por tipo de peça, sem importar cliente histórico | `references/templates/README.md` |
| Legenda, ganchos e alt text | `references/ganchos-e-copy.md` |
| Testes comportamentais e regressões dos scripts | `references/testes.md`, `tests/test_scripts.py` |

Todos os caminhos são relativos à raiz da skill. **Precedência interna:** segurança/licença e fatos confirmados → pedido atual → `direcao-por-pedido.md` e contrato completo de `prompts.md` → nicho → família → exemplos históricos. A navegação tem fonte única em F.4; cabeçalho em `microtipografia-editorial.md`. Casos antigos registram produções anteriores, não substituem o briefing nem as regras atuais.

## Famílias: escolher depois da ideia

| Família | Operação útil | Aplicação |
|---|---|---|
| G · Metáfora de objeto | transformar, encaixar, destacar uma diferença | serviço abstrato, método, capa |
| H · Cinema e tipografia | literalizar tese, contraste de escala, camadas | manifesto, autoridade, história |
| I · Janela de interface | demonstrar um recurso com captura autorizada | app/SaaS; sem captura, ilustração conceitual declarada |
| J · Caderno | ordenar amostras e etapas | tutorial, bastidor, resumo |
| F · Social de conversão | retrato/manchete, apoio e CTA | capa e fechamento de feed, sem herdar pontos das refs |
| A · Céu e campo | horizonte, escala, percurso | quando o conteúdo justificar a paisagem |
| B · Saúde e vidro | relacionar componentes e rótulos | explicação sem simular prova clínica |
| C · Produto | gesto de uso, textura e embalagem | produto com foto e claims autorizados |
| D · Esporte | perspectiva, gesto e energia | contexto esportivo pertinente |
| E · Tipografia/paisagem | mensagem dominante sobre ambiente | capa, manifesto |
| K · Clínica premium | retrato real, luz recortada, sobriedade | template T4 e regras do conselho aplicável |

## Princípios de composição

- Fazer imagem e texto dizerem a mesma tese: um herói, uma operação principal e um acento. Reservar espaço para título e apoio antes de detalhar o cenário.
- Manter título legível no celular; variar escala e voz sem trocar de fontes a cada slide. Microtexto é acabamento, não abrigo de informação essencial.
- Usar **brilho com causa**: fonte de luz definida, reflexão/refração nas arestas, sombra de contato e o componente explicado em destaque. Evitar bloom que lave a letra, pele plástica e interfaces decorativas. Objetos conceituais podem ter materialidade 3D convincente; pessoas exigem realismo fotográfico.
- Preservar continuidade de luz, materiais, identidade e lógica; mudar estado, etapa ou enquadramento quando a narrativa avança. Um carrossel é uma história, não seis pôsteres sem ligação.
- Consultar referências para estrutura, hierarquia e relações; criar sujeito/cena da marca. Reprovar a mesma composição com outra legenda.
- Editar a arte aprovada em vez de regenerá-la só para corrigir texto, cabeçalho ou contador.

## 12. QA

### 12.1 Antes de entregar prompts

1. **Pertinência:** cada visual explica a frase do slide; existe justificativa da seleção e diferença da referência. Se servir inalterado a qualquer assunto, refazer.
2. **Completude:** cada bloco funciona sozinho, inclui copy literal preenchida, posições, @ e contador; ausência de texto só no modo de fundo explicitamente pedido. Não misturar lista de texto com proibição global de letras.
3. **Identidade:** trio na capa e slides planejados; @ central, grafia/tamanho/linha-base consistentes. Nenhuma identidade de terceiro ou selo falso.
4. **Progressão:** o miolo responde ao gancho; resumo utilizável; CTA único. Layouts, escala e câmeras variam com propósito, não por sorteio de MKs. Nenhuma série de três cenas redundantes.
5. **Navegação:** fração legível, sem marcadores repetidos; arraste some no último. Modo integrado ou camada declarado, sem dois contadores.
6. **Honestidade:** separar planejamento de render observado; não inventar métricas, telas, fontes, consulta de arquivos ou resultados.

Automático: `python "<raiz-da-skill>/scripts/lint_prompts.py" prompts/slide-*.txt`. Bloqueia copy ausente, campos por preencher, proibição global conflitante e termos já problemáticos; também confere câmera e nota de referência. Para fundo explícito: `--background-only`. O linter é heurístico: não mede pertinência nem garante lettering.

### 12.2 Rubrica

Aplicar a rubrica de `references/testes.md`: ideia, progressão, identidade, tipografia, realismo e texto/legal. Inspeção de prompt não comprova qualidade dos pixels. Só atribuir nota de render após abrir o arquivo.

### 12.3 Aprovação da arte gerada

Conferir a 100% e a 360–390 px: copy exata com acentos, anatomia, contraste no pior trecho, margens, dimensões, continuidade, cabeçalho e navegação. Textos essenciais permanecem legíveis; não se escondem em miniaturas ou microlegendas. Sem métrica/benefício inventado. Corrigir e reinspecionar o que mudou antes de chamar a peça de pronta.

## 13. Ética, licença e procedência

- Consultar `assets/catalogo.json` antes de anexar/compartilhar. MK/IG/R/N são estudo visual; não enviar ao gerador nem copiar foto, texto, pessoa, marca ou composição-assinatura. R/N ficam locais, fora do Git. Não publicar novas cópias ou índices de terceiros nesta revisão.
- G01/G02 têm autorização específica descrita no catálogo; não presumir direitos além dela. Material de cliente e pacientes permanece privado e desligado sem nome no pedido.
- Não reproduzir celebridades, personagens reconhecíveis (R15), artistas vivos como estilo, bandeiras/insígnias ou logotipos de terceiro. Para produto/profissional real, usar material autorizado fornecido; conferir rótulo e rosto, sem insinuar endosso alheio.
- Saúde: somente claims confirmados; sem promessa de cura/resultado nem antes/depois gerado ou retocado. Identificação profissional, preço, depoimento e comparação exigem checagem das regras atuais do conselho aplicável; consultar `nichos-e-ideias.md §N.3` como ponto de partida e recomendar revisão jurídica. Informação obrigatória é aplicada em camada legível, não em microtexto.
- Registrar prompt, modelo, data, referências consultadas e anexos reais separadamente.

## 14. Contrato de entrega

Entregar: **direção escolhida e por quê → referências e operações → roteiro/copy → prompts independentes → QA e limites**. Para carrossel, incluir capa, miolo e final no mesmo universo, recorrência do topo, navegação e legenda/alt text quando pedidos. Em modo apenas prompts, não executar API nem renderizar por iniciativa própria. Em produção por camadas, entregar também a copy/posições e a aplicação final; fotografia sozinha não cumpre arte pronta.

```bash
python scripts/generate.py --prompt-file slide-01.txt --out slide-01.png --aspect 4:5 --size 2K --dry-run
python scripts/generate.py --prompt-file slide-01.txt --out slide-01.png --aspect 4:5 --size 2K
```

Chave somente em `GEMINI_API_KEY`. `--ref` recebe apenas anexos autorizados; citar caminho no prompt não envia imagem. `--background-only` é opção explícita para fundo/foto, não o padrão da Meadow. Regressões sem API: `python -m unittest discover -s tests -v`.
