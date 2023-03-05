#Создайте функцию, добавьте в неё локальное значение. Сделайте так, чтобы другая
#функция принимала это значение в качестве параметра.
def func():
    global a
    global b
    a = 20
    b = 20
    return a + b
print(func())

def func_1():
    return a + b + 10
print(func_1())

