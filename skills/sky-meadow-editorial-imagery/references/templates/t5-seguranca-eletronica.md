# T5 · Segurança eletrônica e consultoria de segurança

Para empresas de CFTV, alarme, monitoramento, controle de acesso e
consultoria de segurança patrimonial. Status: **prompts entregues, não
testados em rodada**. Famílias G (objeto), H (cinema) e I (janela de
interface) de `../repertorio-mercado.md`; regras do nicho em
`../nichos-e-ideias.md §N.3 e §N.5`.

## S.1 O problema do nicho

O feed do setor é medo genérico: ladrão encapuzado, cadeado, câmera em
fundo azul, "não seja a próxima vítima". Isso afasta o dono de empresa que
já tem equipamento e acha que está protegido, que é quem mais compra
consultoria. A ideia da série é mostrar **o que o equipamento não vê** e
**a rotina que o sistema guarda**, com tom técnico e calmo.

## S.2 Bíblia padrão (ajuste pela marca)

```yaml
fundo: grafite quase preto (#111214) ou concreto claro de fachada
acento: a cor do logo do cliente, só em uma palavra, um objeto ou a interface
tipografia: extensa pesada (Unbounded 800 / Archivo Expanded 800) no título + mono (IBM Plex Mono) em rótulos técnicos tipo câmera (REC, CAM 03, 23:47)
luz: noite real da cidade (poste, vitrine, LED do equipamento) ou fim de tarde
pessoas: técnico com o uniforme real da empresa, dono do negócio; nunca criminoso
equipamento: só o do cliente (foto como --ref) ou genérico sem marca
```

## S.3 Arquétipos

| ID | Peça | Movimento | Núcleo |
|---|---|---|---|
| S1 | Ponto cego | recorte de luz (MK13) + interface (colchetes de câmera) | a área que a câmera **não** cobre iluminada, o resto no escuro, com moldura de visor e "CAM 02 · SEM COBERTURA" em mono |
| S2 | Um sem monitoramento | um se destaca (MK03) | fileira de fachadas/lojas à noite, todas com o LED verde de monitoramento, uma sem |
| S3 | Letra-objeto | MK11 | palavra "SEGURO" ou "VISTO" com o "O" trocado por uma câmera dome real |
| S4 | A rotina guardada | literalizar (MK21) | o dono baixando a porta de enrolar às 22h, visto pela câmera, timestamp em mono |
| S5 | Central como janela | família I | paisagem noturna da cidade com a tela real do app de monitoramento do cliente em camada |
| S6 | Diagnóstico | caderno J | página de laudo técnico com 3 fotos reais da vistoria e setas no acento |

## S.4 Copy

- Título fala do **risco silencioso**, não do crime: "Câmera gravando não é
  câmera vendo." · "O ponto cego fica na porta dos fundos." · "Alarme sem
  resposta é só barulho."
- Rótulos técnicos em mono dão credibilidade: `REC ● 23:47:12`, `CAM 03`,
  `ZONA 2 · SEM SENSOR`.
- CTA de consultoria: "Comente DIAGNÓSTICO", "Peça a vistoria".
- Sem estatística sem fonte, sem "risco zero", sem cena de crime.

## S.5 Prompts base

S1 · ponto cego (post único ou capa):

```text
A portrait 4:5 cinematic night photograph for a security consultancy's Instagram post.
The back door of a small closed shop in an ordinary Brazilian street, seen from a high corner angle as if from a security camera; only a narrow cone of cold white light from a wall lamp reaches the door, everything else falls into deep graphite shadow (#111214).
Light: real urban night light, one sodium street lamp far away, the wall lamp as key; slight wet ground reflections; no people.
Camera: 24mm wide, high corner angle, deep focus, subtle surveillance-camera barrel distortion.
Composition: the door sits in the right 45% of the frame from 30% to 85% of the height; the upper 25% stays dark and calm for a headline added later.
Finish: shot on digital cinema camera, fine grain, true-to-life color, no neon, no teal-orange grading.
Do not include any text, logos, timestamps, UI, people or weapons.
```

S3 · letra-objeto (anúncio):

```text
A square 1:1 premium still life on a matte graphite background (#111214).
The word "VISTO" in very large extended heavy white letters, centered, where the letter "O" is replaced by a real white dome security camera of the same size, photographed with soft studio light and a realistic contact shadow.
{ACCENT_HEX} appears only as the small status LED on the camera.
Render only the exact text "VIST" plus the camera as the final letter; no other lettering, logos or watermarks.
```

Adaptadores para outros geradores: `../modelos-e-producao.md §9`.
