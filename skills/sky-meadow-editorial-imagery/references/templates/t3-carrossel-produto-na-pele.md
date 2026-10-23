# T3 · Carrossel de produto na pele (suplemento, cosmético, saúde íntima)

**Status:** prompts entregues, **não testados em geração** (caso Femini Care,
probiótico feminino da Moza Pharma). Prompts: `casos/femini-care-carrossel.md`.
Antes de reutilizar, aplique as regras que vieram depois, testadas no T1:
contador em camada, padrão do lugar, ficha de personagem e portão da capa.

**Use quando:** o protagonista é a embalagem real do produto, com o corpo
como moldura, sem rosto.

## T3.1 Regras do template

- Família C, arquétipo C3. A foto real do produto entra como **imagem 1** na capa (rótulo e tom de pele) e como **imagem 2** nos slides seguintes (imagem 1 = capa aprovada).
- `Reproduce the product exactly as in the reference image, including its label; do not invent text.`
- Acento = cor da embalagem (tampa), medida na foto; neutros do fundo da foto original.
- Bloco de realismo na variante corpo sem rosto (`realismo-fotografico.md §R.6`).
- **Copy só do rótulo** para o consumidor; ficha técnica e estudos são material de prescritor (`nichos-e-ideias.md §N.1`), sujeitos à ANVISA. Recomendar revisão regulatória.
- Contador em camada (`scripts/kit_overlay.mjs`) e faixa reservada no prompt.
- Ambiente (quando houver): casa ou banheiro bem cuidados, luz de janela (`nichos-e-ideias.md §N.5`).

## T3.2 Roteiro de 6 slides

Gancho (close, corpo como moldura) → tensão (gesto fechado, sem produto) →
virada (plano aberto, produto no chão) → prova (cápsula na palma + 3 tags com
dados do rótulo) → para quem (perfil, pílulas de fase da vida com aviso de
orientação profissional) → ação (produto sozinho, CTA de direct).

## T3.3 O que validar no primeiro teste

- Rótulo idêntico ao real (letras, cores, logo).
- Pele real sem brilho de propaganda; mãos com cinco dedos.
- Contraste do texto escuro sobre o fundo claro medido na arte.
