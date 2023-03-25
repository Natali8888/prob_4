#Простейший калькулятор c введёнными двумя числами вещественного типа.
#Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
#Обработать ошибку: “Деление на ноль”
#Ноль использовать в качестве завершения программы (сделать как отдельную операцию).
def calc_op(op, a, b):
    if op == '+':   return a + b
    elif op == '-':   return a - b
    elif op == '*':   return a * b
    elif op == '/':
        try:
            return a / b
        except:
            return 'Нельзя разделить на ноль'
while True:
    print()
    op = input('Введите операцию (+, -, *, /, 0-завершение работы): ')
    if op == '0':
        break
    if op in '+-*/':
        while True:
            try:
                a, b = map(float, input('a, b = ').split())
                print(calc_op(op, a, b))
                break
            except:
                pass



#Если в функцию передаётся кортеж, то посчитать длину всех его слов.
#Если список, то посчитать кол-во букв и чисел в нём. Число – кол-во нечётных цифр.
#Строка – количество букв. Сделать проверку со всеми этими случаями.
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
#print(sort_all([6, 7, 9, 'm', 'gok']))
#print(sort_all((98, 100, 'a', 'b?')))
#print(sort_all(669))
#print(sort_all('55yh77'))


