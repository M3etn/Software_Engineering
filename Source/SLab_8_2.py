class Book:
    def __init__(self, title, author, pages, genre, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
        self.year = year

    def display_info(self):
        print(f"Книга: '{self.title}'")
        print(f"Автор: {self.author}")
        print(f"Количество страниц: {self.pages}")
        print(f"Жанр: {self.genre}")
        print(f"Год выпуска: {self.year}")

    def update_pages(self, new_pages):
        self.pages = new_pages
        print(f"Количество страниц обновлено на {new_pages}.")

    def is_classic(self):
        return self.year < 1970
my_book = Book("1984", "Джордж Оруэлл", 328, "Драма", 1949)
my_book.display_info()
my_book.update_pages(350)
if my_book.is_classic():
    print(f"'{my_book.title}' считается классикой.")
else:
    print(f"'{my_book.title}' не является классической книгой.")
