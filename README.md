# Tarefa-RAD

# Gerenciador de Livros - Documentação

## Visão Geral

Este projeto é um sistema simples de gerenciamento de livros implementado em Python, seguindo o padrão MVC (Model-View-Controller). Ele permite adicionar, listar e remover livros de um banco de dados SQLite.

## Estrutura do Projeto

```
.
├── model.py      # Lógica de dados e banco de dados
├── view.py       # Interface com o usuário
├── controller.py # Lógica de controle do programa
└── main.py       # Ponto de entrada do aplicativo
```

## Pré-requisitos

- Python 3.x
- Módulo sqlite3 (incluído na biblioteca padrão do Python)

## Instalação

1. Clone o repositório ou baixe os arquivos do projeto
2. Navegue até o diretório do projeto no terminal
3. Execute o programa com:

```bash
python main.py
```

## Documentação dos Arquivos

### model.py

Define as classes `Book` e `BookModel` para manipulação dos dados.

#### Classe Book
- **Atributos**:
  - `title`: Título do livro (string)
  - `author`: Autor do livro (string)
  - `year`: Ano de publicação (inteiro)

- **Métodos**:
  - `__str__()`: Retorna uma representação formatada do livro (ex: "Título - Autor (Ano)")

#### Classe BookModel
- **Métodos**:
  - `__init__(db_name='books.db')`: Inicializa a conexão com o banco de dados
  - `create_table()`: Cria a tabela 'books' se não existir
  - `add_book(book: Book)`: Adiciona um livro ao banco de dados
    - **Entrada**: Objeto Book
    - **Processo**: Insere os dados na tabela books
    - **Saída**: Nenhuma (banco de dados atualizado)
  - `get_all_books() -> list`: Retorna todos os livros do banco de dados
    - **Entrada**: Nenhuma
    - **Processo**: Consulta todos os registros da tabela books
    - **Saída**: Lista de objetos Book
  - `remove_book(index: int)`: Remove um livro pelo índice
    - **Entrada**: Índice do livro na lista
    - **Processo**: Remove o registro correspondente do banco de dados
    - **Saída**: True se removido com sucesso, False se índice inválido

### view.py

Define a classe `View` para interação com o usuário.

#### Classe View
- **Métodos**:
  - `show_menu() -> int`: Exibe o menu principal e obtém a escolha do usuário
    - **Entrada**: Nenhuma
    - **Processo**: Mostra opções e captura entrada do usuário
    - **Saída**: Número da opção escolhida ou -1 para entrada inválida
  - `get_book_info() -> Book`: Obtém informações de um novo livro
    - **Entrada**: Nenhuma
    - **Processo**: Solicita título, autor e ano ao usuário
    - **Saída**: Objeto Book ou None se ano inválido
  - `show_books(books: list)`: Exibe a lista de livros
    - **Entrada**: Lista de objetos Book
    - **Processo**: Formata e exibe cada livro com seu índice
    - **Saída**: Nenhuma (saída para o console)
  - `show_message(message: str)`: Exibe uma mensagem para o usuário
    - **Entrada**: String com a mensagem
    - **Processo**: Exibe a mensagem formatada
    - **Saída**: Nenhuma (saída para o console)

### controller.py

Define a classe `Controller` que coordena modelo e visão.

#### Classe Controller
- **Métodos**:
  - `run()`: Inicia o loop principal do programa
    - **Processo**: Mostra menu e direciona para as operações conforme escolha do usuário
  - `add_book()`: Coordena a adição de um novo livro
    - **Processo**: Obtém dados da view e envia para o model
  - `list_books()`: Coordena a listagem de livros
    - **Processo**: Obtém livros do model e envia para a view exibir
  - `remove_book()`: Coordena a remoção de um livro
    - **Processo**: Lista livros, obtém escolha do usuário e solicita remoção ao model

### main.py

Ponto de entrada do programa. Cria uma instância do Controller e inicia o programa.

## Fluxo do Programa

1. O usuário executa `main.py`
2. O Controller inicia e exibe o menu principal
3. De acordo com a escolha do usuário:
   - **Adicionar livro**: Solicita dados, valida e armazena no banco
   - **Listar livros**: Recupera e exibe todos os livros cadastrados
   - **Remover livro**: Lista livros, solicita qual remover e atualiza o banco
   - **Sair**: Encerra o programa

## Exemplo de Uso

```
--- Menu ---
1. Adicionar Livro
2. Listar Livros
3. Remover Livro
4. Sair
Escolha uma opção: 1
Título: Dom Casmurro
Autor: Machado de Assis
Ano: 1899
Livro adicionado com sucesso!

--- Menu ---
1. Adicionar Livro
2. Listar Livros
3. Remover Livro
4. Sair
Escolha uma opção: 2
1. Dom Casmurro - Machado de Assis (1899)

--- Menu ---
1. Adicionar Livro
2. Listar Livros
3. Remover Livro
4. Sair
Escolha uma opção: 3
1. Dom Casmurro - Machado de Assis (1899)
Digite o número do livro para remover: 1
Livro removido com sucesso.
```

## Observações

- Os dados são persistidos em um arquivo SQLite chamado `books.db`
