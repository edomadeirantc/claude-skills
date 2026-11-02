# Arquitetura de prompt e biblioteca

## 6. Arquitetura do prompt

### 6.1 Saída padrão: ARTE COMPLETA

Prompt de capa/carrossel/post/anúncio contém **imagem + copy + composição + identidade + navegação**. Escrever um bloco independente por peça: o usuário pode colá-lo sozinho em outra IA. Cada bloco repete luz, paleta, fontes, @ e formato necessários. A nota de referência não condiciona o gerador: só anexos autorizados realmente enviados podem fazer isso.

| Ordem | Slot obrigatório | Conteúdo |
|---|---|---|
| 1 | Formato e propósito | proporção, entrega, papel do slide e tese |
| 2 | Sujeito e relação | quem/o quê, gesto/estado, operação que explica a frase |
| 3 | Cenário | universo próprio da marca; referência não é cena a copiar |
| 4 | `Camera:` | lente, altura, ângulo do storyboard; composição plana quando só tipografia |
| 5 | Luz/material | direção, sombra de contato, textura; causa de brilho/refração |
| 6 | Paleta | neutros e acento da série; função do acento |
| 7 | Composição/camadas | zonas em porcentagem, espaço limpo, ordem de sobreposição |
| 8 | Tipografia | display e apoio, hierarquia e escala; texto legível no celular |
| 9 | `Text, rendered exactly:` | strings finais de cabeçalho, @, título, apoio, chamadas, contador e CTA |
| 10 | Restrições | somente lettering listado; erros pertinentes, sem anular a copy |

### 6.2 Receita do bloco final

Preencher todos os campos antes de entregar. Este é esquema de autoria, não prompt pronto:

```text
# slide N · ID da referência · L# · operação semântica
Create a portrait 4:5 complete editorial Instagram carousel slide for [papel e tese]. Intended final delivery: 1080x1350.
Subject and meaning: [objeto/gesto próprio do conteúdo e relação que demonstra].
Setting: [cena, escala e materiais próprios].
Camera: [lente, altura e ângulo desta linha do storyboard].
Light: [fonte e direção; sombra de contato; aresta com reflexo se houver].
Palette: [neutros e acento exatos, repetidos em cada bloco].
Composition: [zonas de imagem e texto; topo; rodapé; margens].
Typography: [display descrita pela forma, apoio, pesos e contraste].
Text, rendered exactly:
- [string do topo esquerdo e posição; omitir quando vazio no roteiro].
- [@ exato, x=50%, baseline y=6%; mesma fonte e tamanho em todos].
- [string do topo direito e posição; omitir quando vazio no roteiro].
- [título preenchido, quebras e posição].
- [apoio ou chamadas preenchidos e posições].
- [contador literal e posição; CTA final somente quando houver].
Render only the exact text listed above; no additional lettering, dates, credits, logos or watermarks.
[restrições específicas da peça, sem proibir globalmente texto].
```

Os campos entre colchetes são instruções de preenchimento. O bloco entregue contém as frases finais, não colchetes, chaves, “mesmo do anterior” ou caminhos/IDs no lugar da descrição. Um exemplo preenchido de seis peças está em `exemplo-agenda-editorial.md`.

Para prompts prontos, **o contador simples entra na lista fechada**: por exemplo, `"03 / 06" at x=6%, baseline y=92%, small neutral sans`. O cabeçalho obedece à recorrência de `microtipografia-editorial.md`; a navegação segue `familia-social-conversao.md §F.4`. Não omitir textos porque serão “aplicados depois” sem combinar produção em camadas.

### 6.3 Câmara, luz e efeito com função

A câmera vem do storyboard, não de um preset repetido. Variações úteis: 28–35 mm em plano aberto para situação; 50 mm na altura do objeto para relação de escala; 85–100 mm em detalhe para textura; overhead paralelo para ordem/etapas. Em página só tipográfica, escrever `Camera: not applicable; flat graphic composition`.

Descrever a causa do impacto: `a single coral component slots into the transparent assembly; directional light catches its bevels, with visible thickness, restrained refraction and a physical contact shadow`. A frase explica peça/estado; trocar “component” pelo objeto real do tema. Não usar “vidro premium” como substituto da ideia.

Pessoas: incorporar o bloco de `realismo-fotografico.md §R.6`. Objetos sem pessoas podem ser esculturas conceituais/materialidade 3D convincente. Manter arestas, reflexos e transparência; impedir glow que lave a letra. Paleta da marca precede céu azul/grama verde da referência.

### 6.4 Linguagem e completude

- Atender ao idioma de prompt pedido. Sem preferência, direção de imagem em inglês e strings visíveis no idioma final; explicar a entrega em português.
- Reservar espaço da copy antes de descrever o cenário. Especificar porcentagens/terços e contraste por área, não só “texto grande no centro”.
- Copiar literalmente a grafia de @, palavras, números e acentos. Não importar autor, crédito, ano, marca, selo ou oferta da referência.
- A imagem responde ao título, o apoio explica e o próximo slide desenvolve. Nunca usar a mesma cena com outro texto nem cenas sem fio narrativo.
- Parâmetros de proporção/resolução seguem a ferramenta; texto no prompt não garante dimensão. Conferir o arquivo real e recompor, não esticar.
- Para outra IA, cada bloco deve bastar sozinho. Informar anexos reais; caminho local no texto não envia imagem.

### 6.5 Modo explícito FOTO/FUNDO ou camadas

Usar somente quando o usuário pedir fundo/foto sem lettering ou quando a produção em camadas for combinada. Identificar a saída como fundo, reservar zonas e escrever uma proibição global de texto **nesse modo apenas**. Rodar os scripts com `--background-only`.

Em produção em camadas, fornecer simultaneamente a lista de strings, fontes, cores, posições e arquivo/comando de aplicação. Exemplos de paisagem para receber screenshot, tipos complexos, dados regulatórios e HTML continuam possíveis; não são a entrega padrão para quem pediu arte completa. Se não houver ferramenta de composição, declarar a limitação, não dizer que o carrossel está pronto.

## 15. Exemplos e famílias

- **Exemplo completo:** `exemplo-agenda-editorial.md` — seis prompts independentes com copy e navegação integrada; marca fictícia e sem métricas.
- **Retrato-capa e final:** `familia-social-conversao.md §F.6`; preencher o contrato desta §6, sem herdar pontos.
- **Metáfora, cinema, janela e caderno:** `repertorio-mercado.md §R.6`; os núcleos são material de autoria, não respostas prontas.
- **Céu/campo:** apêndice de `familia-ceu-campo.md`, somente se o pedido justificar esse ambiente.
- **SaaS:** `saas.md`; captura real autorizada ou conceito declarado, nunca tela fabricada apresentada como produto.

## 16. Exclusões por modo

**ARTE COMPLETA:** encerrar com `Render only the exact text listed above; no additional lettering, dates, credits, logos or watermarks.` Não colar proibição global de texto, letras ou números junto da copy. Restringir anatomia incorreta, marcas/rostos alheios, artefatos, segundo acento e elementos sem nexo conforme o caso.

**FOTO/FUNDO explícito:** pode proibir texto/letras/números no fundo. O identificador `--background-only` não autoriza descartar a copy de uma produção completa combinada.

O linter verifica o contrato e campos por preencher; não mede semântica, direitos, contraste ou acentos renderizados. Aplicar também o QA de `../SKILL.md §12` e inspecionar a exportação quando houver geração.
