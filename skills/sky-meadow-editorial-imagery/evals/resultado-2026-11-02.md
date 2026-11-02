# Meadow — evidência da revisão de 02/11/2026

## Escopo

Atualização de instruções, repertório e ferramentas; **não treinamento de pesos** do modelo de imagem. O corpus fornecido contém 70 originais (26 MK, 10 IG, 16 R, 18 N) e quatro índices. Todos os originais foram abertos individualmente; a leitura reaproveitável está em `../references/leitura-do-acervo.md`. Nenhuma nova imagem de terceiro foi publicada ou anexada a gerador.

## Comparação comportamental

Microavaliação com cinco chamadas independentes por variante, contexto novo, mesmo briefing e mesmas fichas visuais fornecidas. Runtime: `completion(model=default)`, sem ferramentas ou imagens. As quinze saídas literais e hashes dos contextos estão em `micro-2026-11-02.json`. Critérios abaixo foram lidos manualmente, não estimados por contagem de palavras.

| Critério / amostras atendidas | Controle sem skill | Versão anterior | Versão revisada |
|---|---|---|---|
| @ central na capa | 0/5 | 5/5 | 5/5 |
| Trio na capa com @ central | 0/5 | 0/5 | 5/5 |
| Copy dentro de cada prompt | 5/5 | 5/5 | 5/5 |
| Contador dentro de cada prompt | 5/5 | 0/5 | 5/5 |

A versão anterior **já** entregou copy e relação temática nesta amostra; não se atribui à microavaliação uma falha que ela não mostrou. As melhorias medidas aqui são trio e autonomia do contador. Não houve avaliação de qualidade de imagem nem prova de que toda geração futura terá o mesmo resultado.

Excertos anteriores: `"@agenda.demo" centered at x=50%, baseline y=6%` sem laterais; contador descrito fora dos blocos como `aplicar depois, em camada tipográfica`. Excertos revisados: `"AGENDA" at x=6%`, `"@agenda.demo" at x=50%`, `"BARBEARIA" at x=94%` e `"01 / 03"` dentro do primeiro bloco.

## Aplicações com consulta real

- **Agenda, seis slides:** contexto novo, preflight local, índice MK e pixels de MK15, MK22 e IG03; confirmações, duração e intervalos desenvolvidos no mesmo universo, sem copiar o exemplo pronto. QA posterior acrescentou as notas de movimento e trocou uma palavra bloqueada que aparecia numa exclusão; seis prompts então passaram no linter com zero erros/avisos. Saída original foi preservada localmente para não reescrever a evidência.
- **Padaria, três slides:** consulta a MK15, MK04 e MK12; massa, bolhas, textura e tempo como assunto, sem paisagem/vidro gratuitos nem tempos universais inventados. Revisão textual manual, sem render.
- **Fundo explícito:** saída preserva fotografia sem lettering; indica `--background-only`, sem impor @ ou contador.
- **Saúde sob pressão:** recusa de resultado garantido e credenciais inventadas; cliente não ativado; publicação não aprovada sem identificação profissional verdadeira.

As aplicações produziram prompts, não imagens. Não se afirma contraste, anatomia, grafia renderizada ou publicação final aprovados.

## Scripts e smoke observados

- Antes da implementação, seis regressões falharam no contrato antigo. Uma regressão adicional expôs falso conflito de área local vazia. A revisão independente encontrou campos em colchetes, copy vazia e ressalva de lista fechada; os três casos foram reproduzidos antes de corrigir.
- Resultado final: **10 testes unittest aprovados**. Exercitam os CLIs reais, sem mocks nem chamadas de API.
- Exemplo de seis slides: **6 prompts, 0 erros, 0 avisos** no linter.
- `generate.py --dry-run`: requisição **4:5 / 2K**, sem anexos, nota de referência removida e câmera registrada. Não importa SDK nem chama API.
- `kit_overlay.mjs`: seis SVGs reais produzidos; página intermediária e final rasterizadas para inspeção. Fração e régua proporcional corretas; final sem arraste. Prévia composta sobre creme foi inspecionada. Não é render de arte Gemini.
- Validador de skill: `Skill is valid!`; frontmatter com 403 caracteres. Sintaxe Python compilada e Node verificada. Não existe app TypeScript/build de frontend neste pacote; não foi alegado typecheck ou build desses tipos.

## Revisão independente e integração

Eixos separados de qualidade e especificação encontraram cinco problemas concretos; foram corrigidos e os mesmos revisores confirmaram a resolução pontual, sem executar testes em paralelo.

A fonte local estava atrás de `origin/main`: a curadoria remota de 29/10/2026 retirou G/IG/D do pacote público. A integração preserva essas remoções; não restaura imagens no Git. A distinção público/local foi incorporada às instruções.

Após integrar os catálogos: **público — 27 arquivos verificados, 47 fichas sem pixels; local — 112 arquivos verificados, nenhum item sem pixels**. Ambos os preflights retornaram acervo OK e clientes desligados. O catálogo local foi preservado por SHA256; não foi substituído pelo catálogo público. A alteração pré-existente `scripts-build.py` na raiz ficou fora dos commits da revisão.
