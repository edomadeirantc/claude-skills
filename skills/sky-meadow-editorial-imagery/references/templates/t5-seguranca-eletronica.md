# T5 · Segurança eletrônica e consultoria de segurança

Para empresas de CFTV, alarme, monitoramento, controle de acesso e
consultoria de segurança patrimonial. Status: **prompts entregues, não
testados em rodada**. Famílias G (objeto), H (cinema), I (janela de
interface) e J (caderno, uma vez por série) de `../repertorio-mercado.md`;
regras do nicho em `../nichos-e-ideias.md §N.3 e §N.5`.

## SE.1 O problema do nicho

O feed do setor é medo genérico: ladrão encapuzado, cadeado, câmera em
fundo azul, "não seja a próxima vítima". Isso afasta o dono de empresa que
já tem equipamento e acha que está protegido, que é quem mais compra
consultoria. A ideia da série é mostrar **o que o equipamento não vê** e
**a rotina que o sistema guarda**, com tom técnico e calmo.

## SE.2 Bíblia de partida (ponto de partida, muda por marca)

Os valores abaixo são um ponto de partida para quando a marca não traz os
seus. Fundo, acento, tipografia e luz mudam pela marca do cliente. Câmera,
lente, altura e ângulo **não** entram na bíblia: vêm de cada linha do
storyboard (§SE.6, `../variacao-de-layout.md §V.5`).

```yaml
fundo: grafite quase preto (#111214) ou concreto claro de fachada (trocar pelo neutro da marca)
acento: a cor do logo do cliente, só em uma palavra, um objeto ou a interface
tipografia: extensa pesada (Unbounded 800 / Archivo Expanded 800) no título + mono (IBM Plex Mono) em rótulos técnicos tipo câmera (REC, CAM 03, 23:47)
luz: noite real da cidade (poste, vitrine, LED do equipamento) ou fim de tarde
pessoas: técnico com o uniforme real da empresa, dono do negócio; nunca criminoso
equipamento: só o do cliente (foto como --ref) ou genérico sem marca
camera: varia por slide (storyboard)
```

## SE.3 Arquétipos

| ID | Peça | Movimento | Núcleo |
|---|---|---|---|
| SE1 | Ponto cego | recorte de luz (MK13) + interface (colchetes de câmera) | a área que a câmera **não** cobre iluminada, o resto no escuro, com moldura de visor e "CAM 02 · SEM COBERTURA" em mono |
| SE2 | Um sem monitoramento | um se destaca (MK03) | fileira de fachadas/lojas à noite, todas com o LED verde de monitoramento, uma sem |
| SE3 | Letra-objeto | MK11 | palavra "SEGURO" ou "VISTO" com o "O" trocado por uma câmera dome real |
| SE4 | A rotina guardada | literalizar (MK21) | o dono baixando a porta de enrolar às 22h, visto pela câmera, timestamp em mono |
| SE5 | Central como janela | família I | paisagem noturna da cidade com a tela real do app de monitoramento do cliente em camada |
| SE6 | Diagnóstico | caderno J | página de laudo técnico com 3 fotos reais da vistoria e setas no acento |

## SE.4 Copy

- Título fala do **risco silencioso**, não do crime: "Câmera gravando não é
  câmera vendo." · "O ponto cego fica na porta dos fundos." · "Alarme sem
  resposta é só barulho."
- Rótulos técnicos em mono dão credibilidade: `REC ● 23:47:12`, `CAM 03`,
  `ZONA 2 · SEM SENSOR`.
- CTA de consultoria: "Comente DIAGNÓSTICO", "Peça a vistoria".
- Sem estatística sem fonte, sem "risco zero", sem cena de crime.

## SE.5 Prompts base

SE1 · ponto cego (post único ou capa; a câmera é a da linha 1 de §SE.6):

```text
A portrait 4:5 documentary night photograph for a security consultancy's Instagram post.
The back door of a small closed shop in an ordinary Brazilian street, seen from a high corner angle as if from a security camera; only a narrow cone of cold white light from a wall lamp reaches the door, everything else falls into deep graphite shadow (#111214).
Light: real urban night light, one sodium street lamp far away, the wall lamp as key; slight wet ground reflections; no people.
Camera: 24mm wide, high corner angle, deep focus, subtle surveillance-camera barrel distortion.
Composition: the door sits in the right 45% of the frame from 30% to 85% of the height; the upper 25% stays dark and calm for a headline added later.
Finish: shot on digital cinema camera, fine grain, true-to-life color, no neon, no teal-orange grading.
Do not include any text, logos, timestamps, UI, people or weapons.
```

SE3 · letra-objeto (slide 2 de §SE.6, em 4:5; para anúncio quadrado troque a primeira linha por "A square 1:1 premium still life"):

```text
A portrait 4:5 premium still life on a matte graphite background (#111214).
The word "VISTO" in very large extended heavy white letters, centered, where the letter "O" is replaced by a real white dome security camera of the same size, photographed with soft studio light and a realistic contact shadow.
{ACCENT_HEX} appears only as the small status LED on the camera.
Render only the exact text "VIST" plus the camera as the final letter; no other lettering, logos or watermarks.
```

Nos outros slides, monte o prompt pela família do slide em
`../repertorio-mercado.md §R.6`, com a câmera da linha correspondente.

## SE.6 Carrossel 9 slides

Exemplo de variação; não copie: pelo menos 6 de 9 linhas devem mudar de cena e de copy. Formato canônico de `../variacao-de-layout.md
§V.5`. Cada slide usa um movimento MK diferente e uma câmera diferente; a
página J aparece uma vez e a janela I uma vez. Troque cena, copy e paleta
pela marca e pelo conceito da rodada; mantenha só a regra de variação.

| # | papel | movimento (MK## + verbo) | escala/cena | câmera (lente · altura · ângulo) | layout L# | voz | nº palavras | cabeçalho | mesmo lugar da capa? (--ref sim/não) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | capa | SE1 · MK13 recortar com luz | porta dos fundos da loja fechada à noite, vista pela câmera | 24mm · canto alto do muro · plongée de câmera de segurança | L8 | display + mono nos rótulos | 6 | 3 âncoras (PONTO CEGO · @ · CAM 02) | é a capa (sem --ref) |
| 2 | stake | SE3 · MK11 trocar a letra pelo objeto | still life em estúdio grafite, câmera dome como a letra "O" | 85mm · altura do objeto · frontal | letra-objeto (estrutura própria da MK11, sem pilha L2) | display | 5 | só o @ | não |
| 3 | dor | SE4 · MK21 literalizar | plano médio: o dono baixando a porta de enrolar na frente da loja às 22h | 28mm · altura do olho, do outro lado da calçada · frontal | L3 | utilitária (mono) | 8 | @ no topo | não |
| 4 | como funciona | SE6 · J (MK16 caderno de processo) | página de laudo técnico sobre o balcão da loja, 3 fotos reais em camada | 35mm · de cima · top-down a 90° | L10 | utilitária (mono impressa no laudo) | 4 | rodapé J (@ · salvar · →) | não |
| 5 | respiro | TM2 escala extrema (só tipografia) | sem foto, fundo da série | sem câmera | L5 | display | 5 | só o @ | não |
| 6 | prova de rotina | SE2 · MK03 um se destaca | plano aberto: fileira de fachadas à noite, uma sem o LED de monitoramento | 50mm · do outro lado da rua, altura do olho · frontal com fachadas paralelas | L1 | display + contraponto | 7 | 2 âncoras (@ · RUA COMERCIAL) | não |
| 7 | virada | SE5 · família I (MK26 janela noturna) | a cidade de cima à noite, janela real do app em camada | 70mm teleobjetiva · alto de um prédio · plongée leve | janela I em camada | utilitária + display | 9 | 3 âncoras em camada (CENTRAL · @ · AO VIVO) | não |
| 8 | resumo | MK09 trilha de passos | detalhe: cabo em canaleta percorrendo a parede com 5 caixas de passagem como nós | 35mm · altura do peito · diagonal ao longo da parede | L11 | utilitária | 10 | 3 âncoras (CHECKLIST · @ · 5 PONTOS) | não |
| 9 | CTA | MK08 a palavra vira CTA | macro do LED de status desfocado atrás da palavra | 100mm macro · altura do LED · frontal | L12 | display | 5 | só o @ | não |

Conferência (regras de §V.5): nenhum movimento, câmera ou layout repete em
linhas seguidas; o objeto-símbolo (câmera dome/visor) aparece em 3 de 9
linhas (1, 2, 9); 5 linhas com até 6 palavras (1, 2, 4, 5, 9), 1 só
tipográfica (5); a explicação do laudo vai na legenda, porque o L10 aceita
no máximo 4 palavras; a capa (plongée de vigilância) e a dor (altura do olho)
não repetem câmera nem ideia de copy; nenhuma linha usa a capa como
`--ref`, porque nenhuma volta à porta dos fundos.

Copy de exemplo (não copie; troque pela da marca e do conceito):

1. "Câmera gravando não é câmera vendo."
2. "VISTO" (o "O" é a câmera) + "Gravar não é ver."
3. "22h04. A porta desce. O risco começa agora."
4. "PONTO CEGO: 3 ÂNGULOS" (impresso no laudo; o resto vai na legenda)
5. "Alarme sem resposta é barulho."
6. "Na sua rua, qual fachada ninguém monitora?"
7. "{Marca}" + "A central vê o alerta e alguém responde."
8. "O que a vistoria confere:" + "ângulo · cobertura · gravação · resposta · manutenção"
9. "Comente DIAGNÓSTICO" + "peça a vistoria"

Contador e paginação em camada (`../../scripts/kit_overlay.mjs`). Registre
a rodada no caso, seção `## Rodadas` (`README.md`).

Adaptadores para outros geradores: `../modelos-e-producao.md §9`.
