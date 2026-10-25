# Modelos, camadas e exportação web

## 9. Adaptadores de modelo

### 9.1 Gemini 3 Pro Image — script desta skill (recomendado)

Gera na proporção nativa e aceita referências. Chave em `GEMINI_API_KEY`.

```bash
uv run ~/.claude/skills/sky-meadow-editorial-imagery/scripts/generate.py \
  --prompt-file prompts/hero-desktop.txt --out out/hero-desktop.png --aspect 16:9 --size 4K

uv run ~/.claude/skills/sky-meadow-editorial-imagery/scripts/generate.py \
  --prompt-file prompts/hero-mobile.txt --out out/hero-mobile.png --aspect 9:16 --size 2K \
  --ref out/hero-desktop.png
```

- Proporções: `1:1 2:3 3:2 3:4 4:3 4:5 5:4 9:16 16:9 21:9`. Tamanhos: `1K 2K 4K`.
- `--ref` é repetível: master aprovado, slide anterior, foto real do produto.
- `--dry-run` valida entradas e mostra a configuração sem chamar a API.
- Salve prompts em arquivos `.txt` (versionáveis e sem problemas de aspas no shell).

### 9.2 Script `nano-banana-pro` (instalado)

Ele **não** expõe proporção: só `--prompt`, `--filename`, `--input-image`,
`--resolution`, `--api-key`. Use-o para edições pontuais sobre uma imagem já no
formato certo, por exemplo:
`"Remove the cloud behind the upper-center area; keep everything else identical."`

### 9.3 Midjourney

Formato de lista curta, parâmetros no fim:

```text
{subject}, {setting}, {camera}, {light}, deep cerulean sky, lush green grass, {accent}, {finish}, generous empty sky in the upper {N}% --ar 16:9 --style raw --stylize 150 --chaos 5 --no text, letters, logo, watermark, frame
```

- Série: aprove um master e use `--sref <URL do master> --seed <n>` nas
  demais peças. Use como `--sref` apenas imagens próprias ou licenciadas.
- `--chaos` 0–10 para série consistente; 20–35 só na exploração.

### 9.4 Outros modelos

Use o parâmetro nativo de proporção/tamanho do modelo e o template da [prompts.md §6](prompts.md)
inteiro. Se o modelo não aceitar referência de imagem, repita a bíblia da série
literalmente em cada prompt.

### 9.5 Pacote multi-IA (entrega padrão quando o usuário pede prompts)

Cada peça sai com os quatro blocos abaixo, a partir de **um** prompt-mestre
em inglês (template de `prompts.md §6`), para que qualquer modelo ou
terminal chegue ao mesmo resultado:

1. **CLI/API (esta skill):** o prompt salvo em `prompts/{peca}.txt` e o
   comando `generate.py` com `--aspect`, `--size` e os `--ref` na ordem
   (rode `--dry-run` antes para validar acervo e parâmetros).
2. **Chat de imagem** (ChatGPT/GPT Image, app Gemini, Flux, Firefly, Ideogram):
   o mesmo prompt-mestre; a proporção vai no seletor do app ou como
   primeira frase. Peças com mais de 6 palavras na imagem: prefira modelos
   fortes em texto e confira acentos letra a letra.
3. **Midjourney:** versão curta da §9.3, com `--ar` e `--no text` quando o
   texto for em camada.
4. **Anexos:** quais arquivos acompanham o prompt e com que função (foto
   real da profissional = identidade; foto do produto = rótulo). Um caminho
   no texto não envia a imagem; MK/IG/R/N nunca vão como anexo.

Texto longo, números, preço, CRO/CRM e logo continuam em camada em
qualquer modelo.

---

## 10. Texto atrás do sujeito (sanduíche de profundidade)

Padrão de R07, R11, R12, R13: fundo → título → sujeito recortado.

1. **Gere** com `{LAYER_SENTENCE}` de invasão: silhueta nítida, sem desfoque de
   movimento, céu liso atrás do contorno.
2. **Recorte** o sujeito em PNG transparente, um recorte por formato
   (o desktop e o mobile têm enquadramentos diferentes). Opções:
   - edição no próprio modelo: `Isolate the {subject} exactly as it is on a pure flat #00FF00 background; do not change its shape, pose or lighting.` e remova o verde depois;
   - ferramenta de remoção de fundo (ex.: rembg). Verifique a borda em 200%.
3. **Monte** em camadas. O título continua texto HTML real:

```html
<section class="hero">
  <picture class="hero__bg">
    <source media="(max-width: 767px)" type="image/avif" srcset="hero-mobile-750.avif 750w, hero-mobile-1080.avif 1080w" sizes="100vw">
    <source type="image/avif" srcset="hero-desktop-1280.avif 1280w, hero-desktop-1920.avif 1920w, hero-desktop-2560.avif 2560w" sizes="100vw">
    <img src="hero-desktop-1920.jpg" alt="" width="1920" height="1080" fetchpriority="high" decoding="async">
  </picture>
  <h1 class="hero__title">Título real em HTML</h1>
  <picture class="hero__fg" aria-hidden="true">
    <source media="(max-width: 767px)" srcset="hero-mobile-subject.webp">
    <img src="hero-desktop-subject.webp" alt="" width="1920" height="1080" decoding="async">
  </picture>
</section>
```

```css
.hero { position: relative; isolation: isolate; overflow: clip; }
.hero__bg img, .hero__fg img {
  position: absolute; inset: 0; width: 100%; height: 100%;
  object-fit: cover; object-position: var(--focal, 50% 62%);
}
.hero__title { position: relative; z-index: 1; }
.hero__fg { position: absolute; inset: 0; z-index: 2; pointer-events: none; }
```

Regras:
- Fundo e recorte com **mesmas dimensões e mesmo `object-position`**, ou a
  sobreposição desalinha.
- O sujeito cobre no máximo ~25% da área das letras e nunca a primeira palavra.
- Imagem decorativa: `alt=""`. Se a imagem carregar significado, descreva-o no
  `alt` do fundo.
- Movimento (parallax, entrada) é opcional: só `transform`/`opacity`, rolagem
  nativa, nada de sequestrar o scroll, e versão estática com
  `prefers-reduced-motion: reduce`.

---

## 11. Exportação web

```bash
# AVIF (principal)
ffmpeg -y -i hero-desktop.png -vf "scale=1920:-2:flags=lanczos" -c:v libaom-av1 -still-picture 1 -crf 32 -b:v 0 hero-desktop-1920.avif
# WebP (fallback e recortes com transparência)
ffmpeg -y -i hero-desktop.png -vf "scale=1920:-2:flags=lanczos" -c:v libwebp -quality 80 hero-desktop-1920.webp
```

- Larguras: desktop 1280/1920/2560; mobile 750/1080; carrossel 1080 (×1350).
- Alvo do hero (LCP): ≤ 200 KB no tamanho servido; ajuste `-crf`
  (maior = menor arquivo).
- Céu liso comprime bem; se aparecer banding no gradiente, reduza o `-crf`
  antes de aumentar a resolução.
- Pré-carregue só a imagem LCP do formato atual; declare `width`/`height`.
- Para carrossel social, exporte PNG ou JPEG de alta qualidade em 1080×1350;
  a plataforma recomprime.

## 11.1 Hero em tela cheia + texto em HTML logo abaixo (preferido no caso de telemedicina)

Quando a imagem é a mensagem, ela ocupa a hero inteira **sem texto** e o
título + botão vêm numa seção logo abaixo, em HTML. A hero ocupa ~88% da
altura da tela para o começo do título aparecer acima da dobra.

Duas formas de entregar a mesma peça:

| Peça | Imagem | Texto/botão |
|---|---|---|
| Redes sociais / mockup | Gerada **com** texto e botão (G01, G02) | Na imagem |
| Site | Gerada **sem** texto (`Do not include any text…`) | HTML real, clicável e indexável |

```html
<section class="hero">
  <picture>
    <source media="(max-width: 767px)" type="image/avif" srcset="hero-mobile-750.avif 750w, hero-mobile-1080.avif 1080w" sizes="100vw">
    <source type="image/avif" srcset="hero-desktop-1280.avif 1280w, hero-desktop-1920.avif 1920w, hero-desktop-2560.avif 2560w" sizes="100vw">
    <img src="hero-desktop-1920.jpg" width="2560" height="1440" fetchpriority="high" decoding="async"
         alt="{descrição da cena}">
  </picture>
</section>

<section class="intro">
  <h1>Escutar <em>também</em> é cuidar.</h1>
  <p>{subtítulo}</p>
  <a class="btn-outline" href="/agendar">Agendar consulta <span aria-hidden="true">→</span></a>
</section>
```

```css
:root { --sky-top: #546D8C; } /* branco 5,33:1 */

.hero { position: relative; height: 88svh; min-height: 520px; overflow: clip; }
.hero img { display: block; width: 100%; height: 100%; object-fit: cover; object-position: 50% 45%; }
.hero::after {               /* funde a base da foto no fundo da seção */
  content: ""; position: absolute; inset: auto 0 0 0; height: 24%;
  background: linear-gradient(to bottom, transparent, var(--sky-top));
  pointer-events: none;
}

.intro { background: var(--sky-top); color: #fff; text-align: center;
  padding: clamp(40px, 7vw, 104px) 24px clamp(64px, 9vw, 128px); }
.intro h1 { margin: 0; font: 400 clamp(2.5rem, 5.5vw, 4.75rem)/1.05 "Instrument Serif", serif; text-wrap: balance; }
.intro em { font-style: italic; }
.intro p { max-width: 34ch; margin: 20px auto 36px; font: 400 clamp(1.125rem, 1.5vw, 1.25rem)/1.5 Inter, sans-serif; }

/* botão de contorno — o estilo aprovado */
.btn-outline {
  display: inline-flex; align-items: center; gap: .6em; min-height: 48px; padding: 14px 36px;
  border: 1.5px solid #fff; border-radius: 999px; color: #fff; text-decoration: none;
  font: 500 .95rem/1 Inter, sans-serif; letter-spacing: .08em; text-transform: uppercase;
  transition: background-color .2s ease;
}
@media (hover: hover) and (pointer: fine) {
  .btn-outline:hover { background-color: rgb(255 255 255 / .12); }
}
.btn-outline:focus-visible { outline: 2px solid #fff; outline-offset: 4px; }
```

Variante **acrílico fumê** (quando o fundo atrás do botão é claro):
`background: rgb(20 35 60 / .20); border: 1px solid rgb(255 255 255 / .45); backdrop-filter: blur(14px) saturate(1.2);` → branco ≈ 6,65:1.

Conferir em 390 px e 1440 px de largura: o título precisa aparecer acima da
dobra e o degradê não pode cortar queixos ou mãos.

---
