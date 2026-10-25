# Repertório de mercado — famílias G–J e o salto fora da caixa

As referências MK01–MK26 (`referencias.md §1.4`) foram validadas pelo
usuário como o nível profissional que a skill deve alcançar. Elas são a
**régua**, não o molde: de cada uma se tira o **movimento** (o verbo da
ideia), a tipografia e o acabamento; a cena, o objeto e as palavras nascem do
cliente. Uma peça que um observador reconheceria como "aquela referência com
outro texto" está reprovada, por melhor que esteja.

Serve para qualquer peça de alto impacto: post único, carrossel, story,
anúncio e slide (formatos em `formatos-e-composicao.md §5.6–§5.7`).

---

## R.1 Famílias

### G · Metáfora de objeto

**Assinatura:** um objeto do ofício, em escala ou estado inesperado, diz a
frase sozinho; fundo limpo (branco, cinza claro ou preto) ou um único
cenário; **um** acento saturado no objeto ou na palavra-chave.
**Refs:** MK03 (um se destaca), MK06 (o papel vira lâmpada), MK10 (menu do
sistema), MK11 (letra vira tecla), MK13 (recorte de luz), MK24 (objeto
tomado pelo tempo).

- **Tipografia:** grotesca compacta e pesada com entrelinha justa, em
  minúsculas com maiúscula inicial (Inter Tight 800, Manrope 800, Archivo
  800); marca-texto do acento atrás de 2–3 palavras; ou serif condensada +
  itálica no acento (MK24).
- **Núcleo de prompt:**
  `A single {OBJECT_OF_THE_TRADE} shown {TRANSFORMATION: becoming X | replacing the letter "Y" in the word "Z" | the only {ACCENT} one among identical grey ones | lit only by a narrow slit of light}, photographed as a premium still life on {BACKGROUND}, soft directional studio light, realistic materials and contact shadows; {ACCENT_HEX} appears only on {ELEMENT}.`
- **Quando usar:** serviço abstrato (consultoria, software, segurança,
  marketing), oferta que precisa de uma ideia em 1 segundo, anúncio.

### H · Cinema com contraponto tipográfico

**Assinatura:** fotografia de cinema ou de filme (paisagem, sala, plateia,
monocromia) em que a tipografia **conversa** com a cena: atravessa, é
engolida, orbita ou literaliza uma expressão.
**Refs:** MK01, MK02, MK08, MK09, MK14, MK19, MK21, MK22.

- **Tipografia:** troca de família no meio da frase (sans leve → serif
  itálica na palavra emocional; MK02, MK21); pilha de 3–4 vozes (MK01);
  palavra única gigante com frases pequenas em volta.
- **Núcleo de prompt:**
  `A cinematic {35mm film | anamorphic} photograph of {SCENE_THAT_LITERALIZES_THE_KEY_PHRASE}, {LIGHT}, {MONOCHROME_OR_PALETTE}; the composition leaves {ZONE} for a giant headline that {passes behind the subject's head | is partly swallowed by the landscape at its last line | is crossed by {OBJECT}}.`
- **Quando usar:** manifesto, posicionamento, capa de carrossel, post único
  de autoridade.

### I · Janela de interface sobre paisagem

**Assinatura:** paisagem ampla e calma (céu, campo, montanha, noite) com uma
janela de app ou site **real do cliente** flutuando no centro; nome ou marca
em grotesca grande acima; uma frase com trecho em bold abaixo; cabeçalho de
3 âncoras (data · autor · categoria) e paginação `BACK 01–08 NEXT` com seta
fina na base.
**Refs:** MK07, MK12, MK15, MK17, MK18, MK20, MK23, MK26.

- **Regra de produção:** a janela é **captura real** do produto aplicada em
  camada (Figma/HTML) com sombra suave; o gerador entrega só a paisagem com
  o centro calmo. Gerar a interface inventa letras e logos.
- **Núcleo de prompt (só a paisagem):**
  `A calm wide {LANDSCAPE} photograph, {TIME_OF_DAY} light, {SMALL_HUMAN_FOR_SCALE optional}; the central 70% of the width from 28% to 72% of the height is soft, low-detail {sky|field|water} for a floating app window added later; no text, no UI, no logos.`
- **Quando usar:** SaaS, app, portal do cliente, monitoramento remoto,
  agenda online, série de "ferramentas" ou "bastidores do sistema".

### J · Caderno editorial

**Assinatura:** folha de papel com textura (bege, linho, quadriculado,
fichário), título em serif condensada itálica terminado em **dois-pontos**,
parágrafo curto em itálico, 3 miniaturas em fila ligadas por setas
manuscritas no acento, rodapé `@handle · salvar · →`.
**Refs:** MK04, MK05, MK16, MK25.

- **Regra de produção:** a página e as setas podem ser geradas; miniaturas
  são fotos reais do cliente aplicadas em camada.
- **Quando usar:** passo a passo, bastidor de processo, "como funciona",
  estudo de caso, comparação.

Ao combinar G–J com A–F, mantenha **uma** luz, **uma** paleta e **um**
acabamento por série (`SKILL.md`, Famílias).

---

## R.2 Sistema tipográfico de contraste

Os movimentos que mais aparecem nas MK. Use no máximo **dois** por peça.

| Movimento | O que é | Refs | Frase de prompt |
|---|---|---|---|
| T1 Troca no meio da frase | a palavra emocional muda de sans para serif itálica (ou vice-versa) | MK02, MK21, MK24 | `"{FRASE}" in a light grotesque sans, with the word "{PALAVRA}" set in a large high-contrast serif italic` |
| T2 Escala extrema | uma palavra gigante (60–90% da largura) e o resto em corpo pequeno | MK02, MK12, MK15 | `the word "{X}" fills 85% of the width; all other lines are small` |
| T3 Marca-texto | bloco do acento atrás de 2–3 palavras | MK06, MK10, MK11 | `a flat {ACCENT_HEX} highlighter block sits behind "{TRECHO}"` |
| T4 Palavra-objeto | uma letra ou palavra substituída/atravessada por objeto real | MK02, MK11 | `the letter "{L}" is replaced by a realistic {OBJECT} at the same size` |
| T5 Pilha de vozes | 3–4 linhas, cada uma numa voz (condensada, serif itálica, numeral) | MK01 | ver `variacao-de-layout.md` L2 |
| T6 Engolida pela cena | a última linha some atrás do horizonte, da grama ou do sujeito | MK14, MK19 | ver `modelos-e-producao.md §10` (sanduíche) |
| T7 Âncoras e microrrótulos | texto pequeno só nas bordas (3 âncoras) ou espalhado em pontos da cena | MK03, MK13 | ver `microtipografia-editorial.md` |
| T8 Sublinhado editorial | parágrafo justificado com sublinhado fino | MK24 | aplicar em camada |

Famílias livres equivalentes: extensa pesada (Unbounded 800, Syne 800,
Archivo Expanded 800); grotesca compacta (Inter Tight 800, Manrope 800);
serif itálica de contraponto (Instrument Serif Italic, Playfair Display
Italic, DM Serif Display Italic); serif condensada editorial (Gloock, Bodoni
Moda Italic em corpo grande); sans leve (Inter 300). Acentos e hífens no
idioma final, sempre conferidos no QA.

---

## R.3 O salto: do repertório para uma ideia que só o cliente poderia ter

Siga os quatro passos **antes** dos três conceitos de `nichos-e-ideias.md
§N.4`; o resultado alimenta as alavancas 9–13 dessa seção.

1. **Verbo da referência.** Para cada MK escolhida, escreva o movimento em
   uma linha com um verbo, sem nomes de objetos: "transformar o material do
   ofício no resultado" (MK06), "literalizar a expressão do público" (MK14,
   MK21), "trocar uma letra pelo objeto" (MK11), "revelar só o essencial no
   escuro" (MK13).
2. **Inventário do cliente.** Liste, a partir do material e do briefing:
   10 objetos que só existem nesse trabalho; 5 expressões que o **público**
   usa para a dor (as palavras dele, não as do profissional); 3 interfaces
   ou documentos que o cliente usa (app, laudo, contrato, agenda, câmera).
3. **Busca fora do nicho.** Com ferramenta de busca disponível, procure
   peças premiadas ou de marcas líderes de **dois nichos vizinhos** e de
   uma linguagem de fora (cinema, sinalização, museu, embalagem, editorial
   de moda). Registre 3 achados com link e o verbo de cada um. São
   vocabulário de estudo: não baixe nem anexe ao gerador.
4. **Cruzamento.** Combine verbo × inventário em 6 ideias e reduza a 3
   (seguro, ousado, fora da curva). Cada uma passa por:
   - **2 segundos:** a ideia é entendida sem ler o subtítulo.
   - **Anti-réplica:** lado a lado com a MK de origem, não é a mesma cena.
   - **Assinatura:** trocando o logo por um concorrente, a peça perderia
     sentido. Se continuar servindo para qualquer marca, volte ao passo 2.

Registro no conceito (`nichos-e-ideias.md §N.4`):
`Movimento: MK11 (letra-objeto) · Achado externo: {link} · Inventário usado: {objeto}, {expressão}`.

---

## R.4 Como cada família muda por formato

| Formato | G · Objeto | H · Cinema | I · Janela | J · Caderno |
|---|---|---|---|---|
| Post único 4:5 | objeto central, frase em 2 linhas, assinatura no rodapé | foto inteira + título entrelaçado | 1 janela, 1 frase | página com 1 miniatura grande |
| Carrossel | capa G, miolo alterna H/J | capa H, miolo L1–L12 com a mesma foto-base | uma janela por slide com paginação 01–08 | a prancheta/página em no máximo 2–3 slides; o resto em outras escalas (R.5) |
| Story/Reels 9:16 | objeto no terço central | título no meio; topo e base livres | janela menor, centro | evitar: texto pequeno demais |
| Anúncio | o melhor: entende-se sem ler | bom para marca; teste com G | bom para app/SaaS | fraco em mídia paga |
| Slide 16:9 | objeto à direita, texto à esquerda | foto de fundo, título em L8 | janela grande à direita | pouco indicado |

Zonas, proporções e áreas da plataforma em `formatos-e-composicao.md §5.7`.

## R.5 Série com movimento (a família é o fio, não o molde)

Erro visto no caso de consultoria de segurança, carrossel em caderno: os 9
slides saíram com a mesma prancheta vista de cima, o mesmo bloco de texto
no topo e a mesma densidade de texto. O universo estava certo; a série
estava morta. Uma família define **luz, paleta, acento e materiais**; ela
não define cena, escala nem quantidade de texto. Regras para qualquer
carrossel:

1. **Um movimento por slide.** Cada slide nasce de uma MK diferente (ou de
   uma alavanca de `nichos-e-ideias.md §N.4`); dois slides seguidos nunca
   usam o mesmo movimento. Registre o movimento ao lado do prompt.
2. **O objeto-símbolo da família aparece em no máximo 1/3 dos slides**
   (prancheta, janela, papel, painel). Nos outros, mude a escala: foto em
   tela cheia, macro, página só de tipografia, objeto como herói, recorte de
   luz no escuro, folha de contato, mão em cena.
3. **Densidade de texto varia pelo papel do slide.** Em 9 slides, pelo
   menos 3 com até 6 palavras (manchete sozinha), 1 de respiro só
   tipográfico, no máximo 3 com parágrafo.
4. **O cabeçalho varia:** 3 âncoras (capa, falha numerada, checklist), 2
   âncoras, microrrótulos espalhados na cena (MK13) ou só o @. O @ continua
   no centro do topo em todos.
5. **Vozes tipográficas pelo papel** (`variacao-de-layout.md §V.3`): serif
   itálica nas frases de reflexão, extensa pesada nos golpes curtos, mono
   nos rótulos.
6. **Referência de continuidade só nos slides do mesmo cenário.** Foto em
   tela cheia de outro lugar vai sem a capa como `--ref`, senão o gerador
   copia a mesa.

Teste antes de entregar: ponha as 9 miniaturas lado a lado. Se três
seguidas parecem a mesma foto com outro texto, refaça o roteiro.
