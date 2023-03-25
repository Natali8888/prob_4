#ДЗ на пятницу:
# №1. Если в функцию передаётся кортеж, то посчитать длину всех его строк.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Сделать проверку со всеми этими случаями.
# Использовать готовые типы данных, с клавиатуры ничего не вводится
# Например function([1,2,3,'a','bc8?']) -> 4 числа, 3 буквы
# function((1,2,3,'a','bc8?',7,8,9)) -> 5 символов
# function(788) -> 1
# function('788') -> 0 букв

# №2. Привяжите к предыдущей функции декоратор, который будет выводить информацию о том,
# какой тип данных вы отправили: кортеж, список, число, строку или какой-то другой тип данных

#def function(fn):
#    def wrapper(W):
#        print(f'Тип данных, который вы отправили: {type(W)}')
#            return fn(W)

#    return wrapper #возвращаем САМУ ФУНКЦИЮ, а не ее значение


#@function
#def sort_all(n):
#    if type(n) == list:
#        letters = 0
#        numbers = 0
#        for i in str(n):
#            if i.isalpha():
#                letters += 1
#            if i.isdigit():
#                numbers += 1
#        return f'Количество букв: {letters}, количество цифр: {numbers}'

#    elif type(n) == tuple:
#        len_count_string = 0 #счетчик длины всех строк
#        for i in n:
#            if type(i) is str: len_count_string += len(i)
#        return len_count_string

#    elif type(n) == int:
#        count = 0 #счетчик нечётных цифр
#        for i in str(n):
#            if i in '13579': count += 1

#        return f'Количество нечётных цифр: {count}'

#    elif type(n) == str:
#        count = 0 #счетчик букв
#        for i in n:
#            if i.isalpha(): count += 1
#        return f'Количество букв в строке: {count}'
#    else:
#        return 'Другой тип данных'


#print(sort_all([6, 7, 9, 'm', 'gok']))
#print(sort_all((98, 100, 'a', 'b?')))
#print(sort_all(669))
#print(sort_all('55yh77'))
#print(sort_all({5,7,8,9, 'a','b'}))
#print(sort_all({'a': 90,'b': 100}))
