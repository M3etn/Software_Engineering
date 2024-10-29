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

class EBook(Book):
    def __init__(self, title, author, pages, genre, year, file_format, file_size):
        super().__init__(title, author, pages, genre, year)
        self.file_format = file_format
        self.file_size = file_size

    def display_info(self):
        super().display_info()
        print(f"Формат файла: {self.file_format}")
        print(f"Размер файла: {self.file_size} MB")
my_ebook = EBook("1984", "Джордж Оруэлл", 328, "Драма", 1949, "PDF", 1.2)
my_ebook.display_info()
if my_ebook.is_classic():
    print(f"'{my_ebook.title}' считается классикой.")
else:
    print(f"'{my_ebook.title}' не является классической книгой.")
