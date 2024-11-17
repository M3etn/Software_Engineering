class RepeatDecorator:
    def __init__(self, times):
        self.times = times

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for i in range(self.times):
                print(f"Выполнение {i + 1} из {self.times}")
                func(*args, **kwargs)
        return wrapper

@RepeatDecorator(times=3)
def print_hello():
    print("Привет!")

counter = 0

@RepeatDecorator(times=5)
def increment_counter():
    global counter
    counter += 1
    print(f"Текущее значение счетчика: {counter}")

print("Запуск функции print_hello:")
print_hello()

print("\nЗапуск функции increment_counter:")
increment_counter()