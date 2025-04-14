from view import View
from model import BookModel

class Controller:
    def __init__(self):
        self.view = View()
        self.model = BookModel()

    def run(self):
        while True:
            option = self.view.show_menu()

            if option == 1:
                self.add_book()
            elif option == 2:
                self.list_books()
            elif option == 3:
                self.remove_book()
            elif option == 4:
                self.view.show_message("Saindo do sistema...")
                break
            else:
                self.view.show_message("Opção inválida!")

    def add_book(self):
        book = self.view.get_book_info()
        if book:
            self.model.add_book(book)
            self.view.show_message("Livro adicionado com sucesso!")

    def list_books(self):
        books = self.model.get_all_books()
        self.view.show_books(books)

    def remove_book(self):
        books = self.model.get_all_books()
        self.view.show_books(books)
        try:
            index = int(input("Digite o número do livro para remover: ")) - 1
            if self.model.remove_book(index):
                self.view.show_message("Livro removido com sucesso.")
            else:
                self.view.show_message("Índice inválido.")
        except ValueError:
            self.view.show_message("Erro: entrada inválida.")
