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

    def is_classic(self):
        return self.year < 1970

class EBook(Book):
    def __init__(self, title, author, pages, genre, year, file_format, file_size):
        super().__init__(title, author, pages, genre, year)
        self._file_format = file_format
        self._file_size = file_size

    def display_info(self):
        super().display_info()
        print(f"Формат файла: {self._file_format}")
        print(f"Размер файла: {self._file_size} MB")

class Audiobook(Book):
    def __init__(self, title, author, duration, genre, year):
        super().__init__(title, author, None, genre, year) 
        self.duration = duration

    def display_info(self):
        super().display_info()
        print(f"Длительность: {self.duration} часов")
my_ebook = EBook("1984", "Джордж Оруэлл", 328, "Драма", 1949, "PDF", 1.2)
my_audiobook = Audiobook("1984", "Джордж Оруэлл", 11.5, "Драма", 1949)
books = [my_ebook, my_audiobook]
for book in books:
    book.display_info()
    print()
