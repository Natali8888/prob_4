#Есть список состоящий из слов и чисел,
# нужно записать в файл построчно сначала
# слова в порядке их длины, а после слов числа в порядке возрастания
import os
with open('example.py', 'w', encoding='utf8') as f:
    pass
a = ('2', '4', '6', 'Питон', 'изучаю', '78', 'я')
b = []  # числа
c = [] # слова
for i in a:
    i = i.strip()
    if i.isdigit(): b.append(int(i))
    else: c.append(i)
b.sort()
c.sort(key=len)
print(c)
print(b)
    #f.write(c)
    #f.write(b)

#2. Добавьте на свой РАБОЧИЙ СТОЛ папку, в ней создайте 3 текстовых файла:
# test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt.
# После этого удалите созданную папку.
# Все операции выполнять с помощью встроенных функций библиотеки os
# Создаем именно на РАБОЧЕМ СТОЛЕ!!!

import os
#os.mkdir('C://users/Andrei/Desktop/HW_file.txt')
#os.chdir('C://users/Andrei/Desktop/HW_file.txt')
#print(os.getcwd())
#f = open('test_1.txt', w)
#f.close()
#f_1 = open('test_2.txt', w)
#f_1.close()
#f_2 = open('test_3.txt', w)
#f_2.close()
#os.rename('test_1.txt', 'rename_1.txt')
#os.rename('test_2.txt', 'rename_2.txt')
#os.rename('test_3.txt', 'rename_3.txt')
#os.remove('rename_1.txt')
#os.remove('rename_2.txt')
#os.remove('rename_3.txt')
#os.chdir('..')
#os.rmdir('HW_file.txt')