# Formatos, zonas seguras, séries e camada gráfica

## 5. Formatos e zonas seguras

Gere **cada formato na proporção nativa**. Recortar muda o enquadramento,
e o espaço negativo deixa de estar onde o texto vai ficar.

| Uso | Proporção | Geração (`--size`) | Entrega |
|---|---|---|---|
| Hero desktop | 16:9 | 4K | 2560×1440, 1920×1080, 1280×720 |
| Hero desktop ultra-wide | 21:9 | 4K | 3440×1474 (ou corte do 21:9) |
| Hero mobile | 9:16 | 2K | 1080×1920, 750×1334 |
| Hero mobile compacto / feed | 4:5 | 2K | 1080×1350 |
| Carrossel Instagram/LinkedIn | 4:5 | 2K | 1080×1350 por slide |
| Carrossel quadrado | 1:1 | 2K | 1080×1080 |
| Story / Reels capa | 9:16 | 2K | 1080×1920 |
| Panorama de carrossel | 21:9 ou 16:9 | 4K | fatiado (§7.3) |

### 5.1 Hero desktop 16:9 — layout centralizado (padrão das referências)

```
┌────────────────────────────────────────────────────────┐ 0%
│  margem (nav sobreposta) — céu liso                    │
│ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─│ 10%
│              ZONA DO TÍTULO (céu profundo,             │
│              sem nuvens) 15–45% da altura,             │
│              25–75% da largura                         │
│ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─│ 45%
│                    ▲ topo do sujeito pode invadir      │
│                 [ SUJEITO / OBJETO ]  45–85%           │
│   nuvens só nas     centro: 40–60% da largura          │
│   laterais                                             │
│▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ colina/campo ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│ 70%+
│▓▓▓▓▓▓▓▓▓▓ grama em sombra (CTA claro aqui) ▓▓▓▓▓▓▓▓▓▓▓▓│ 100%
└────────────────────────────────────────────────────────┘
```

Frase de prompt: `Leave the band between 15% and 45% of the frame height, across the central half of the width, as clean uninterrupted deep blue sky reserved for a headline. Place the subject centered horizontally, its top reaching about 45% of the frame height, its base at about 80%.`

### 5.2 Hero desktop 16:9 — layout texto à esquerda

```
┌───────────────────────────┬────────────────────────────┐
│  ZONA DE TEXTO            │                            │
│  8–48% da largura         │      [ SUJEITO ]           │
│  20–75% da altura         │      terço direito         │
│  céu liso, sem nuvens     │      58–88% da largura     │
│                           │      nuvens permitidas     │
│▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ horizonte/colina em 70–78% ▓▓▓▓▓▓▓▓▓▓▓▓▓│
└───────────────────────────┴────────────────────────────┘
```

Frase: `Keep the left 48% of the frame as calm open sky with no clouds and no objects, reserved for text. Place the subject in the right third, centered around 72% of the width.`

### 5.3 Hero mobile 9:16

```
┌──────────────────┐ 0%
│ status/nav  (8%) │
│ ZONA DO TÍTULO   │ 10–38%  céu profundo, sem nuvens
│                  │
│ ─ ─ ─ ─ ─ ─ ─ ─ ─│ 38%
│    ▲ invasão     │
│  [ SUJEITO ]     │ 40–80%  centrado, 50–70% da largura
│                  │
│▓▓▓ colina ▓▓▓▓▓▓▓│ ~72%
│▓ CTA (82–96%) ▓▓▓│ grama escura e calma, sem flores claras
└──────────────────┘ 100%
```

Frase: `Vertical composition. The top 38% is clean deep blue sky for a headline, below a small 8% margin. The subject is centered, occupying roughly 40% to 80% of the frame height. The bottom 18% is calm, evenly shaded grass with no bright flowers, reserved for a button.`

### 5.4 Carrossel 4:5

```
┌────────────────────┐ 0%
│ meta-linha (4–9%)  │  três rótulos próprios, opcionais
│ TÍTULO  12–40%     │
│                    │
│  [ SUJEITO ] 40–88%│
│▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
│ paginação 90–100%  │  ← 01 02 03 … →  (camada gráfica)
└────────────────────┘
```

Frase: `Portrait 4:5. Keep the top 9% and bottom 10% visually calm for small interface text. Reserve 12% to 40% of the height as open sky for a headline; place the subject between 40% and 88%.`

### 5.5 Margens de segurança

- Nada essencial a menos de 5% de qualquer borda (corte de plataforma,
  `object-fit: cover`, safe areas do iPhone).
- Ponto focal registrado em porcentagem (ex.: `50% 62%`) para usar em
  `object-position` ([modelos-e-producao.md §11](modelos-e-producao.md)).

---

## 7. Consistência: séries, formatos e carrosséis

### 7.1 Bíblia da série (preencher antes de gerar)

```yaml
serie: "{nome}"
arquetipo: A            # A–H ([familia-ceu-campo.md §4](familia-ceu-campo.md)); carrossel pode usar até 2
acabamento: F1          # F1 CGI | F2 filme | F3 moda — único para a série
luz: L1                 # L1–L5 — única para a série
hora_e_sol: "midday, sun high behind camera-left"
ceu: "deep cerulean, few cumulus at edges"
terreno: "rounded grassy hill, short dense grass, small yellow and white wildflowers"
camera: "low, 28mm, slight upward angle"
acento: "lime #D4FF1A on {elemento}"   # um só
objeto_heroi: "{descrição exata e reutilizada palavra por palavra}"
texto_branco_ou_tinta: branco          # define o tipo de céu na zona do título
proibidos: [texto, logos, pessoas reconhecíveis, segundo acento]
```

Copie os campos **palavra por palavra** em todos os prompts da série.
Sinônimos geram variações.

### 7.2 Desktop → mobile → carrossel

1. Gere e aprove o **master** (geralmente o desktop 16:9).
2. Para cada outro formato, gere na proporção nativa usando o master como
   referência e o prompt do formato:
   `Use the reference image only for subject, materials, light, palette and finish. Recompose the scene natively for a {ASPECT} frame following these zones: {SAFE_ZONE_SENTENCE}. Do not crop or stretch the reference.`
3. Compare lado a lado: o objeto, a luz e o céu devem parecer o mesmo
   momento fotográfico.

### 7.3 Carrossel com panorama contínuo

Use quando o horizonte deve correr de um slide para o outro.

1. Gere um panorama 4K: **21:9 para 3 slides** ou **16:9 para 2 slides**.
2. Regras do prompt do panorama:
   - `the horizon line runs perfectly level and continuous across the full width`
   - um ponto de interesse **centralizado em cada terço** (ou metade);
   - nada importante sobre as linhas de corte (33,3% e 66,7% da largura para
     3 slides; 50% para 2);
   - zona de título em cada terço, conforme §5.4.
3. Fatie com ffmpeg. Três slides 4:5 de um 21:9 (ajusta a altura para 2,4:1
   e corta três faixas contíguas):

```bash
for i in 0 1 2; do
  ffmpeg -y -i pano.png \
    -vf "crop=iw:trunc(iw/2.4/2)*2,crop=trunc(ih*4/5/2)*2:ih:${i}*trunc(ih*4/5/2)*2:0,scale=1080:1350:flags=lanczos" \
    "slide-$((i+1)).png"
done
```

Dois slides 4:5 de um 16:9: troque `2.4` por `1.6` e use `i` em `0 1`.

### 7.4 Carrossel: um universo, uma história

**Regra validada pelo cliente (caso de telemedicina):** o carrossel 1, com o
mesmo casal e o mesmo céu em todos os slides, "seguiu um sentido" e foi
preferido. O carrossel 2, com um mundo diferente por slide (cadeira no morro,
relógio gigante, guarda-chuvas, folhas de bananeira), saiu **bagunçado** e
**copiou as referências**. Nunca troque de família entre slides.

| Slide | Papel | O que muda | O que fica |
|---|---|---|---|
| 1 | Gancho (capa) | Plano mais próximo e mais emocional | Pessoas, luz, céu, acabamento, tipografia |
| 2 | Tensão / problema | Outro gesto ou objeto da rotina do público | idem |
| 3 | Virada / solução | Mudança de distância (abre o plano) | idem |
| 4 | Prova / como funciona | Interface de vidro (tags, constelação, passos) | idem |
| 5 | Para quem / benefício | Outro ângulo das mesmas pessoas | idem |
| N | Ação | O plano mais calmo, maior espaço livre, botão | idem |

**De onde vem a variedade** (combine 2 por slide, nunca a cena inteira):
- **gesto:** testas, mãos, pulso, ombros, celular erguido, cabeça no ombro;
- **distância:** rosto → mãos → meio corpo → as duas figuras pequenas no céu;
- **ângulo:** perfil, de costas, de baixo, de cima;
- **interface:** título solto, tags, constelação, passos numerados, botão;
- **posição do texto:** topo, centro, base, à esquerda.

**Sequência (o que faz "arrastar"):**
- Paginação idêntica em todos os slides, gerada na mesma posição:
  `"0N / 0T"` à esquerda e `"ARRASTE →"` à direita, no rodapé (94%),
  pequeno, branco, caixa-alta espaçada. No último slide, só a paginação.
- Um elemento que **atravessa a borda** entre slides reforça o arrastar:
  a mão, o ombro ou a linha da constelação cortados na borda direita
  continuam na esquerda do próximo slide (use o panorama da §7.3 quando
  quiser continuidade real).
- O título de cada slide termina "aberto" para o próximo (pergunta,
  dois-pontos, frase que pede continuação), exceto o último.

**Antes de gerar, escreva o roteiro em uma linha por slide** (papel, gesto,
distância, texto). Se dois slides tiverem o mesmo gesto e a mesma distância,
mude um. Se algum slide pedir outro cenário, a ideia não cabe neste carrossel.

Grade, setas complexas e fitas curvas continuam sendo camada de design (§8).
Para o cabeçalho de três âncoras, consulte `microtipografia-editorial.md`:
pode ser solicitado na imagem quando pedido, mas a grafia e a grade precisam
ser conferidas; sobreposição tipográfica é a alternativa de controle exato.

---

## 8. Camada gráfica — geração ou sobreposição

Cabeçalho de três âncoras: regras, escala, textos exatos e QA em
`microtipografia-editorial.md`. A aplicação é opcional em slides escolhidos,
sem copiar data, autor ou categoria das referências.

Para os elementos complexos abaixo, prefira HTML/Figma por cima da imagem:
- Linhas finas, grade, círculo grande, marcas "+", molduras finas (R03, R05, R07, R12).
- Paginação `BACK 01 … 08 NEXT` e setas (R12, R14).
- Chips de vidro tipo HUD com dados (R13).
- Etiquetas de anotação com linha-guia (R02, R04).
- Fita de texto curva (R06): SVG `textPath`, nunca texto gerado.

Linhas e chips: branco com 40–70% de opacidade, 1 px, sem sombra pesada.

### Pares tipográficos das referências

| Par observado | Ref. | Alternativa livre (Google Fonts) |
|---|---|---|
| Serifa de exibição + sans neutra | R09, R10 | Instrument Serif + Inter |
| Serifa itálica + sans pesada | R04, R15 | Playfair Display Italic + Inter Bold |
| Script formal + sans | R08 | Pinyon Script + Inter |
| Condensada esportiva em lime | R13 | Anton ou Bebas Neue |
| Display larga pesada + serifa | R14 | Archivo Black + Instrument Serif |
| Display retrô + geométrica | R02 | Abril Fatface + Montserrat |

As fontes usadas nas peças originais (Athelas, Moara, Tan Headlines) podem
exigir licença comercial; confirme antes de usar.

---
