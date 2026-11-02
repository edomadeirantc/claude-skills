# Acervo visual — consulta obrigatória antes de cada prompt

## Disponibilidade e curadoria

**Pacote público:** preservar a curadoria de 29/10/2026: somente as 26 imagens MK01–MK26 e `assets/indices/mercado-mk.jpg` são distribuídas. G01/G02, IG01–IG10 e D01 permanecem removidas do Git; R/N nunca foram distribuídas. As fichas e a leitura dos 70 originais são conhecimento de direção, não arquivos de imagem.

**Instalação local do treinamento:** o pedido de revisão de 02/11/2026 fornece novamente MK/IG/R/N para estudo privado. Usar os arquivos que o catálogo local declarar presentes e autorizados para consulta. Isso não restaura a distribuição pública nem autoriza anexos ao gerador. Não copiar catálogo público sobre catálogo local: a disponibilidade é específica da instalação.

Fonte única de caminhos, hashes e permissões: `../assets/catalogo.json`. `caminho=null` significa **sem pixels nessa instalação**. Não procurar versões no histórico, baixar cópias externas ou alegar consulta visual a arquivo ausente. Se só houver ficha, declarar “ficha consultada; pixels indisponíveis” e usar MKs disponíveis para decisões que exigem observação visual.

## Passos

1. **Preflight, uma vez por sessão:** `python "<raiz-da-skill>/scripts/check_assets.py"`. Arquivo declarado presente que falha no hash bloqueia: informar ID e restaurar somente cópia conhecida autorizada. Sem busca geral no PC ou recuperação de arquivo retirado.
2. **Estudar tese e papel antes da família.** Ler `direcao-por-pedido.md` e `leitura-do-acervo.md`; consultar o índice MK. Abrir 2–4 candidatas pertinentes disponíveis no catálogo, incluindo a função de capa, explicação e final quando o pedido for carrossel.

   | Papel | Candidatas | Disponibilidade |
   |---|---|---|
   | Capa de hierarquia forte | MK15, MK01; IG01/IG04 como alternativa | MK públicas; IG só se houver caminho local |
   | Miolo de tempo/ordem | MK22, MK04/MK16/MK25 | públicas |
   | Miolo de contraste, componentes e par | R02/R05/R15, N07/N12; MK03/MK06 como alternativas por operação | R/N só quando presentes localmente; MK públicas |
   | Final de salvar/agir | MK12, MK08; IG03/IG08 como alternativa | MK públicas; IG só se houver caminho local |
   | Recurso de app | MK07/17/18/20/23/26 + captura autorizada do produto | MK públicas; captura fornecida pela marca |
   | Continuidade de caso já aprovado | texto do caso e imagem aprovada autorizada disponível | não recuperar G/RC ausente; respeitar ativação de cliente |

   A tabela inicia a seleção, não impõe as mesmas refs em todo pedido. Reutilizar uma referência quando a relação continuar útil, sem exigir uma MK diferente por slide. Não prometer três imagens abertas se só duas estão disponíveis.
3. **Ler pixels, não nomes.** Registrar ID, duas observações concretas, operação visual, frase que ajuda a explicar e diferença proposta da cena. Separar observação e recomendação. Índice visto não equivale a original visto em tamanho integral.
4. **Teste anti-réplica.** A nova peça não pode ser a mesma cena com outra legenda. Criar sujeito, gesto, copy e contexto próprios; transferir relação, hierarquia e luz.

## Clientes: desligados por padrão

`clientes/{cliente}/` permanece desligado. Abrir ficha, índice e artes somente quando o usuário **nomear esse cliente no chat**. Pedido de nicho parecido não ativa dados reais: usar T4/T5 e acervo geral; não listar nem procurar nomes, rostos, cores ou logo de cliente.

Com cliente nomeado, consultar a ficha e os materiais autorizados do mesmo tipo; estrutura aprovada não transforma todo texto antigo em copy reutilizável. Pacientes/RC não são anexos de geração nem material de publicação da skill.

## Consultar não é anexar

| Grupo | Consultar | Anexar ao gerador |
|---|---|---|
| MK01–MK26 | sim, arquivos distribuídos para consulta | não: marcas, pessoas e obras de terceiros |
| IG01–IG10, R01–R16, N01–N18 | somente se presentes no catálogo local; público tem fichas | não |
| G01/G02 | somente se uma cópia local autorizada já estiver declarada; público só ficha | apenas se catálogo autorizar e houver continuidade pertinente; nunca recuperar arquivo retirado |
| D01 | ficha histórica; cópia local, se presente, só demonstra grade | não |
| RC | somente com cliente nomeado e permissão pertinente | não |

Declarar anexos reais separadamente. Caminho ou ID escrito no prompt não envia imagem. Sem suporte a anexos, descrever a operação e não alegar condicionamento por arquivo.

## Inventário por instalação

| Grupo | Instalação local de treinamento | Pacote público |
|---|---|---|
| MK01–MK26 e índice MK | presentes conforme catálogo | distribuídos |
| IG01–IG10 e índice IG | estudo privado quando declarados presentes | metadados; imagens continuam removidas |
| R01–R16, N01–N18 e índices | estudo privado quando declarados presentes | metadados; nunca distribuir |
| G01/G02 e D01 | somente cópias previamente autorizadas e declaradas | metadados; imagens continuam removidas |
| Material de cliente | privado e desligado sem ativação explícita | nunca distribuído |

A revisão usa o acervo completo **local**, sem republicar imagens retiradas do repositório. Direitos em `../assets/NOTICE.md`; a licença do código não concede licença sobre as imagens.
