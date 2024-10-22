FILENAME = 'books.txt'

def main():
    books = []
    while True:
        choice = input("1. Добавить книгу\n2. Показать книги\n3. Выход\nВыберите опцию: ")
        if choice == '1':
            book = input("Введите название книги: ")
            books.append(book)
            with open(FILENAME, 'a') as f: f.write(book + '\n')
        elif choice == '2':
            with open(FILENAME, 'r') as f: print(f.read())
        elif choice == '3':
            break
        else:
            print("Неверный ввод.")

if __name__ == "__main__": main()
