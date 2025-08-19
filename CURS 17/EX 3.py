class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def tip(self):
        if self.pages > 150:
            return "Roman"
        else:
            return "Nuvela"


if __name__ == "__main__":
    book = Book("Lord of the rings", "Tolkien", 110)
    print(book.tip())