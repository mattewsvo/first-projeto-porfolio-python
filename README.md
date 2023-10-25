# first-project-porfolio-python
Documentação do projeto "first-projeto-portifolio-python".
O projeto consiste em um sistema que integra dados inseridos pelo usuário a um banco de dados. O usuário consegue cadastrar um produto (com campos como descrição do produto, unidade de medida e quantidade) e também visualizar quais cadastros ja foram feitos no banco de dados. 
Todo o processo está comentado para facilitar o entendimento de cada linha de código.

Pontos importantes desse sistema:

- Tem uma forte cultura de tratamento de erros, possuindo duas funções complexas que integram vários conceitos, afim de moldar e inserir os dados captados, dentro do banco de dados sqlite3.
  
- As funções são associadas aos botões da janela gráfica principal e são acionadas quando os botões são clicados, trazendo mais dinâmica e menos lentidão para as respostas do Python.
  
- Tanto as janelas gráficas quanto o banco de dados foram desenvolvidos em Python, utilizando bibliotecas importantes e poderosas, como a tkinter, sqlite3 e a datetime.
  
- Tem uma forte cultura de código limpo, sendo direto, claro e conciso.

Dificuldades encontradas:

- Trabalhar com as estruturas de dados, relacionar e integrar esses dados ao banco não se mostrou uma tarefa fácil. Em vários momentos, me deparei com erros de sintaxe ou erros causados, por essas estruturas, que não possuíam determinadas funções. Isso me fez pesquisar e aprender como associar as estruturas e conseguir introduzir tudo no banco de dados.
  
- Outro problema foi a forma como os dados eram injetados na tabela, às vezes duplicados, às vezes com algum índice faltando. Por esse motivo, foram implementadas saídas de dados de segurança, para conferir o tráfego dos dados e facilitar a manutenção.

Conclusão:

Embora seja um projeto de nível júnior, ele me ajudou a analisar pontos de melhoria e lacunas onde a integração entre os processos não estava ideal. Como é um projeto que trabalha com conceitos complexos, tive a oportunidade de desenvolver várias habilidades.
