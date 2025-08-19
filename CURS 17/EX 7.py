class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"

class Library:
    def __init__(self,):
        self.books = []
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Error you can add only book objects")
    def find_book(self, author):
        return [book for book in self.books if book.author.lower() ==  author.lower()]

    def list_books(self):
        if not self.books:
            print("No books found")
        else:
            print("Carti in bibilioteca:")
            for book in self.books:
                print(f" - {book}")


if __name__ == "__main__":
    book1 = Book("Pe urmele șamanului albastru", "Miruna Drăghici")
    book2 = Book("Moromeții", "Marin Preda")
    book3 = Book("Istorii cu Vlad Țepeș", "Miruna Drăghici")

    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    library.list_books()

    print("\nCarti scrise de Miruna Drăghici")
    for book in library.find_book("Miruna Drăghici"):
        print(f" - {book}")
