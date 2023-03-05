# Задача 3. Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра ...
str_ = input('Введите текст: ')
a = 'АЕЁИОУЫЭЮЯаеёиоуыэюя'
b = 0
c = 0
e = 0
k = 0
for i in str_:
    if i in a:
        b += 1
    else:
        c += 1
print('кол. гласных: ', b)
print('кол. согласных: ', c)
d = len(str_)
print('кол. симв. в строке:  ', d)
for i in range(len(str_)-1):
    if str_[i].isupper() and str_[i+1].isupper():
        e += 1
    if str_[i].islower() and str_[i+1].islower():
        k += 1
print('кол. пар с верхн. рег.:  ', e)
print('кол. пар с нижн. рег.: ', k)
