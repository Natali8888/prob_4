#1. Написать рекурсивную функцию, которая определяет, является ли строка
# палиндромом (одинаково читается в обе стороны: герег, лол, мам, level и тд.)

#def is_palindrome(stroka):
#    if len(stroka) < 1:
#        return True
#    else:
#        if stroka[0] == stroka[-1]:
#            return is_palindrome(stroka[1:-1])
#        else:
#            return False
#a = str(input("Введите строку: "))
#if (is_palindrome(a) == True):
#    print("палиндром")
#else:
#    print("не палиндром")

#2. Написать рекурсивную функцию для подсчета количества элементов в списке

#def func(lst):
#    if not lst:
#        return 0
#    return 1 + func(lst[1:])
#a = [34,56,7]
#print("Длина списка: ", func(a))


#3. Этот код отсортирует список строк по последнему символу в каждой строке.
# Здесь использована лямбда-функция в качестве ключа в сортировке.
# Измените код так, чтобы сортировка была по второму символу каждой строки

#strings = ['apple', 'banana', 'cherry', 'date']
#sorted_strings = sorted(strings, key=lambda s: s[-5:], reverse=True)
#print(sorted_strings) # Output: ['cherry', 'date', 'apple', 'banana']

#4. Напишите функцию make_adder(n),
# которая принимает целое число n и возвращает внутреннюю функцию,
# которая может прибавлять этот n к любому другому целому числу.

#def make_adder(n):
#    def helper(b):
#        return n+b
#    return helper
#print(make_adder(40)(60))

#5. Напишите функцию counter(), которая возвращает внутреннюю функцию increment(),
# которая увеличивает счетчик на 1 каждый раз, когда она вызывается.
#count = 0
#def counter():
#    global count
#    count += 1
#def increment():
#    counter()
#increment()
#print(count)
