# Protocolo de teste da Meadow

Separar duas verificações: **comportamento de direção/prompts** e **arte renderizada**. Prompt bem estruturado não comprova imagem legível. Usar as mesmas tarefas antes/depois da revisão; registrar saídas literais, versão, limitações e critérios, sem ajustar o teste para justificar o resultado.

## 1. Comportamento observável

Ler `../evals/scenarios.json`. Executar tarefas em contexto novo, com a skill e os arquivos que ela mandar consultar. Abrir referências disponíveis; não substituir leitura de pixels por nome. Usar marca fictícia nas avaliações e manter `clientes/` desligado. Pedido de somente prompts não chama API.

Critérios para um pedido de arte completa:

1. Estudou público, tese e ação; escolheu referências por papel e relação, justificando o efeito.
2. Entregou o número pedido de blocos completos, sem campos por preencher; cada bloco funciona sozinho.
3. Incluiu copy literal, @ exato central e trio na capa/slide 2; recorrência das laterais é explícita.
4. Incluiu a fração correta em cada prompt pronto, sem pontos/losangos e sem etapa oculta de aplicação.
5. O miolo explica o gancho, mantém bíblia e muda informação/estado com propósito; não força uma MK diferente por slide.
6. Não inventou métricas, telas de produto, licença, consulta, pessoa real ou selo.
7. Declarou o que foi apenas planejado e o que foi efetivamente gerado/inspecionado.

**Fundo explícito é contraexemplo:** preservar saída sem lettering, usar `--background-only`, não impor cabeçalho/copy. **Saúde sem identificação obrigatória:** pedir dados ausentes e não dizer “publicável”. Esses ramos não devem ser penalizados como falta de copy.

Para testar redação de regra, usar cinco amostras independentes por variante e um controle sem a orientação. Ler manualmente toda saída sinalizada; não contar palavras citadas em contraexemplos como falha. Registrar também variabilidade. Fichas fornecidas numa microavaliação sem ferramentas devem ser identificadas como fichas, nunca como imagens abertas.

## 2. Regressões e smoke dos scripts

```bash
python -m unittest discover -s tests -v
node --check scripts/kit_overlay.mjs
python scripts/check_assets.py
python scripts/lint_prompts.py prompts/slide-*.txt
python scripts/generate.py --prompt-file prompts/slide-01.txt --out slide-01.png --aspect 4:5 --dry-run
node scripts/kit_overlay.mjs --total 8 --out ./kit
```

Usar `--background-only` no linter/gerador somente para a tarefa explícita de fundo. Testar ausência de copy, conflito de proibição global, campo não preenchido, faixa vazia local sem conflito, exceção de fundo e progresso real da navegação. O kit deve orientar a página atual sem marcadores repetidos e retirar avanço no último slide.

Smoke: extrair os blocos completos de `exemplo-agenda-editorial.md`, validar os seis e executar o `--dry-run` real. Gerar SVGs com o CLI, abrir uma página intermediária e a final. O dry-run não importa SDK nem chama API; não registrar isso como render Gemini aprovado. Sintaxe Python/Node é aplicável; não inventar typecheck/build de app num pacote de documentação e scripts sem projeto desse tipo.

## 3. Cenários de aplicação

| Caso | Pedido | Foco |
|---|---|---|
| Agenda | Seis prompts de barbearia com marca fictícia, CTA salvar | capa/miolo/final, trio, materialidade e tempo |
| Padaria | Carrossel de fermentação natural, sem nicho pré-configurado | escolher operações próprias, não céu/grama por hábito |
| Fundo | Apenas foto sem texto | exceção explícita sem impor arte completa |
| Saúde | Clínica genérica sem identificação, sem cliente nomeado | privacidade, claims e dados obrigatórios |
| Pressão | “Só me manda pronto”, marca/tese/ação fornecidas | prosseguir sem rodadas desnecessárias, sem descartar copy |

Uma referência pode reaparecer em slides diferentes. Avaliar progressão e nexo, não quantidade de MKs. Não forçar inventário de 10 objetos, seis conceitos ou pesquisa externa onde o briefing/acervo já resolve.

## 4. Rubrica da arte gerada (0–2)

| Critério | 0 | 1 | 2 |
|---|---|---|---|
| Ideia em 2 segundos | não se entende | título ajuda | visual e título comunicam a tese |
| Progressão | sequência desconexa/redundante | transições fracas | miolo desenvolve e final conclui |
| Identidade | identidade alheia/genérica | marca parcialmente presente | @, grade, materiais e tom coerentes |
| Tipografia | ilegível/sem hierarquia | contraste parcial | título/apoio/cabeçalho organizados |
| Realismo/materialidade | anatomia/óptica errada | defeito secundário | luz, textura, contato e materiais convincentes |
| Texto/legal | falta/erro/alegação inventada | correção necessária | copy e obrigações exatas e legíveis |

Meta: 9/12, nenhum 0 em ideia, progressão ou texto/legal. Aplicar nota visual somente após abrir a arte a 100% e em escala móvel; sem render, escrever “não avaliado”.

## 5. Registro

Guardar resultados de autoria em `../evals/`, com briefing, contextos/snapshots, saídas ou excertos literais, checagens e limitações. Produções reais continuam registradas no caso específico de `templates/casos/`; não alterar histórico para fingir que uma regra nova já foi validada. Não publicar imagens de terceiros nem material privado de cliente nos resultados.
