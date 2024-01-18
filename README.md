Esse projeto é a resolução de um desafio proposto pela Rocketseat.
A ideia é desenvolver um programa simples para gerenciar uma lista de contatos utilizando conceitos vistos durante as aulas introdutórias de Python.

Alguns desses conceitos são:
### Funções:
  - São definidas pelo 'def'. Neste projeto cada função é responsável por uma tarefa, o que facilita a compreensão, manutenção e reutilização do código. Os nomes também foram definidos visando a clareza do que cada função realiza.
  - Ex: def adicionar_contato(contatos, nome_contato, telefone, email):
      - Adiciona um novo contato à lista de contatos; Recebendo como parâmentros o nome, telefone e email do contato.
      - Define o contato como não favorito por padrão.
      - Exibe uma mensagem informando que o contato foi adicionado com sucesso.

  
### Listas:
* São estruturas de dados que permitem armazenar múltiplos valores em uma única variável.<br>
No caso a lista contatos armazena os detalhes de cada contato.


### Estruturas de Dados (Dicionários):
* Dicionário é uma coleção não ordenada de pares chave-valor.
* Os contatos são representados como dicionários, permitindo associar informações (como nome, telefone, email e favorito) a chaves específicas.<br>
    Ex: pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}


### Loop:
* É uma estrutura que permite repetir um bloco de código enquanto uma condição for verdadeira. Automatizar tarefas repetitivas e executar ações repetidas vezes.
* Utilizando um loop while True para criar um menu interativo, permite que o usuário realize diversas operações sem que o programa finalize. A finalização só ocorre quando o usuário escolher sair.
E para isso utilizamos o break.

  
### Controle de Fluxo (Condicional if-elif-else):
* O código utiliza estruturas condicionais para executar diferentes blocos de código com base na escolha do usuário no menu.


### Entrada do Usuário (input):
* A função input é utilizada para receber entradas do usuário, permitindo que ele interaja com o programa.


### Enumeração (enumerate):
* A função enumerate é usada para obter tanto o índice quanto o valor durante a iteração sobre a lista de contatos. Dessa forma o usuário poderá selecionar corretamente o indice de cada contato.

  
### Compreensão de Listas ([contato for contato in contatos if contato["favorito"]]):
* A lista de favoritos é gerada usando uma compreensão de lista para filtrar os contatos marcados como favoritos.


### Tratamento de exceções:
* No código em algumas funções foi adicionada uma nova variável para transformar o input do usuário que seria um str para um número inteiro com o int(). Isso para lidar com possíveis erros quando o usuário for selecionar o indice desejado.<br
Isso porque o sistema não iria identificar, já que o indice é um número inteiro e a entrada do usuário uma string.
