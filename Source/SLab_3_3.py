n = int(input())
if 0 <= n <= 3:
    print('Переменная в диапозоне от 0 до 3')
elif 3 < n < 6:
    print('Переменная в диапозоне от 4 до 5')
elif 6 <= n <= 10:
    print('Переменная в диапозоне от 6 до 10')
else:
    print("Число должно быть в диапазоне от 0 до 10")