---
name: ig-carousel-pipeline
description: >-
  Carrossel de Instagram do zero ao post pronto, numa linha de produção só:
  pesquisa de referências virais, roteiro slide a slide, arte 1080x1350 em PNG,
  revisão anti-IA e legenda com hashtags. Use quando pedirem "carrossel",
  "carousel", "post em slides", "transforma isso em carrossel" ou um post de
  Instagram com passos, lista ou antes/depois.
---

# ig-carousel-pipeline

Cinco etapas, sempre nesta ordem, cada uma com um critério de pronto:

```
0 briefing → 1 pesquisa → 2 roteiro → 3 visual → 4 revisão anti-IA → 5 legenda
```

Tudo o que roda está nesta pasta (chamada aqui de `$SKILL`): os scripts em
`$SKILL/scripts/` e o modelo de slides em `$SKILL/assets/template.html`. No
Windows use `python`; em outros sistemas, `python3`. Os scripts de render
precisam do Playwright (`pip install playwright`).

Nada é publicado, curtido, seguido ou enviado por esta skill. O usuário posta.

## Etapa 0: briefing

Pergunte tudo de uma vez:

1. Ideia ou tema, e o material de origem, se houver
2. Público
3. @handle
4. A **única** ação que o post pede: salvar, comentar uma palavra-chave ou seguir
5. Marca: cores e fontes, ou a skill de marca/design system do projeto
6. 2 ou 3 termos que a pessoa digitaria na busca para achar esse post
7. Idioma (padrão: português do Brasil)

Carrossel serve para ideias com **sequência e que pedem releitura**: passos,
framework com partes, antes e depois, lista que vale print. Se a ideia é uma
afirmação só, ou depende de movimento ou de rosto, diga isso e sugira um Reel.

**Pronto quando:** os sete itens têm resposta ou um padrão que você declarou.

## Etapa 1: pesquisa (ig-viral)

Objetivo: três opções de capa apoiadas em evidência, não em achismo.

**Visualização bruta não prova nada.** Ordene pelo **múltiplo de outlier**:
métrica do post dividida pela mediana do próprio perfil. Acima de 3x é sinal;
abaixo de 1,5x é o dia normal da conta. Carrossel não mostra visualizações em
público, então use curtidas (ou comentários) e a mediana das últimas 12
publicações. Diga no relatório qual métrica usou.

Contas: de 6 a 12, sendo 4 diretas (mesmo nicho, um pouco à frente), 4
adjacentes (outro nicho, mesmo público) e de 2 a 4 bem maiores, só para
formato. Prefira contas com até 10x o tamanho da do usuário. Peça também a
coleção **Salvos** do usuário.

Regras fixas:

- O usuário já está logado no navegador dele. Você lê junto com ele ou ele cola
  os dados. Nunca peça senha nem faça login por ele.
- É leitura em ritmo humano: umas dez contas, uma dúzia de posts cada. Coleta
  automatizada em volume viola os Termos do Instagram e bloqueia contas.
- Copie a **fórmula** (forma do gancho, estrutura, número de slides), nunca o
  texto ou a arte. Atribua cada linha à conta de origem.

Monte um TSV com cabeçalho, e o texto da capa vai literal na coluna `hook`:

```
account	followers	median	views	hook
@conta	48000	900	6100	ninguém te conta que os primeiros 20 orçamentos são pra perder
```

```bash
python $SKILL/scripts/swipe.py captured.tsv --out ~/.claude/instagram/swipe.md
```

O classificador de fórmulas usa regex em inglês, então ganchos em português
saem como `unclassified`. Classifique esses à mão, usando os nomes das 26
fórmulas de `$SKILL/scripts/hooks.json`. Relate três coisas: as fórmulas que
mais aparecem no terço de cima (com contagem), o que esse terço tem em comum
na estrutura e o que não foi classificado. Depois diga o tamanho da amostra e
a confiança em palavras simples: 40 posts de 6 contas sustentam uma conclusão,
12 não.

**Pronto quando:** `swipe.md` foi escrito e há três capas na versão do usuário
(com a história e o número dele, no formato que está funcionando). Se o usuário
pular a pesquisa, diga que as capas vão sair das fórmulas sem evidência e siga.

## Etapa 2: roteiro (ig-carousel)

São de 6 a 10 slides. Com menos de 5 o deslize nem começa, e 20 vira um livro
que ninguém termina.

```
1        CAPA       gancho com até 6 palavras, legível na miniatura do grid,
                    e uma linha de promessa embaixo
2        STAKE      por que importa, numa frase. Também é uma segunda capa: o
                    Instagram pode reexibir o carrossel a partir do slide 2
3..N     UMA IDEIA  título de 3 a 7 palavras e no máximo 25 palavras embaixo.
                    Se precisar de parágrafo, são dois slides
N+1      RESUMO     a lista inteira, legível sem contexto: é o slide do print
ÚLTIMO   CTA        uma ação só, a mesma do briefing
```

- A capa responde por 80% do resultado. Escolha uma das três da etapa 1.
- Palavra-chave de comentário: uma palavra, sem espaço nem emoji, em
  maiúsculas (`Comente CONTRATO`).

Mostre o roteiro como lista numerada, que se lê em dez segundos:

```
CARROSSEL  ·  8 slides
1  CAPA    A CLÁUSULA DE R$ 18 MIL
           Uma linha que agora vai em todo contrato meu.
2  STAKE   Aprovei o trabalho. Nove dias depois, pediram o dinheiro de volta.
...
7  RESUMO  As quatro linhas, em ordem.
8  CTA     Comente CONTRATO e eu te mando a cláusula completa.
```

**Pronto quando:** o usuário aprovou o texto de cada slide. Nada é renderizado
antes disso.

## Etapa 3: visual (assinatura do card-xiaohongshu no formato do Instagram)

Copie `$SKILL/assets/template.html` para a pasta de trabalho como `deck.html`.
Cada slide é uma `<section class="slide">`, e o tipo vai na classe: `cover`,
`stake`, `idea`, `recap` ou `cta`. Troque só as variáveis do `:root`. Se o
projeto tiver marca ou design system, as cores e as fontes dele valem mais que
as do modelo.

- **Formato:** 1080x1350 (4:5). Não use o 3:4 do Xiaohongshu.
- **Zona segura:** 120 px livres em cada borda, porque o grid do perfil corta
  as laterais.
- **Tipografia:** nada menor que 32 px, porque o slide é lido no celular a um
  terço do tamanho real. Use um acento de cor só.
- **Assinatura visual:** capa com título enorme, uma linha de apoio e uma
  pílula ("Salve para depois"); cartões arredondados; bastante respiro; paleta
  suave. Ícones e emojis são decorativos e levam `aria-hidden="true"`, assim
  ficam fora da revisão de texto.
- O @handle aparece em todos os slides (o modelo já faz isso pela variável
  `--handle`) e a numeração 2/8 aparece do slide 2 em diante.
- Se um slide pedir foto ou ilustração, gere com a skill `imagegen`, salve na
  pasta e use caminho relativo. Placeholder não entra no carrossel.

```bash
python $SKILL/scripts/render.py deck.html --out slides/
```

Abra os PNGs e olhe cada um. O render avisa sobre tamanho errado e texto
cortado.

**Pronto quando:** existe um PNG por slide, o render não deu nenhum aviso e
você olhou cada imagem.

## Etapa 4: revisão anti-IA (ig-human)

Esta etapa roda sobre o texto dos slides e termina gerando os PNGs de novo.

```bash
python $SKILL/scripts/render.py deck.html --text deck.txt
python $SKILL/scripts/humanize.py deck.txt -o clean.txt --report
python $SKILL/scripts/detect.py deck.txt clean.txt --lang pt
```

1. O `humanize.py` remove caracteres invisíveis, troca travessão por vírgula e
   aspas curvas por retas, e substitui os clichês do `slop.json`, que tem um
   bloco `pt-br` ("no mundo atual", "alavancar", "marque alguém que precisa ver
   isso").
2. As **estruturas** marcadas no relatório você reescreve à mão, mantendo o
   sentido: "não é só X, é Y", pergunta retórica de uma linha ("O resultado?"),
   tríades, lista com emoji, isca de engajamento. Leve as correções para o
   `deck.html`.
3. O `detect.py` dá nota de 0 a 100 em cinco checagens. Para PASS, a média
   precisa ser 70 ou mais e nenhuma checagem pode ficar abaixo de 55. Se não
   der PASS, corrija a checagem mais fraca e rode de novo. Duas rodadas são
   normais. Se chegar a cinco, o texto foi escrito por fórmula e precisa ser
   reescrito.
4. Gere os PNGs de novo a partir do `deck.html` revisado.

Seja honesto com o usuário: são heurísticas locais, parecidas com os sinais
que os detectores públicos medem. Não são GPTZero nem Originality, e nunca
diga que o texto é "indetectável". Mostre o texto limpo junto com a nota,
nunca a nota sozinha.

**Pronto quando:** o veredito é PASS (ou o usuário aceitou REVIEW sabendo qual
checagem ficou fraca) e os PNGs finais saíram do texto revisado.

## Etapa 5: legenda (ig-caption)

No carrossel, a legenda faz o **Job B**: a capa já gastou as seis palavras
dela, então a linha 1 da legenda é um gancho novo.

```
Linha 1    até 125 caracteres visíveis antes do "... mais": concreta, curta,
           termina num corte, não no meio da frase. Sem saudação e sem hashtag
           ou emoji como primeiro caractere
Corpo      de 2 a 6 parágrafos curtos, separados por linha em branco. Os
           termos de busca entram aqui como frase que alguém digitaria
Pedido     um só, o mesmo do slide de CTA
Hashtags   até 5, específicas, sozinhas no fim (o Instagram limitou a 5 em
           dezembro de 2025). #viral, #fyp e #explorepage não descrevem nada
```

Link na legenda não é clicável: vai na bio ou na DM. Escreva também o **alt
text** da capa, no mínimo, porque leitores de tela e o próprio Instagram usam
esse texto.

```bash
python $SKILL/scripts/humanize.py caption.txt -o caption.txt --report
python $SKILL/scripts/detect.py caption.txt --lang pt
python $SKILL/scripts/caption.py caption.txt --keywords "termo 1,termo 2"
```

Corrija todo FAIL do linter. Cada WARN você decide em voz alta, não em
silêncio.

**Pronto quando:** o linter diz READY e o humanizer diz PASS.

## Entrega

```
slides/slide-01.png … slide-NN.png   ordem de upload
caption.txt                          legenda pronta para colar
alt-text.txt                         alt text por slide (no mínimo, a capa)
deck.html                            fonte editável
~/.claude/instagram/swipe.md         pesquisa (se feita)

CARROSSEL PRONTO
slides:     8 · 1080x1350 · render sem avisos
capa:       fórmula #3 Nobody Tells You (6,2x no swipe)
anti-IA:    PASS 78 (slides) · PASS 74 (legenda)
legenda:    Job B · 118/125 visíveis · 1 pedido (comente CONTRATO) · 3 hashtags
busca:      "contrato de freelancer" na linha 3
```

## Créditos

As etapas 1, 2, 4 e 5 e os scripts `swipe.py`, `hookscore.py`, `hooks.json`,
`humanize.py`, `detect.py`, `slop.json` e `caption.py` foram adaptados de
[instagram-agent-skill](https://github.com/Jakeschincariol/instagram-agent-skill),
de Jake Schincariol (MIT, veja `LICENSE`). As adaptações foram: bloco `pt-br`
no léxico, `--lang pt` no `detect.py`, pedidos e hashtags em português no
`caption.py` e caminhos locais no `swipe.py`. A assinatura visual da etapa 3
vem do template card-xiaohongshu de
[html-anything](https://github.com/nexu-io/html-anything) (Apache-2.0).
O `render.py` e o `template.html` foram escritos para esta skill.
