# T4 · Clínica premium em fundo preto (Família K)

Estrutura visual aprovada por uma cliente real (cirurgiã-dentista com HOF).
Estrutura medida em artes locais da cliente; os valores já estão transcritos
abaixo e não é preciso abrir as artes. O material da cliente (`clientes/`,
RC) só é lido quando o usuário nomeia a cliente no chat; pedido de clínica
sem esse nome usa só este template. O que foi aprovado é a **estrutura**:
fundo preto, contorno fino desenhado no perfil, dourado discreto e a
profissional sentada de terno claro como imagem de autoridade. O card claro
com preço foi **retirado pelo usuário na curadoria de 25/10/2026** e não é
modelo. O **texto** das peças também não é modelo (K.2). Serve para
qualquer clínica ou profissional premium: HOF, odontologia, dermatologia,
estética, cirurgia plástica, nutrologia.

Regras legais por conselho em `../nichos-e-ideias.md §N.3` (linhas médico e
cirurgião-dentista). Em caso de dúvida, a peça sai sem o elemento e com nota
"conferir com o conselho".

Procedimento dentro da competência do conselho? Lipo/lipoplastia de papada
por cirurgião-dentista está em disputa CFO × CFM (Res. CFO 198/2019 e
230/2020; parecer CREMESP 2026 contrário à lipoaspiração de papada por
dentista): a peça não usa termo cirúrgico (lipoaspiração), descreve o método
real informado pela cliente e pede revisão jurídica; nunca afirma que é
permitido.

---

## K.1 Estrutura aprovada (o que fica fixo)

Medidas sobre 1080×1350; cores amostradas por mediana de área nas artes da
cliente (valores transcritos na tabela; não abrir as artes).

| Elemento | Posição (altura) | Especificação |
|---|---|---|
| Fundo | inteiro | preto puro `#000000` (antes/depois) ou preto quente `#0B0B08` (retrato, tipografia) |
| Topo | 3–6% | @ da profissional no centro do topo, com a mesma grafia e o mesmo tamanho em toda a série; logo real em camada à esquerda, se couber; rótulo opcional em caixa-alta espaçada dourado `#B8A67C` à direita |
| Título | conforme o layout | serif de alto contraste (Playfair Display 700, Libre Caslon Display, Bodoni Moda 700), branco, com uma palavra em itálico dourado (TM1 é o padrão da K; outro TM de `../repertorio-mercado.md §R.2` é permitido quando o movimento da peça pedir) |
| Antes/depois | 4–92% | dois painéis lado a lado, rótulos ANTES/DEPOIS em sans espaçada branca acima, contorno fino branco desenhando o perfil no painel "depois", logo pequeno no canto do "depois", "RESULTADO REAL" centrado na base |
| Identificação | 92–95% | nome + conselho no rodapé: `Dra. {Nome} · CD · CRO-{UF} {nº}` em sans pequena cinza |

Card de oferta é opcional e **não aprovado**: se usar, é claro, sem preço
(dentista) e nunca repetido em série.

Tudo isso é **camada de design** (Figma/HTML), não pedido ao gerador: logo,
números, CRO/CRM, rótulos e fotos de pacientes. O gerador entra só nos
retratos da profissional, nas cenas conceituais e nas texturas.

## K.2 O que estava genérico (não repetir)

Observado nas 33 peças da cliente:

- **Título que é só o nome do procedimento** ("LIPO SCULPT", "PAPADA +
  FIRMEZA"): é rótulo, não ideia; não diz nada que o paciente sinta.
- **A mesma frase em todas as peças** ("Um novo olhar para o perfil", "Cada
  detalhe conta", "O primeiro passo é a avaliação", "Agende sua
  avaliação"): 11 variações de "Paciente modelo R$ X" com o mesmo layout
  cansam o feed e não acrescentam prova nova.
- **Preço e escassez no card** ("R$ 1.350", "10 vagas", "edição limitada"):
  para cirurgião-dentista, preço em publicidade é infração (art. 44, I);
  vagas só se forem reais e verificáveis.
- **Paciente identificável** (rosto inteiro, olhos, cabelo) quando a regra
  permite só a área tratada; falta nome + CRO + "CD" na peça.
- **Rosto da profissional diferente entre séries**: o retrato gerado de uma
  série não bate com o da outra. Toda peça com a profissional usa a foto
  real dela como `--ref` e a ficha de personagem (`../realismo-fotografico.md §R.10`).

O que estava bom e fica: a cadeira e o terno claro como assinatura de
autoridade; o contorno desenhado sobre o perfil; o preto puro do
antes/depois; o dourado discreto só no logo e em uma palavra.

## K.3 Copy: como sair do genérico

- **Título = a frase do paciente ou o critério técnico traduzido**, 3–7
  palavras, sem promessa. Ex.: "O perfil que você evita nas fotos." ·
  "Contorno é proporção, não só volume." · "Antes de tirar, avaliar a pele."
  · "Seu ângulo favorito tem um motivo."
- **Troca de família na palavra emocional** (`../repertorio-mercado.md §R.2`):
  padrão TM1, título serif branco com uma palavra em serif itálica dourada;
  outro TM quando o movimento da peça pedir.
- **Subtítulo educativo** (exigência do CFM para antes/depois e boa
  prática no CFO): indicação, fator que muda o resultado, tempo entre as
  fotos. Em post único e anúncio (limite de 12 palavras na peça,
  `../formatos-e-composicao.md`), a educação pode ir para a legenda; a
  identificação do rodapé não conta no limite.
- **Card sem preço:** coluna 1 = "Avaliação individual" + o que é avaliado
  (pele, volume, proporção); coluna 2 = CTA ("Falar no direct", "Agendar
  avaliação"). Médico pode pôr valor de consulta (CFM 2.336/2023); dentista não.
- **Identificação obrigatória** no rodapé: `Dra. {Nome} · CD · CRO-{UF} {nº}`
  (ou `· MÉDICA · CRM-{UF} {nº} · RQE {nº}`).
- Sem "melhor", "único", "garantido", "sem dor", "resultado imediato".

## K.4 Arquétipos de peça

| ID | Peça | Como fazer | Gerador? |
|---|---|---|---|
| K1 | Card de caso (opcional, não aprovado) | foto real e card claro sem preço; no máximo 1 por série | não (camada) |
| K2 | Antes/depois | dois painéis, mesma pose e luz, recortados na área tratada, TCLE arquivado | **nunca** gerar ou retocar |
| K3 | Retrato de autoridade no preto | profissional real em recorte de luz (MK13), título serif à esquerda | sim, com foto real como `--ref` |
| K4 | Ideia conceitual | alavancas 9–13 (`../nichos-e-ideias.md §N.4`) sem paciente: a luz rasante desenhando um perfil de escultura, a régua de proporção dourada, o espelho de mão no preto | sim |
| K5 | Manifesto tipográfico | só tipografia no preto, pilha TM5 com uma palavra dourada | não (camada) ou gerador com lista fechada |
| K6 | Fechamento | preto, título curto, botão de contorno dourado, identificação | camada |

Carrossel: K3 (capa) → K4 (stake) → K1 ou K2 (prova, uma só) → K5 (critério)
→ K6, com um movimento e uma câmera diferentes por slide no storyboard de
`../variacao-de-layout.md §V.5`. Post único: K3 ou K4. Anúncio: K4
(entende-se sem texto) com título curto e identificação; sem card K1.

## K.5 Prompts base

K3 · retrato de autoridade (IMAGE 1 = foto real da profissional; preserva a aparência geral, sem alterar traços):

```text
A portrait 4:5 editorial photograph for a premium clinic's Instagram post. Reference image 1 shows the real dental surgeon: keep her general look, hair, skin tone and age; do not change or beautify any feature.
She sits upright in a cream armchair in a light {beige|ivory} tailored suit, hands resting naturally, calm direct gaze, a slight closed-mouth smile.
Setting: a dark room that falls into pure warm black (#0B0B08); no visible walls, no marble, no gold props.
Light: a single soft window light from camera-left, narrow and directional, so only her face, hands and the front of the suit are lit and the rest falls to black (low-key, chiaroscuro); natural skin texture with pores and fine lines, no glow.
Camera: 85mm f/2.8, eye level, she occupies the right 55% of the frame from 18% to 96% of the height.
Composition: the left 40% of the width from 6% to 60% of the height is pure black for a serif headline added later.
Do not include any text, logos, frames, borders or UI.
```

K4 · ideia conceitual (sem pessoa real). Exemplo de variação; não copie:
escolha uma das 3 sementes abaixo (ou crie outra a partir do conceito da
rodada) e monte o prompt pela família G de `../repertorio-mercado.md §R.6`,
com a câmera da linha do storyboard. Nunca reuse a mesma semente em duas
séries seguidas.

1. **Luz rasante:** um objeto da área tratada (escultura, molde, tecido)
   em perfil, só uma linha de luz desenhando o contorno no preto.
2. **Espelho de mão:** um espelho de mão no preto refletindo só uma faixa
   de luz, sem rosto; a pergunta do paciente no título.
3. **Fotografia evitada:** uma foto de família impressa, virada para baixo
   sobre uma mesa escura, um canto levantado pela luz.

Base fixa de qualquer semente: `A portrait 4:5 fine-art still life on a pure
warm black background (#0B0B08)`, zona de título preta à esquerda, `Do not
include any text, logos, frames, people or medical instruments.`

Adaptadores para outros geradores: `../modelos-e-producao.md §9`.

## K.6 QA específico

- [ ] Nenhum preço em peça de cirurgião-dentista; valor de consulta só em peça de médico.
- [ ] Antes/depois: fotos reais, mesma pose e luz, recortadas na área, TCLE confirmado com a cliente; nada gerado ou retocado.
- [ ] Nome + conselho + número em toda peça.
- [ ] Rosto da profissional idêntico à foto real (comparar lado a lado).
- [ ] Título não é só o nome do procedimento e não se repete na série.
- [ ] Dourado só em linha, rótulo e uma palavra; nada de brilho dourado na cena.
