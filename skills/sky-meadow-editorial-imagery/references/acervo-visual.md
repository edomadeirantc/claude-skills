# Acervo visual — pacote público

## Consulta obrigatória antes de cada prompt

1. Consulte `assets/catalogo.json`, cujos caminhos são relativos à raiz da skill, e abra o [índice das gerações aprovadas](../assets/indices/geracoes-aprovadas.jpg). O índice serve para selecionar, não substitui a leitura dos pixels das imagens escolhidas.
2. Abra **2–4 imagens pertinentes**, sem carregar todo o acervo a cada criação. Nesta distribuição há doze imagens-base: [G01](../assets/aprovadas/g01-casal-grama-mobile.png) e [G02](../assets/aprovadas/g02-perfis-frente-a-frente-mobile.jpg) (golden) e IG01–IG10 (carrosséis de referência, passo 5). Para peças das famílias A–E abra G01/G02; para uma questão não coberta, solicite outra referência autorizada, em vez de alegar acesso a imagens privadas.
3. Leia a imagem real, não apenas o nome: sujeito/gesto, enquadramento, luz, textura de pele e cabelo, espaço para copy, hierarquia tipográfica e comportamento do vidro. Registre os IDs consultados, duas observações concretas e o princípio a transferir. Para o sistema de pequenos textos editoriais, consulte também [Microtipografia editorial](microtipografia-editorial.md), sem atribuir a esses golden detalhes que não exibem.
4. Compare o conceito com os golden e faça o teste antirréplica: repetir sujeito + gesto + enquadramento de uma referência, mudando apenas a cor ou o texto, continua sendo repetição. Uma peça nova deve trazer outro gesto ou cena, mesmo se usar um golden autorizado para continuidade.
5. **Carrossel de Instagram, nicho de conversão ou SaaS de feed:** abra o [índice IG](../assets/indices/carrosseis-ig.jpg) e 2–3 arquivos de `assets/carrosseis/` (caminhos relativos à raiz da skill) do mesmo papel da peça: capa, miolo ou fechamento. Na Família F, essas IG contam no limite de 2–4 imagens no lugar de G01/G02; abra G01/G02 só se a série reaproveitar suas pessoas, luz ou interface. Leia nelas as posições do @, do título, da pílula, dos pontos e do rodapé antes de escrever as porcentagens do prompt.

### Leitura visual disponível

- **G01:** casal deitado na grama, enquadrado de cima; vegetação verde desfocada na parte superior; combinação de serif itálica e sans; rostos na metade inferior, CTA fino de contorno. Título e espaço negativo estão integrados à vegetação, não a um card branco opaco.
- **G02:** rostos de perfil se tocando contra céu azul; textura de pele, barba e fios de cabelo visíveis; título serif no céu; pequenas tags translúcidas com conectores e CTA de contorno. O céu sustenta a hierarquia sem cobrir o casal com um grande painel.
- **IG01–IG10:** carrosséis de feed (originais 1080×1440) em três papéis — capa (IG01, IG02, IG04, IG05, IG06, IG09, IG10), miolo (IG07) e fechamento (IG03, IG08). Base escura que nasce da própria foto, título gigante na base, um acento por série, @ no topo, pontos com losango, numeração e "ARRASTA →". Fichas em `referencias.md §1.3`; sistema em `familia-social-conversao.md`.

Não há marca do cliente visível em G01/G02. Foram mantidas em seus bytes e dimensões originais: G01 em PNG, 941 × 1672; G02 em JPEG, 1536 × 2752.

Para a grade de três rótulos, abra também a [demonstração técnica D01](../assets/indices/microtipografia-exemplo.png): rótulos próprios sobrepostos por Pillow à G02 inteira, sem recorte, nas âncoras 6%/50%/94% e linha-base a 6% da altura. D01 é referência técnica da grade, **não** peça aprovada, nova geração ou prova de que uma IA produziu o texto. Não substitui os golden originais. A medição integrada comparou 5.949 pixels brancos puros dos glifos com os mesmos pixels da foto-base: contraste de 4,248:1 a 5,348:1. O mínimo fica abaixo de 4,5:1 para texto pequeno; **não é demonstração aprovada de acessibilidade** e exige adequação de contraste para uso final.

### Consultar não é anexar ao gerador

**Consultar** é abrir os pixels para análise pelo assistente. **Anexar** é transmitir a imagem ao gerador como identidade, referência ou base de edição. Consulta não implica envio, nem concede licença de anexo.

- G01/G02 foram explicitamente autorizadas pelo usuário como referências; podem ser anexadas quando necessário à continuidade visual. Declare quais imagens foram efetivamente enviadas.
- R01–R16 e N01–N18: somente estudo, sem autorização de redistribuição ou anexo ao gerador. Seus arquivos não estão neste pacote.
- IG01–IG10: enviadas pelo usuário e publicadas no pacote a pedido dele, para **consulta** ao escrever prompts. Não anexar ao gerador: contêm pessoa pública (IG01), nome e @ de terceiro (IG01, IG06–IG08) e modelos de terceiros. Extraia estrutura, zonas, acento e tipografia; nunca pessoas, nomes, @ ou textos.
- H01/H02: históricos privados, não golden e não usar como alvo final ou anexo de referência.
- Se o serviço não aceitar anexos, descreva os princípios observados e informe a limitação; não afirme que a geração foi condicionada por arquivos que não recebeu.

## Inventário e limite da distribuição

| Grupo | Acervo local privado | Pacote público |
|---|---|---|
| R01–R16 | 16 originais recuperados e 16 miniaturas | Somente metadados: `distribuido=false`, `caminho=null` |
| N01–N18 | 18 originais recuperados e 18 miniaturas | Somente metadados: `distribuido=false`, `caminho=null` |
| G01/G02 | 2 golden aprovados | 2 imagens próprias autorizadas, sem marca visível, em qualidade original |
| H01/H02 | 2 versões anteriores com marca visível | Somente metadados; imagens não publicadas nem editadas para ocultar marca |
| S01–S05 | 5 anexos reais recuperados da conversa, somente privados | Somente metadados; nenhum screenshot ou miniatura distribuído |
| IG01–IG10 | 10 carrosséis de feed enviados pelo usuário, 1080×1440 | 10 imagens em `assets/carrosseis/`, publicadas por decisão do usuário, só para consulta |
| Índices | 5 folhas: R, N, G/H, S e IG | 2 folhas: G01/G02 e IG01–IG10 |
| D01 | 1 demonstração técnica derivada de G02 | Mesmo arquivo técnico; não é golden |

O local preserva 53 imagens únicas de conteúdo: 34 fontes de terceiros, 10 carrosséis IG, 2 golden, 2 históricas e 5 screenshots da conversa. A distribuição pública contém **12 imagens-base (G01/G02 e IG01–IG10), 2 índices derivados e 1 demonstração tipográfica derivada**. Os registros de arquivos privados no catálogo não são links para imagens públicas: `caminho=null` evita prometer arquivos inexistentes.

A recuperação local usou apenas dois arquivos compactados já fornecidos (16 + 18 referências) e os cinco nomes de imagens explicitamente mencionados na conversa. Os 34 originais foram relacionados às miniaturas por comparação de pixels e revisão visual. Os cinco arquivos nomeados foram encontrados: dois eram aliases exatos de G01/G02 por SHA256, dois eram históricos privados e um era N12, já pertencente ao acervo de terceiros. Nada foi buscado entre imagens não relacionadas.

O arquivo de nome hexadecimal indicado como candidato no arquivo compactado era **N12**, com mãos de dedos enganchados, tags de saúde e marca de terceiro; não era uma geração própria desktop aprovada. Nenhum novo golden desktop foi criado. Um eventual desktop próprio aprovado adicional **não foi recuperado** entre esses caminhos.

Foram recuperados também **cinco anexos reais de imagem das mensagens do usuário**, resolvendo somente seus blobs locais explicitamente identificados, sem copiar a transcrição: S01–S03 são screenshots de iterações da arte na grama, S04 é uma colagem com material de terceiros e S05 é uma seção de site com marca. Todos permanecem locais, com SHA256 e dimensões no catálogo; não foram recortados, promovidos a golden ou publicados, nem em miniatura. Screenshots não equivalem aos arquivos originais em alta resolução das artes que mostram. A recuperação não alega arquivos adicionais além dos inventariados.

## Direitos e fallback honesto

Veja [Aviso dos assets](../assets/NOTICE.md). Publicação autorizada pelo usuário e permissão de usar G01/G02 como referência não atestam exclusividade, autoria jurídica ou licença ampla de terceiros. Não atribua licença MIT às imagens por herança da licença do código/documentação. Nenhuma foto foi editada, recortada ou teve crédito removido para tornar-se publicável.

`assets/.gitignore` impede inclusão acidental das pastas privadas `referencias/`, `originais/`, `historico/` e `conversa/` em uma sincronização futura. Não protege contra `git add -f` e não sanitiza metadados: o catálogo público também precisa permanecer sem caminhos pessoais, nomes do cliente ou links para arquivos privados. Não copiar o catálogo local diretamente para o público.

As descrições de R/N em outros módulos são notas textuais de análise anterior, não evidência de pixels presentes nesta instalação. Se os arquivos não estiverem disponíveis, **não alegue tê-los aberto ou usado como referência visual**. Abra G01/G02 como as duas referências disponíveis e explique o limite caso não sejam pertinentes. Para obter 3–4 imagens ou uma família não coberta, peça material autorizado ao usuário. Não baixe substitutos de terceiros para contornar a restrição. Com originais autorizados fornecidos em outra sessão, selecione somente 2–4 pertinentes e respeite as permissões individuais.
