# 1. Допишите скрипт для расчета средней температуры
#week_temp = (26, 29, 34, 32, 28, 26, 23)
#sum_temp = sum(week_temp)
#days = len(week_temp)
#mean_temp = sum_temp / days
#print(int(mean_temp))

#2. Найти самое длинное слово в кортеже ('a', 'z', 'hello_world!')
#korteg = ('a', 'z', 'hello_world!')
#korteg = list(korteg)
#long_word = ''
#for i in korteg:
    #if len(i) > len(long_word):
        #long_word = i
#print(long_word)

#3. Преобразовать текст в кортеж слов с удалением знаков препинания

first_str = '''Я изучаю:;[]{}=+-_Пайтон'''
new_str = first_str.replace(':;[]{}=+-_', '')
print(tuple(new_str))
#t = tuple(map(int, s.split(',')))

                             #ДОЛГ ПО Д.З. (СПИСКИ)

#1. В списке, содержащем положительные и отрицательные целые числа, вычислите сумму
# чётных положительных элементов.

#a = (2, -4, -1, 1, 5, 4, 5, 6, 10, -10, 1)
#sum = 0
#for i in a:
    #if i > 0 anl i % 2:
        #sum += i
#print(f'Сумма положительных четных чисел: {sum}')

#2. Найти в списке те элементы, значение которых меньше среднего арифметического,
# взятого от всех элементов списка.
#arr = [10,12,14]
#summa = 0 #счетчик суммы
#sred = 1 #счетчик произведения
#ints = [1, 2, 3, 4, 5]
#avg = sum(ints) / len(ints)
#print(avg)
#elem = 0
#for i in ints:
#    elem += i
#    if i < avg:
#        print(elem)
 #   summa += i if i < avg and i != avg:
  #  sred *= summa/len(arr)
#
#print(f'Сумма: {summa}'f' Сред.арифм.: {sred}')


