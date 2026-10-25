# Protocolo de teste

Como avaliar as próximas rodadas da skill e onde registrar o resultado. Vale
para qualquer gerador. Cada teste roda o fluxo completo: brief, salto + 3
conceitos, família derivada do conceito, storyboard
(`variacao-de-layout.md §V.5`), copy, prompts, autochecagem e geração.

## 1. Rubrica (0 a 2 por critério)

| # | Critério | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | Ideia em 2 s | não se entende sem ler o subtítulo | entende-se lendo o título | a imagem sozinha diz a ideia |
| 2 | Variação da série | 3 ou mais slides seguidos parecem a mesma foto com outro texto | movimento ou câmera repete em slides seguidos | movimento, escala, câmera e densidade mudam a cada slide |
| 3 | Assinatura do cliente | serve para qualquer marca do nicho | serve para 2 ou 3 concorrentes | com o logo de um concorrente, a peça perde sentido |
| 4 | Contraste tipográfico do movimento | uma voz só, ou itálico decorativo sem motivo | contraste presente, mas não é o do movimento escolhido | o contraste é o movimento TM do slide (`repertorio-mercado.md §R.2`), no máximo dois por peça |
| 5 | Realismo | cara de banco de imagem ou de render (`realismo-fotografico.md §R.8`) | um defeito visível (pele, mãos, lugar genérico) | passa no §R.8 sem ressalva |
| 6 | Texto e legal exatos | texto errado, inventado ou regra do conselho violada | um erro de acento, hífen ou posição | texto igual à lista fechada e regras do nicho cumpridas |

**Passa** com 9/12 ou mais e nenhum 0 nos critérios 1 e 2.

Peça única (post, anúncio, slide): o critério 2 avalia as entregas do mesmo
pedido entre si. Post e anúncio, ou o slide e os vizinhos do deck, não podem
ser o mesmo recorte com outro texto.

## 2. Checagens que todo teste repete antes de gerar

1. Storyboard com uma linha por slide nas colunas de §V.5, e as regras de
   §V.5 conferidas.
2. Linhas `Camera:` distintas em pelo menos metade dos prompts (arredonde
   para cima); nenhuma câmera na bíblia da série.
3. Busca nos prompts por `cerulean|grassy hill|35mm f/2 at eye level|identity|same face|match the reference exactly`:
   cada ocorrência justificada ou removida.
4. Cada prompt tem o movimento numa linha de comentário fora do texto do
   prompt.
5. Anti-réplica contra todas as R/N/IG/MK citadas: a cena não é a da
   referência.
6. Contador, paginação e números em camada, nunca no prompt.

## 3. Briefs dos próximos testes

### A · Carrossel de 9 slides, segurança eletrônica genérica

Brief: "Carrossel de 9 slides para uma empresa de monitoramento e CFTV de
bairro. Objetivo: comentários pedindo diagnóstico. Sem nome de cliente, sem
logo; acento e @ fictícios." Partida: `templates/t5-seguranca-eletronica.md
§SE.6`.

Checagens esperadas:
- 9 linhas no storyboard, cada uma com um MK diferente; nenhum movimento,
  câmera ou layout repetido em linhas seguidas.
- Página J em no máximo 1 slide, janela I em no máximo 1 slide; o
  objeto-símbolo (câmera ou visor) em no máximo 3 slides.
- Pelo menos 3 slides com até 6 palavras, 1 só tipográfico, no máximo 3 com
  parágrafo.
- @ em todos os slides com a mesma grafia e o mesmo tamanho; cabeçalho
  variando entre 3 âncoras, 2 âncoras, microrrótulos e só o @.
- `--ref` da capa só em slide no mesmo lugar da capa.
- Sem cena de crime, sem estatística sem fonte, sem "risco zero".
- Falha a evitar: os 9 slides com a mesma prancheta vista de cima
  (`repertorio-mercado.md §R.5`).

### B · Post único + anúncio 4:5 para clínica HOF, sem nome de cliente

Brief: "Post único e anúncio 4:5 para uma clínica de harmonização orofacial
de cirurgiã-dentista. Público: mulheres de 35 a 55 anos. Objetivo: agendar
avaliação." Nenhum nome de cliente no chat.

Checagens esperadas:
- O agente **não** lista, procura nem abre `clientes/`; não cita RC, nomes
  reais, logo ou cores de cliente. Usa só
  `templates/t4-clinica-premium-fundo-preto.md` e o acervo geral.
- 3 conceitos com movimentos MK antes da família; família K confirmada na
  rodada 2, junto do conceito.
- Sem preço, gratuidade ou forma de pagamento (cirurgiã-dentista);
  identificação `Dra. {Nome} · CD · CRO-{UF} {nº}` em camada.
- Nenhum antes/depois gerado ou retocado.
- Título não é nome de procedimento; itálico só como movimento TM1.
- O anúncio se entende sem ler (K4) e não é o mesmo recorte do post.

### C · Carrossel de 6 slides para nicho novo (padaria artesanal)

Brief: "Carrossel de 6 slides para uma padaria artesanal de fermentação
natural. Objetivo: salvar o post." O nicho não está em
`nichos-e-ideias.md §N.3`: o caminho é só o salto + MK.

Checagens esperadas:
- Salto de `repertorio-mercado.md §R.3` registrado: verbos das MK,
  inventário (10 objetos, 5 expressões do público, 3 interfaces ou
  documentos), 3 achados externos com link quando houver busca, 6 ideias
  reduzidas a 3.
- Cada conceito cita MK + verbo; a família vem depois do conceito.
- Procedimento de nicho novo de `nichos-e-ideias.md §N.5`: 5 itens que só
  quem trabalha lá conhece e 2 sinais leves de uso.
- Sem paleta da Família A (céu cerúleo, grama, lime) e sem monumento na
  colina, salvo pedido da marca.
- Storyboard de 6 linhas cumprindo §V.5.

### D · Slide 16:9 de pitch

Brief: "Um slide 16:9 de pitch para uma startup de logística de entregas
locais: o slide do problema." Formato e regras de
`templates/t2-pitch-deck-16x9.md`.

Checagens esperadas:
- 1920×1080; uma ideia; dados e número da página em camada, nunca no
  prompt.
- Composição pela linha "Slide 16:9" de `repertorio-mercado.md §R.4`
  (objeto à direita e texto à esquerda, foto de fundo com título em L8 ou
  janela grande à direita).
- Câmera vinda da linha do storyboard, mesmo com um slide só.
- Nenhum número sem fonte; sem `identity` nem `same face`.

## 4. Registro da rodada

Cada rodada vai para `templates/casos/{caso}.md`, na seção `## Rodadas`.
Teste sem caso existente cria o arquivo: `teste-a-seguranca-carrossel.md`,
`teste-b-clinica-hof.md`, `teste-c-padaria-carrossel.md`,
`teste-d-pitch-slide.md`. Não salve imagens no pacote.

```
## Rodadas

| data | gerador | MK por slide | nota da rubrica | falha principal | correção na skill |
|---|---|---|---|---|---|
| AAAA-MM-DD | {gerador e versão} | 1 MK13 · 2 MK11 · 3 MK21 · … | 10/12 (2·2·1·2·2·1) | {o que falhou, em uma frase} | {arquivo §seção alterado, ou "nenhuma"} |
```

A nota lista os seis critérios na ordem da rubrica. Uma falha com 0 nos
critérios 1 ou 2 sempre gera uma correção na skill antes da próxima rodada.
