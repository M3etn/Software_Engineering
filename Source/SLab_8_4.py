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
        self._file_format = file_format
        self._file_size = file_size

    def display_info(self):
        super().display_info()
        print(f"Формат файла: {self._file_format}")
        print(f"Размер файла: {self._file_size} MB")

    def set_file_format(self, new_format):
        self._file_format = new_format

    def get_file_format(self):
        return self._file_format

    def set_file_size(self, new_size):
        if new_size > 0:
            self._file_size = new_size
        else:
            print("Размер файла должен быть больше нуля.")

    def get_file_size(self):
        return self._file_size
my_ebook = EBook("1984", "Джордж Оруэлл", 328, "Драма", 1949, "PDF", 1.2)
my_ebook.display_info()
my_ebook.set_file_format("EPUB")
my_ebook.set_file_size(1.5)
print("\nПосле обновления информации:")
my_ebook.display_info()
