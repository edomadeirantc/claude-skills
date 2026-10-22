# Interface de vidro e camada gráfica gerada

Componentes de interface desenhados **pelo modelo, dentro da imagem**:
vidro fosco, tags, constelação, caixas, botões. Cada componente traz a frase de
prompt que funcionou e o erro que o modelo costuma cometer.

Quando o elemento precisa ser clicável, indexável ou traduzível, faça-o em
HTML/CSS por cima da imagem (`modelos-e-producao.md`). Gere-o na imagem só
para mockup, redes sociais ou quando o cliente pedir a peça fechada.

---

## V.1 Vidro em degradê progressivo (aprovado — G01)

Vidro fosco que **dissolve na foto**, sem objeto, borda ou caixa. É o recurso
certo quando se quer "vidro/acrílico tomando a imagem e ainda dando para ver o
fundo".

```text
PROGRESSIVE FROSTED GLASS (full width, no edges)
- The real {BACKGROUND} continues across the entire image, all the way to the top edge.
- Over the upper part of the image, apply a full-width frosted acrylic glass effect that blends seamlessly into the photo:
  - From 0% to 25% of the image height: strong frosted diffusion; the background is still visible as soft shapes and light, not a flat color.
  - From 25% to 45%: the blur fades out smoothly and gradually.
  - Below 45%: completely sharp, untouched photograph. The blur must end above the top of the heads.
- Add a subtle dark smoky tint that follows the same gradient, strongest at the very top and fading to nothing by 45%, only enough to keep white text clearly readable.
- Add a very fine frosted grain inside the blurred area only.
- There is no visible boundary, line, edge, highlight or shadow anywhere in the gradient.
```

Reforço quando o modelo insiste em fazer uma caixa:
`Important: the glass effect is a gradient over the whole width, not an object.`

**Erro observado:** pedir "a floating frosted acrylic glass panel inset 5%…"
produziu um **card** retangular com borda e sombra, rejeitado pelo cliente.
"Panel", "card", "box" e "inset" geram objeto; use "gradient", "full-width",
"no edges".

---

## V.2 Painéis e cards de vidro (quando o card é desejado)

| Variante | Ref. | Frase-chave |
|---|---|---|
| Card central | N03 | `a rounded frosted-glass card with soft backdrop blur, a thin semi-transparent white edge and a very soft shadow` |
| Painel que sangra a borda | N01 | `a wide frosted-glass panel that bleeds off the left edge of the frame, its right side rounded` |
| Painel recortado | N02 | `a tall frosted-glass panel with two semicircular notches cut into its left and right edges` |
| Card com miniatura | N05 | `inside the card, on the right, a small vertical thumbnail of the same scene` |
| Aba de vidro no topo | N01 | `a narrow rounded glass tab hanging from the top edge` |

Regras: um card por peça; o fundo atrás do vidro precisa ter forma e luz
(floresta, flores, grama) para o vidro "ler"; sobre céu liso o vidro some.

---

## V.3 Tags de vidro (aprovado — G02)

```text
Three frosted-glass pill tags with soft backdrop blur and a thin semi-transparent white edge, picking up the warm skin tones where they overlap. White sans-serif labels:
- "{TAG_1}" at about {X}% of the width and {Y}% of the height;
- "{TAG_2}" …;
- "{TAG_3}" ….
```

- Sempre **3 tags**, com posições em porcentagem, distribuídas em triângulo.
- Rótulos curtos (1–2 palavras). Confira acentos.
- Tags sobrepostas à pele ficam mais bonitas que sobre o céu puro.

## V.4 Constelação (aprovado — G02)

```text
Next to each tag, a small solid white dot. Thin 1-pixel white lines connect the three dots to each other. No other lines.
```

**Erros observados:** o modelo acrescentou **linhas verticais finas** descendo
pelo centro e uma linha ligando o ponto inferior ao rodapé. Sempre inclua
`No other lines` e, na edição, `Remove the thin straight vertical lines running down the center of the image`.

## V.5 Conectores tracejados ortogonais (N07)

`Thin dashed white connector lines run horizontally and then turn vertically at right angles, linking each card to the next.`
Use com cards de contorno informativos (título itálico + 2–3 linhas), nunca com tags.

## V.6 Caixas de contorno pontilhado (N12)

`A large rounded rectangle outlined with a thin dotted white line at 60% opacity, no fill.`
Se sair linha contínua: `dotted outline made of small separate dots`.
O cliente aprovado preferiu **título solto, sem caixa**; ofereça as duas versões.

---

## V.7 Botões

| Tipo | Frase | Quando usar | Contraste |
|---|---|---|---|
| **Contorno** ★ aprovado (G01, G02) | `a pill drawn only with a thin, crisp, solid white outline, fully transparent inside, containing "AGENDAR CONSULTA →" in a clean white uppercase sans-serif with slight letter spacing and a thin right arrow. No fill, blur, tint, glow or shadow inside or around it.` | Foto escura atrás (roupa grafite, grama escura) | Depende do fundo; sobre `#667E9F` ≈ 4,2:1 |
| Acrílico fumê | `frosted acrylic glass … with a slight smoky tint so the white text is clearly legible, a thin semi-transparent white edge, a subtle light highlight along its top edge` | Céu claro atrás | ≈ 6,65:1 sobre `#546D8C` |
| Sólido claro | `a solid off-white pill with dark text` | Fundo muito variado | Alto, mas **foi rejeitado** no caso: o cliente queria só o contorno |

**Erros observados, todos com o botão:**
1. O modelo coloca um **véu verde/escuro desfocado** em volta do botão para
   "ajudar" a leitura. Proíba sempre: `No fill, blur, tint, glow, shadow, halo or vignette inside or around it`
   e `The lower part of the image is a clean, sharp, natural photograph`.
2. Se o véu voltar, escureça o que está **atrás** do botão (ex.: camisa grafite
   em vez de cinza-claro) ou gere sem botão e faça o botão em HTML.
3. Para copiar um botão de outra peça, passe-a como segunda referência e diga
   `IMAGE 2 is a reference used only for the style of the button`.

Botão sem mais nada: `Nothing else at the bottom: no box, no frame, no logo, no other text.`

---

## V.8 Outros elementos

| Elemento | Ref. | Frase |
|---|---|---|
| Marcas de corte nos cantos | N04 | `small thin white crosshair crop marks in the four corners` |
| Selo pill de contorno | N03, N06 | `small outlined pill badges with short labels` |
| Selo carimbado circular | N18 | `a circular stamped badge with scalloped edge` (texto dentro sai mal; prefira aplicar depois) |
| Grade de ícones de linha | N17 | **Não gere.** Ícones saem inconsistentes; aplique no design |
| Fita/laço gráfico | R06, N11 | `a wide flat {COLOR} ribbon that loops behind and in front of the subject` |
| Texto pintado no chão | N18 | `huge white letters painted on the court surface, following its perspective` (alto risco de erro) |

---

## V.9 Textos indesejados que vazam

O modelo repete rótulos de prompts anteriores ("{MARCA}", "{ANO}", meta-linhas).
Feche sempre com:
`No other text anywhere: no logo, no wordmark, no navigation, no supporting text.`
Na edição: `Delete the small texts "{TEXTO}" completely and restore the background.`
