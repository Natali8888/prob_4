# Калькулятор. Создать класс, где реализованы методы математических операция (+-/*)
# и функция (вне класса) для ввода данных.

class Calc:
    def __init__(self):
        self.vvod()

    def plus(self, a): return self.a + self.b
    def minus(self): return self.a - self.b
    def dele(self):
        if self.b == 0:
            return "error"
        else:
            return self.a / self.b
    def umn(self): return self.a * self.b

    def vvod(self):
        self.a = int(input("Введите первое число: "))
        self.b = int(input("Введите второе число: "))


while True:
    ex = Calc()
    c = input("Введите операцию(+,*,/,-): ")
    if c == '+':
        print(ex.plus())
    elif c == "-":
        print(ex.minus())
    elif c == '*':
        print(ex.umn())
    elif c == '0':
        break
    else:
        print(ex.dele())


#Создайте класс Example. В нём пропишите 3 (метода) функции. Две переменные
#задайте статически, две динамически.
#❖ Первая функция: создайте переменную и выведите её
#❖ Вторая функция: верните сумму 2-ух глобальных переменных
#❖ Третья функция: верните результат возведения первой динамической
#переменной во вторую динамическую переменную
#❖ Создайте объект класса.
#❖ Напечатайте обе функции
#❖ Напечатайте переменную a

class TheExample:
    a = 2
    b = 3

    def __init__(self, t, r):
        self.t = t
        self.r = r

    def func(self):
        self.c = 5
        print(self.c)

    def func1(self):
        return self.a + self.b

    def func2(self):
        return self.t**self.r


example = TheExample(4,2)

print(example.a)
print(example.func1())
print(example.func2())
example.func()

