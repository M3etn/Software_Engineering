def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            if not content:
                raise ValueError("файл пустой")
            print("Содержимое файла:")
            print(content)
    except ValueError as e:
        print(e)
    except FileNotFoundError:
        print("Файл не найден")

read_file("test.txt")
