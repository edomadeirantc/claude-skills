# T1 · Carrossel de conversão para Instagram (serviço, SaaS, negócio local)

**Status:** testado em 3 rodadas reais (caso Groomy, SaaS de gestão para
barbearias). Rodada 1 aprovada em direção e consistência; rodada 2 aprovada
em variação de layout; rodada 3 reprovada pelo padrão do lugar, corrigida na
v4. Prompts finais: `casos/groomy-carrossel-v4.md`. As folhas de contato das
rodadas saíram do acervo na curadoria de 25/10/2026; as lições ficaram no texto.

**Use quando:** a peça é um carrossel de feed que precisa de alcance e ação
(direct, teste, salvar) para um serviço ou software, com uma pessoa real do
ofício como protagonista. Para produto físico na pele use T3; para
apresentação 16:9 use T2.

## T1.1 Entregas e formato

- Feed 1080×1350 (4:5) e story 1080×1920 (9:16). Nada mais vai para publicação.
- O gerador usado entregou 3:4 (1792×2400) mesmo pedindo 4:5. Escreva os
  prompts em 3:4 **compostos para o corte central** (`formatos-e-composicao.md §5.6`):
  faixas 0–4% e 96–100% só com fundo; @ com linha-base em 8,8%; faixa
  reservada ao contador em 85–93%.
- Confira a proporção do primeiro arquivo gerado antes de seguir.

## T1.2 Sequência de trabalho

1. **Leitura do material** (site, logo, prints): nicho, oferta real, preço, @,
   acento da marca medido no logo, padrão do lugar (`briefing-perguntas.md` Q.0).
2. **Uma rodada de perguntas** com resposta recomendada: @ exato, nº de
   slides, gerador (4:5 ou 3:4), prova social e prints. Prints e prova social
   são opcionais; sem eles o slide de prova vira resumo.
3. **Salto + 3 conceitos** (seguro, ousado, fora da curva) com verbos MK (`repertorio-mercado.md §R.3`) e 3 ganchos; aprovado no caso: "O rolo do dia" (fita de comanda gigante) + "PARE DE FECHAR O CAIXA DE CABEÇA."
4. **Família derivada do conceito**: F quando a marca é escura com acento forte (Groomy: `#0A0A0A` + lime `#C8F028`).
5. **Storyboard por slide** na tabela canônica de `variacao-de-layout.md §V.5`, partindo do roteiro SaaS de 8 slides (`saas.md §S.4`): movimento, escala/cena, câmera e layout mudam a cada slide.
6. **Bíblia da série** com ficha de personagem, padrão do lugar, luz, paleta, acento e registro documental (T1.4); sem câmera.
7. **Capa primeiro**, sem referência; passa no portão da capa (`realismo-fotografico.md §R.13`) antes de servir de referência.
8. **Referência da capa** só nos slides que o storyboard marca como "mesmo lugar da capa = sim"; slides em outra escala ou lugar e **slides sem pessoa** vão sem referência e sem bloco de pele.
9. **Corte** para 1080×1350 e **contador em camada** (T1.6).
10. **Story** a partir da capa aprovada, 9:16 nativo (T1.7).

## T1.3 Storyboard (8 slides)

Use a tabela de `variacao-de-layout.md §V.5`. No caso Groomy aprovado, os
layouts por slide foram L1, L2, L3, L8, L11, L7, L4 e L12, e o topo seguiu a
recorrência de `microtipografia-editorial.md §2.3`. Em todo slide sem tag à
direita, escreva `Nothing on the right`: a tag da capa vazou para o slide 4
na rodada 2.

## T1.4 Bíblia da série (modelo)

```text
SERIES BIBLE (fixed in every slide: light, palette, accent, materials, type voices and, when the slide has a person, the {PAPEL}; place, scale, camera and layout come from each slide's storyboard row)
- Main place (used only in the slides the storyboard marks as the cover's place): a well-kept, mid-market {TIPO DE LUGAR} in a Brazilian city, {tamanho}, successful and organized. {3–4 materiais do padrão}; {luz real do lugar}; {móveis em bom estado}; {objetos de uso variados e organizados}; {área de espera/gente}. {Rastro de trabalho do momento}. Posters, price board and calendar stay soft, out of focus and unreadable.
- The {PAPEL}: {ficha de personagem: nome, idade exata, origem, tipo físico real, cabelo real, 2–3 marcas únicas, roupa limpa coerente com o padrão, acessório comum}. Not a model: a real, likable professional.
- Other people: ordinary customers of varied ages, faces not the focus, partly turned away.
- Light: the real light of the place, {fonte 1} mixed with {fonte 2}, one dominant direction; time of day as stated in each slide. No bare fluorescent tubes, no Edison bulbs, no moody concept lighting.
- Photography: documentary reportage photograph taken during a normal working day for a Brazilian news magazine; full-frame camera, available light, visible ISO grain, slightly imperfect framing, true-to-life color, no color-grading look. Lens, height and angle come from each slide's storyboard row.
- Brand treatment lives only in the design layer: {ACCENT} never appears on objects in the scene.
- Type voices: DISPLAY = {sans pesada}. COUNTERPOINT = {serif itálica}. UTILITY = {mono}. Use only the voices the slide names.
- Frame: portrait 3:4, composed to be center-cropped to 4:5: top 4% and bottom 4% only background.
- Top handle line, baseline at 8.8%: "{@handle}" centered, lowercase exactly as written, no verification badge. Only the side labels this slide lists.
- Reserved band: from 85% to 93% of the height keep only calm dark background, with no text, dots, squares, numbers or shapes.
```

Bloco de realismo com pessoa: R.6 + proibição de visual precário
(`realismo-fotografico.md §R.11.0`). Slides sem pessoa: realismo só de
materiais. Referência dos slides 2+: frase de `variacao-de-layout.md §V.4`
(sem `identity`).

## T1.5 Erros por rodada e correções (registrados)

| Rodada | Sintoma | Causa | Correção na skill |
|---|---|---|---|
| 1 | 8 slides com a mesma diagramação | Um prompt-base de layout + "keep typography exactly" na referência | Layouts L1–L12 e 3 vozes (`variacao-de-layout.md`) |
| 1 | Primeiro ponto lime em vários slides | Ponto herdado da capa | Contador em camada (T1.6) |
| 1 | Arquivo 3:4 com @ a 4% e rodapé a 96% | Gerador ignorou 4:5 | Prompt 3:4 composto para o corte (§5.6) |
| 2 | Contador com 6–7 pontos ou aceso errado em 5 de 8 | O gerador não conta elementos repetidos | Contador fora do prompt, `scripts/kit_overlay.mjs` |
| 2 | Barbeiro e barbearia de banco de imagem | Bíblia de arquétipo de revista, personagem médio, luz dramática | Ficha de personagem, ambiente vivo, registro documental, portão da capa (`realismo-fotografico.md §R.9–R.13`) |
| 2 | Tag da capa no slide 4 | Herança da referência | `Nothing on the right` |
| 3 | Barbearia pobre e precária | Prompt pedindo azulejo trincado, assento remendado, LED frio | Padrão do lugar: mediano bem cuidado (`§R.11.0`), tabela por nicho (`nichos-e-ideias.md §N.5`) |
| PlantMed | Geração bloqueada por política | `identity` + bloco de pele + referência num slide sem pessoa | Referência de continuidade sem `identity`; slide sem pessoa sem referência |

## T1.6 Contador em camada

```bash
node scripts/kit_overlay.mjs --total 8 --accent "#C8F028" --out ./kit
```

Gera `kit-01.svg … kit-08.svg` (1080×1350, transparentes): pontos com o
losango no slide atual, "0N/08" e "ARRASTE →" (some no último). Corte cada
imagem para 1080×1350 e aplique o kit por cima no Canva/Figma. Testado sobre
o slide 4 da rodada 2: alinhado com a faixa reservada.

## T1.7 Story derivado

9:16 nativo com `--ref` da capa aprovada; topo 0–13% e base 82–100% livres
(interface do Instagram); @ em ~15%; título 50–62%; faixa 70–80% vazia para
a figurinha de link (aplicada no app). Sem contador. Prompt pronto no fim de
`casos/groomy-carrossel-v4.md`; regras em `formatos-e-composicao.md §5.6`.

## T1.8 Checklist de entrega

- [ ] Capa passou no portão (nem banco de imagem, nem lugar precário).
- [ ] 4+ layouts distintos (no caso Groomy: 8), um respiro, recorrência do topo correta; storyboard §V.5 cumprido (nada repetido em slides seguidos).
- [ ] Textos com acento, @ exato, sem selo indevido.
- [ ] Corte 1080×1350 conferido; contador aplicado em camada.
- [ ] Legenda (Job B), 5 hashtags no máximo, alt text da capa.
