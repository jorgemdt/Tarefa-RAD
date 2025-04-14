from model import Book

class View:
    def show_menu(self) -> int:
        print("\n--- Menu ---")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Remover Livro")
        print("4. Sair")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    def get_book_info(self) -> Book:
        try:
            title = input("Título: ")
            author = input("Autor: ")
            year = int(input("Ano: "))
            return Book(title, author, year)
        except ValueError:
            self.show_message("Erro: Ano deve ser um número inteiro.")
            return None

    def show_books(self, books: list):
        if not books:
            print("Nenhum livro cadastrado.")
            return
        for idx, book in enumerate(books):
            print(f"{idx + 1}. {book}")

    def show_message(self, message: str):
        print(f"\n{message}")
