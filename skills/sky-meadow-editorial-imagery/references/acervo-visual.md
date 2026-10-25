# Acervo visual — consulta obrigatória antes de cada prompt

O acervo foi **curado pelo usuário em 25/10/2026**: ficaram só as imagens que
ele considera as melhores. Elas são a régua de qualidade. Nenhuma é molde:
de cada uma sai um movimento, uma decisão de tipografia ou de luz; a cena
nasce do cliente (`repertorio-mercado.md §R.3`).

## Passos

1. **Preflight:** `python "<raiz-da-skill>/scripts/check_assets.py"`. Erro em
   arquivo declarado presente bloqueia o trabalho: informe o ID e restaure a
   cópia conhecida. Sem rede, sem busca no PC.
2. **Escolha pelo tipo de peça**, não pela família de costume. Abra o índice
   e depois 2–4 imagens em tamanho integral:

   | Peça | Abra primeiro | Índice |
   |---|---|---|
   | Post único, anúncio, capa de alto impacto, slide | 2–3 MK do movimento pretendido | `assets/indices/mercado-mk.jpg` |
   | Carrossel de conversão (kit de sequência, @, pílula) | 1–2 IG do mesmo papel (capa, miolo, fechamento) **e** 1–2 MK para o movimento | `carrosseis-ig.jpg` + `mercado-mk.jpg` |
   | Hero web ou peça de paisagem (céu, campo, vidro) | 2–3 R/N (só instalação local) ou G01/G02 | `referencias-R.jpg`, `referencias-N.jpg`, `geracoes-aprovadas.jpg` |
   | Continuidade com o caso telemedicina | G01/G02 | `geracoes-aprovadas.jpg` |

   Carrossel: escolha **uma MK diferente por slide** (`repertorio-mercado.md §R.5`).
3. **Leia os pixels**, não o nome: sujeito e gesto, escala, enquadramento,
   luz, tipografia (famílias, troca de voz, tamanho relativo), onde está o
   texto e quanto texto há, acento. Registre por imagem: ID, duas observações
   concretas e o **verbo** do movimento.
4. **Teste anti-réplica:** lado a lado com a referência, a peça nova não pode
   ser "a mesma cena com outro texto". Mude sujeito, cena e gesto; mantenha
   só o movimento.

## Clientes: desligados por padrão

`clientes/{cliente}/` (só na instalação local: ficha, artes RC, prompts) é
**aberto somente quando o usuário nomeia o cliente no chat** (pelo nome da
pessoa ou da empresa). Pedido de nicho parecido sem o nome (clínica, HOF, segurança)
usa os templates públicos T4/T5 e o acervo geral; não lê a ficha nem abre
as artes do cliente, e não usa o nome, o logo ou as cores dele.

Com o cliente nomeado: abra a `ficha.md`, o `indice-*.jpg` e 2–3 peças do
mesmo tipo. Elas valem como estrutura aprovada; o texto só vale se a ficha
disser que vale.

## Consultar não é anexar ao gerador

Consultar é abrir os pixels para análise. Anexar é enviar ao gerador.

| Grupo | Consultar | Anexar ao gerador |
|---|---|---|
| MK01–MK26, IG01–IG10 | sim (publicadas por decisão do usuário) | **não**: têm marcas, @, pessoas e obras de terceiros |
| R01–R16, N01–N18 | sim, só na instalação local | **não** |
| G01/G02 | sim | sim, para continuidade do mesmo casal e luz |
| RC (cliente) | só com o cliente nomeado | **não**; o retrato da profissional vem de foto real enviada por ela |
| D01 (grade de rótulos sobre G02) | sim, como exemplo técnico | não |

Declare quais imagens foram de fato anexadas. Se o gerador não aceita
anexos, descreva os princípios observados; não alegue condicionamento por
arquivo que ele não recebeu.

## Inventário

| Grupo | Instalação local | Pacote público (GitHub) |
|---|---|---|
| MK01–MK26 | `assets/mercado/` | mesmo |
| IG01–IG10 | `assets/carrosseis/` | mesmo |
| R01–R16, N01–N18 | `assets/originais/` + miniaturas em `assets/referencias/` | só metadados (`caminho=null`) |
| G01/G02, D01 | `assets/aprovadas/`, `assets/indices/` | mesmo |
| RC (cliente de saúde) | `clientes/{cliente}/artes/` | só metadados; nunca publicado (pacientes) |

Fonte única de caminhos, hashes e permissões: `assets/catalogo.json`. No
pacote público, `caminho=null` é limite de distribuição, não arquivo perdido:
não alegue ter aberto o que não está na instalação. Direitos em
`../assets/NOTICE.md`; a licença do código não vale para as imagens.
