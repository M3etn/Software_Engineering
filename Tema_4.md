# Тема 4. Функции и модули
Отчет по Теме #4 выполнил(а):
- Кудренко Денис Валерьевич
- ИВТ-22-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ |---------|
| Задание 1 | + | +       |
| Задание 2 | + | +       |
| Задание 3 | + | +       |
| Задание 4 | + | +       |
| Задание 5 | + | +       |
| Задание 6 | + | -       |
| Задание 7 | + | -       |
| Задание 8 | + | -       |
| Задание 9 | + | -       |
| Задание 10 | + | -       |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Напишите функцию, которая выполняет любые арифметические действия и выводит результат в консоль. Вызовите функцию используя “точку входа”.

```python
def main():
    print(2+2)
if __name__ == '__main__':
    main()
```
### Результат.
![](Pictures/Lab_4_1.jpg)

## Выводы
Научились вызывать функцию использую "точку входа"

## Лабораторная работа №2
### Напишите функцию, которая выполняет любые арифметические действия, возвращает при помощи return значение в место, откуда вызывали функцию. Выведите результат в консоль. Вызовите функцию используя “точку входа”.

```python
def main():
    result = 2 + 2
    return result
if __name__ == '__main__':
    answer = main()
    print(answer)
```
### Результат.
![](Pictures/Lab_4_2.jpg)

## Выводы
Оптимизировали скорость работы предыдущей программы

## Лабораторная работа №3
### Напишите функцию, в которую передаются два аргуфмента, над ними производится арифметическое действие, результат возвращается туда, откуда эту функцию вызывали. Выведите результат в консоль. Вызовите функцию в любом небольшом цикле.

```python
def main(one,two):
    result = one + two
    return result
for i in range(5):
    x = 1
    y = 10
    answer = main(x,y)
    print(answer)
```
### Результат.
![](Pictures/Lab_4_3.jpg)

## Выводы
Создали функцию с двумя аргументами

## Лабораторная работа №4
### Напишите функцию, на вход которой подается какое-то изначальное неизвестное количество аргументов, над которыми будет производится арифметические действия. Для выполнения задания необходимо использовать кортеж “*args”.

```python
def main(x, *args):
    one = x
    two = sum(args)
    three = float(len(args))
    print(f"one={one}\ntwo={two}\nthree={three}")
    return x + sum(args) / float(len(args))
if __name__ == '__main__':
    result = main(10,0,1,2,-1,0,-1,1,2)
    print(f"\nresult={result}")
```
### Результат.
![](Pictures/Lab_4_4.jpg)

## Выводы
Создали функцию с двумя аргументами, но второй из них уже является массивом

## Лабораторная работа №5
### Напишите функцию, которая на вход получает кортеж “**kwargs” и при помощи цикла выводит значения, поступившие в функцию.

```python
def main(**kwargs):
    for i in kwargs.items():
        print(i[0], i[1])

    print()
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
if __name__ == '__main__':
    main(x=[1,2,3], y=[3,3,0], z=[2,3,0], q=[3,3,0], w=[3,3,0])
    print()
    main(**{'x': [1,2,3], 'y': [3,3,0]})
```
### Результат.
![](Pictures/Lab_4_5.jpg)

## Выводы
1. def main(**kwargs): функция с картежом в качестве аргумента
2. for i in kwargs.items(): проходимся по предметам
3. for key in kwargs: проходимся по ключам

## Лабораторная работа №6
### Напишите две функции. Первая – получает в виде параметра “**kwargs”. Вторая считает среднее арифметическое из значений первой функции. Вызовите первую функцию используя “точку входа” и минимум 4 аргумента.

```python
def main(**kwargs):
    for i, j in kwargs.items():
        print(f"{i}. Mean = {mean(j)}")
def mean(data):
    return sum(data) / float(len(data))
if __name__ == '__main__':
    main(x=[1,2,3], y=(3,3,0))
```
### Результат.
![](Pictures/Lab_4_6.jpg)

## Выводы
Научились использовать функцию с картежом в качестве аргумента

## Лабораторная работа №7
### Создайте дополнительный файл .py. Напишите в нем любую функцию, которая будет что угодно выводить в консоль, но не вызывайте ее в нем. Откройте файл main.py, импортируйте в него функцию из нового файла и при помощи “точки входа” вызовите эту функцию.

```python
from for_import import say_hello
if __name__ == '__main__':
    say_hello()
```
```python
def say_hello():
    print('Hello world!')
```
### Результат.
![](Pictures/Lab_4_7.jpg)

## Выводы
Научились импортировать метод из одного в другой

## Лабораторная работа №8
### Напишите программу, которая будет выводить корень, синус, косинус полученного от пользователя числа.

```python
import math
def main():
    value = int(input('Введите значение: '))
    print(math.sqrt(value))
    print(math.sin(value))
    print(math.cos(value))

if __name__ == '__main__':
     main()
```
### Результат.
![](Pictures/Lab_4_8.jpg)

## Выводы
Импортируем базовую функцию math из python

## Лабораторная работа №9
### Напишите программу, которая будет рассчитывать какой день недели будет через n-нное количество дней, которые укажет пользователь.

```python
from datetime import datetime as dt
from datetime import timedelta as td

def main():
    print(
        f"Сегодня {dt.today().date()}. "
        f"День недели - {dt.today().isoweekday()}"
    )
    n = int(input('Введите количество дней: '))
    today = dt.today()
    result = today + td(days=n)
    print(
        f"Через {n} дней будет {result.date()}. "
        f"День недели - {result.isoweekday()}"
    )

if __name__ == '__main__':
    main()
```
### Результат.
![](Pictures/Lab_4_9.jpg)

## Выводы
Научились импортировать datatime и timedelta, а также давать им псевдонимы

## Лабораторная работа №10
### Напишите программу с использованием глобальных переменных, которая будет считать площадь треугольника или прямоугольника в зависимости от того, что выберет пользователь. Получение всей необходимой информации реализовать через input(), а подсчет площадей выполнить при помощи функций. Результатом программы будет число, равное площади, необходимой фигуры.

```python
global result

def rectangle():
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    global result
    result = a * b

def triangle():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    global result
    result = 0.5 * a * h

figure = input("1-прямоугольник, 2-треугольник: ")

if figure == '1':
    rectangle()
elif figure == '2':
    triangle()

print(f"Площадь: {result}")
```
### Результат.
![](Pictures/Lab_4_10.jpg)

## Выводы
Создаем две функции, после чего вызываем их

## Самостоятельная работа №1
### Дайте подробный комментарий для кода, написанного ниже. Комментарий нужен для каждой строчки кода, нужно описать что она делает. Не забудьте, что функции комментируются по-особенному.

```python
from datetime import datetime # Это импортирует класс datetime из модуля datetime, который позволяет работать с датами и временем.
from math import sqrt # Это импортирует функцию sqrt (квадратный корень) из модуля math, которая будет использоваться для вычисления расстояния между точками.

def main(**kwargs): # Это определение функции main, которая принимает произвольное количество именованных аргументов в виде словаря kwargs.
    for key in kwargs.items(): # Здесь начинается цикл, который перебирает каждую пару ключ-значение в kwargs.
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2) # Здесь вычисляется расстояние между двумя точками, заданными значениями в key[1], которые представляют собой список с двумя элементами
        print(result) # Выводится на экран значение переменной result, т.е. расстояние между точками.

if __name__ == '__main__': # Это проверка, является ли текущий скрипт точкой входа.
    start_time = datetime.now() # Получает текущее время и сохраняет его в переменную
    main( # Вызывается функция main с пятью именованными аргументами, каждый из которых представляет собой список с двумя элементами.
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15]
    )
    time_costs = datetime.now() - start_time # Вычисляется разница между текущим временем и временем, сохраненным в start_time.
    print(f"Время выполнения программы - {time_costs}") # Выводится на экран время выполнения программы, которое было вычислено в предыдущем пункте.
```
### Результат.
![](Pictures/SLab_4_1.jpg)

## Выводы
Расписали каждую строчку кода, согласно тексту задания

## Самостоятельная работа №2
### Напишите программу, которая будет заменять игральную кость с 6 гранями. Если значение равно 5 или 6, то в консоль выводится «Вы победили», если значения 3 или 4, то вы рекурсивно должны вызвать эту же функцию, если значение 1 или 2, то в консоль выводится «Вы проиграли». При этом каждый вызов функции необходимо выводить в консоль значение “кубика”. Для выполнения задания необходимо использовать стандартную библиотеку random. Программу нужно написать, используя одну функцию и “точку входа”

```python
from random import randint

def dice():
    number = randint(1, 6)

    print(f"Значение кубика: {number}")

    if number == 5 or number == 6:
        print("Вы победили")
    elif number == 3 or number == 4:
        dice()
    elif number == 1 or number == 2:
        print("Вы проиграли")

if __name__ == '__main__':
    dice()
```
### Результат.
![](Pictures/SLab_4_2.jpg)

## Выводы
Написали программу, которая имитирует бросание 6 гранного кубика при помощии функции "точка входа"

## Самостоятельная работа №3
### Напишите программу, которая будет выводить текущее время, с точностью до секунд на протяжении 5 секунд. Программу нужно написать с использованием цикла. Подсказка: необходимо использовать модуль datetime и time, а также вам необходимо как-то “усыплять” программу на 1 секунду.

```python
import time
from datetime import datetime

duration = 5

for i in range(duration):
    current_time = datetime.now()
    print("В данным момент:", current_time)

    time.sleep(1)
```
### Результат.
![](Pictures/SLab_4_3.jpg)

## Выводы
Написали программу, которая указывает текущее время с интервалом 1 секунду в течении 5 секунд

## Самостоятельная работа №4
### Напишите программу, которая считает среднее арифметическое от аргументов вызываемое функции, с условием того, что изначальное количество этих аргументов неизвестно. Программу необходимо реализовать используя одну функцию и “точку входа“.

```python
def main(*args):
    return sum(args) / len(args)

if __name__ == '__main__':
    print(main(15, 25, 35))
```
### Результат.
![](Pictures/SLab_4_4.jpg)

## Выводы
Написали программу, которая высчитывает среднее арефметическое и выводит на экран при помощи функции "точка входа"

## Самостоятельная работа №5
### Создайте два Python файла, в одном будет выполняться вычисление
площади треугольника при помощи формулы Герона (необходимо
реализовать через функцию), а во втором будет происходить
взаимодействие с пользователем (получение всей необходимой
информации и вывод результатов). Напишите эту программу и
выведите в консоль полученную площадь.

```python
from for_import import square

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())

    print(square(a, b, c))
```
```python
from math import sqrt

def square(a, b, c):
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))
```
### Результат.
![](Pictures/SLab_4_5.jpg)

## Выводы
Написали программу согласно текстовому заданию, создав 2 Python в один из которых мы импортировали метод