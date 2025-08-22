class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def info(self):
        return f"Book: {self.title}, de catre {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size, format):
        super().__init__(title, author)
        self.file_size = file_size
        self.format = format
    def info(self):
        return f"EBook: '{self.title}', de {self.author}, file size: {self.file_size} MB, format: {self.format}"

class Library:
    def __init__(self):
        self.Books = []


    def add_book(self, book):
        if isinstance(book, Book):
            self.Books.append(book)
    def list_books(self):
        for book in self.Books:
            print(" -", book.info())
    def total_size(self):
        total = sum(book.file_size for book in self.Books if isinstance(book, EBook))
        return total


if __name__ == "__main__":
    book1 = Book("Pe urmele șamanului albastru", "Miruna Drăghici")
    book2 = EBook("Moromeții", "Marin Preda",5.4,"PDF")
    book3 = EBook("Istorii cu Vlad Țepeș", "Miruna Drăghici", 7.2, "txt")

    library = Library()

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.list_books()

    print(f"\nSpatiul total ocupat de ebooks: {library.total_size():.2f} MB ")



