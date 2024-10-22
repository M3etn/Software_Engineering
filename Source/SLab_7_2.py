import csv
import os

FILENAME = 'expenses.csv'
def add_expense(date, amount, category, description):
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])
def display_expenses():
    if not os.path.exists(FILENAME):
        print("Файл с расходами не найден.")
        return
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        print("Данные о расходах:")
        for row in reader:
            print(f"Дата: {row[0]}, Сумма: {row[1]}, Категория: {row[2]}, Описание: {row[3]}")
def main():
    while True:
        print("\n1. Добавить расход")
        print("2. Показать расходы")
        print("3. Выход")
        choice = input("Выберите опцию: ")

        if choice == '1':
            date = input("Введите дату (ГГГГ-ММ-ДД): ")
            amount = float(input("Введите сумму: "))
            category = input("Введите категорию: ")
            description = input("Введите описание: ")
            add_expense(date, amount, category, description)
            print("Расход успешно добавлен.")

        elif choice == '2':
            display_expenses()

        elif choice == '3':
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод. Пожалуйста, выберите еще раз.")

if __name__ == "__main__":
    main()
