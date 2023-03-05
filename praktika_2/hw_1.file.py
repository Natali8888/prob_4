#В текстовом файле посчитать количество строк, а также для каждой отдельной
#строки определить количество в ней символов.
f = open('2.txt', 'r')
s = f.readlines()
print(s)
for i in s:
    i = i[:-1]
    print(i)
line = 0
for i in s:
    line += 1
    flag = 0
    for j in i:
        if j != ' ' and flag == 0:
            flag = 1
        elif j == ' ':
            flag = 0
    print(i, len(i[:-1]), 'симв.')
    print(line, 'стр.')
    #f.close()
