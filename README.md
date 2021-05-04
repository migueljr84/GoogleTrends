# GoogleTrends
Pessoal da minha timeline, veno disponibilizar um código O que as pessoas estão pesquisando no Google?

Por acaso você conhece o Google Trends? 
Ele é um portal do Google que permite "pesquisar sobre as pesquisas no Google". Cada pesquisa no Google fica registrada, bem como todos os termos relacionados, e o Google disponibiliza um portal para que possamos pesquisar e analisar quais são as tendências relacionadas a palavras-chave e a um país específico.
Essa ferramenta ( Google Trends ) no qual o  Google disponibiliza é bastante usado por profissionais de Marketing Digital.

E por que não extrair esses dados e analisá-los?

É o que mostrarei nesta publicação agora neste Lab.

Com esse código inclusive estou disponibilizando no meu GitHub para livre utilização, podemos obter os resultados das tendências (e muito mais) no site de tendências do Google usando Python.
Neste caso não precisamos pesquisar e copiar manualmente os resultados de tendências, a API Python chamada pytrends faz o trabalho para nós.

Através deste exemplo que publico, poderíamos automatizar e gerar um DashBoard dinâmico de forma diária, tendo uma visibilidade de tedência por uma área específica, indústria, empresa, personagem, etc.

Poderíamos monitorar um assunto específico ou até mesmo uma empresa, e caso atingíssimos um ''pico'' por exemplo, teríamos uma visibilidade em tempo real para realizar uma análise para tal, como por exemplo investir no mercado financeiro no papel desta empresa no qual está sendo monitorada.

Neste exemplo do código, gerei uma pesquisa de personagens políticos, neste caso buscando um histórico de pesquisas relacionadas ao Bolsonora, Lula e Ciro Gomes.

Com o que já definido, defini um períodos nos últimos 3 anos para a região do Brasil.

Em resumo, irei buscar todas as tendências que ocorreram no Google que aconteceu no Brasil relacionado ao Bolsonaro, Lula e Ciro Gomes nos últimos 3 anos.

O código encontra-se no arquivo GoogleTrends.py
