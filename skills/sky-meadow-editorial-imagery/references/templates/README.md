# Templates testados — índice

Receitas completas por tipo de peça, nascidas de casos reais desta skill.
Cada template junta o fluxo, a bíblia, o roteiro, os erros já vistos e o
link para os prompts finais do caso. Comece por aqui quando o pedido
combinar com um deles; as regras gerais continuam nos módulos de `../`.

| ID | Template | Formato | Status | Caso | Arquivos |
|---|---|---|---|---|---|
| T1 | Carrossel de conversão para Instagram (serviço, SaaS, negócio local) | 1080×1350 + story 1080×1920 | **Testado, 3 rodadas** | Groomy (SaaS para barbearias) | `t1-carrossel-conversao.md`, `casos/groomy-carrossel-v4.md`, `../../assets/templates/groomy-rodada1.jpg`, `../../assets/templates/groomy-rodada2.jpg`, `../../assets/templates/groomy-rodada3-capas.png` |
| T2 | Pitch deck de 5 minutos | 16:9, 9 slides | **Testado, aprovado** | PlantMed (agro) | `t2-pitch-deck-16x9.md`, `casos/plantmed-pitch.md`, `../../assets/templates/modelo-financeiro-pitch.xlsx` |
| T3 | Carrossel de produto na pele | 1080×1350, 6 slides | Prompts entregues, não testados | Femini Care (suplemento) | `t3-carrossel-produto-na-pele.md`, `casos/femini-care-carrossel.md` |

## Linha do tempo do que foi aprendido

1. **Femini Care:** primeira aplicação da skill pública; @ no centro do topo, copy só do rótulo.
2. **Groomy rodada 1:** universo consistente aprovado; mesma diagramação em todos os slides, contador errado, arquivo em 3:4.
3. **Groomy rodada 2:** layouts variados aprovados; contador errado em 5 de 8; realismo de banco de imagem.
4. **PlantMed:** pitch 16:9 aprovado; bloqueio de política resolvido com prompt enxuto em slide sem pessoa.
5. **Groomy rodada 3:** lugar precário (erro oposto); regra do padrão mediano bem cuidado.
6. **Groomy v4:** prompts atuais com todas as correções (aguardando nova rodada).

## Regras que todos os templates herdam

- Contador do carrossel sempre em camada (`../../scripts/kit_overlay.mjs`).
- Capa (ou slide 1) passa no portão antes de virar referência (`../realismo-fotografico.md §R.13`).
- Lugar e pessoas no padrão da marca, nunca precários sem pedido (`§R.11.0`).
- Referência de continuidade sem `identity`; slides sem pessoa sem referência.
- Logo e embalagem reais: logo por cima; embalagem como referência.
- Gerador entrega 3:4? Prompt composto para o corte (`../formatos-e-composicao.md §5.6`).

Ao fechar um novo caso: crie `tN-*.md` ou atualize o template existente,
salve os prompts finais em `casos/`, uma folha de contato por rodada em
`assets/templates/` e a linha correspondente na tabela acima.
