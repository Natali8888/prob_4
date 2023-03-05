#В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за
# контрольную. Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать
# средний балл по классу.
with open('ocenka.txt') as file:
    counter = summa = 0
    for line in file:
        counter += 1
        length_line = len(line)
        for i in range(length_line):
            if line[i].isdigit():
                num = int(line[i])
                summa += num
                if num < 3:
                    print("Ученик c оценкой меньше 3-х:", line)
                break
print('Средний балл по классу: %2.f' % (summa/counter))


       # print('Средний балл по классу: %.2f' % (summa / counter))

    #sred = summa / counter
    #print("\nСредний балл по классу:", sred)



#f = open('ocenka.txt', 'r')
#s = f.readlines()
#for i in s:
#    i = i[:-1]
 #   print(i)
#suma = 0
#n = 0
 #   g = int(i[len(i) - 1])
  #  suma += g
   # n += 1
   # if g < 3:
    #print(i[:-1])
#print('Средний балл: %.2f' % (suma / n))
#counter = summa = 0
#for i in s:
#i = int(i[len(i)-1])
 #   counter += 1
  #  summa += 1


#for s in f:
#s = s.split()
#d = int(s[2])
#sum += d
#

#with open ('ocenka.txt', 'r') as file:
 #   counter = summa = 0
  #  for line in file:
   #     counter += 1
    #    length_line = len(line)
     #   for i in range(length_line):
      #      if line[i].isdigit():
       #         num = int(line[i])
        #        summa += num
         #       if num < 3:
          #          print("Ученик(ца) у которого средний бал по классу меньше 3-х:", line)

    #sred = counter // summa
    #print("\nСредний бал по классу:", sred)

#f = open('ocenka.txt')
#sum = 0
#n = 0
#for s in f:
#s = s.split()
#d = int(s[2])
#sum += d
#n += 1
#if d < 4:
#print(s[0], s[1] , s[2])
#f.close()
#print('Средний балл %.2f' %(sum/n))



#d = f.readlines()
#print(d)
#for i in d:
 #   i = i[:-1]
  #  print(i)
#suma = 1
#n = 1
#for i in d:
 #   g = int(i[len(i)-2])
  #  suma += g
   # n += 1
    #if g < 3:
     #   print(i[:-1])
      #  print(sum[:-1])

