
#1.	Создайте класс "Студент", который имеет атрибуты имя и возраст, а также методы "изменить_имя"
# и "изменить_возраст". Напишите функцию, которая создает объект класса "Студент",
# запрашивая у пользователя его имя и возраст, а затем предлагает пользователю изменить
# имя и возраст.
#class Student:
   #name = 'Olga'
   #age = 19
   #def opis_(self):

    #   print(f'Студент по имени {self.name}, возраст {self.age}')
#girl = Student()
#girl.opis_()
#    def __init__(self, imya, vozrast):
#        self.imya = imya
#        self.vozrast = vozrast
#boy = Student('Alex', 20)
#print(f'Введите Ваше имя и возраст: {boy.imya}, {boy.vozrast}. Можете изменить имя и возраст на другое')
#    def chang_name():
    #pass
#        print(f'Можете изменить имя {self.imya} на другое')
#    def chang_age():
    # pass
#    print(f'Можете изменить имя {self.vozrast} на другое')

#2.	Напишите функцию, которая принимает на вход список чисел и возвращает
#сумму квадратов всех четных чисел в списке.
#def all_even(lst):
#    suma = 0
#    for i in lst:
#        if i % 2 == 0:
#            suma += i * i
#    return(suma)
#mylist = [1, 2, 4, 8, 10]
#s = all_even(mylist)
#print(f'Сумма квадратов четных чисел списка {mylist} равна {s}')


#3.	Создайте класс "Калькулятор", который имеет атрибуты "значение" и методы "сложить", "вычесть",
# "умножить" и "разделить". Напишите функцию, которая создает объект класса "Калькулятор"
# и позволяет пользователю выполнить несколько арифметических операций с его помощью.
#class Calc:
#    def __init__(self):
#        self.vvod()
#    def plus(self, a): return self.a + self.b
#    def minus(self): return self.a - self.b
#    def dele(self):
#        if self.b == 0:
#            return "error"
#        else:
#            return self.a / self.b
#    def umn(self): return self.a * self.b
#    def vvod(self):
#        self.a = int(input("Введите первое число: "))
#        self.b = int(input("Введите второе число: "))
#while True:
#    ex = Calc()
#    c = input("Введите операцию(+,*,/,-): ")
#    if c == '+':
#        print(ex.plus())
#    elif c == "-":
#        print(ex.minus())
#    elif c == '*':
#        print(ex.umn())
#    elif c == '0':
#        break
#    else:
#        print(ex.dele())

#4.	Создайте класс "Автомобиль", который имеет атрибуты "марка", "модель", "год_выпуска",
# "цвет" и метод "описание", который выводит описание автомобиля в виде строки.
# Напишите функцию, которая создает объект класса "Автомобиль", запрашивая у пользователя
# информацию о марке, модели, годе выпуска и цвете, а затем выводит описание автомобиля.
#class Auto():
#    marka = 'BMW'
#    model = "X5"
#    year = 2022
#    color = "red"
#    def opis_(self):
#        print(f'Марка {self.marka}, модель {self.model}, {self.year} года выпуска, {self.color} цвета')
#avto = Auto()
#avto.opis_()
#    def __init__(self, make, seriya, god, cvet):
#        self.make = make
#        self.seriya = seriya
#        self.god = god
#        self.cvet = cvet

#car = Auto("Volga", 2110, 2000, 'blue')
#print(f'Какая информация об автомобиле Вас интересует?: '
#      f' Марка {car.make}, Модель {car.seriya}, {car.god} г.в., цвет {car.cvet}')

#5.	Создайте класс "Сотрудник", который имеет атрибуты "имя", "фамилия", "должность"
# и метод "описание", который выводит описание сотрудника в виде строки.
#class Sotrudnik():
#    name = 'Sofia'
#    last_name = 'Petrova'
#    dolgnost = 'direktor'
#    def opis_(self):
#        print(f'Имя: {self.name}, Фамилия: {self.last_name}, должность: {self.dolgnost}')
#women = Sotrudnik()
#women.opis_()
# Создайте класс "Отдел", который имеет атрибуты "название" и "список_сотрудников",
# а также методы "добавить_сотрудника" и "удалить_сотрудника". Напишите функцию, которая создает объект класса "Отдел",
# запрашивая у пользователя его название,
#class Otdel:
    #nazvanie = 'marketing'
    #spis_sotr = ['Ivanova', 'Petrova']
    #def dobav_sotr(self):
    #    pass
    #def del_sotr(self):
    #    pass
    #def opis_(self):
     #   print(f'Введите название отдела: {self.nazvanie}')
#rabotnik = Otdel()
#rabotnik.opis_()

# а затем предлагает пользователю добавить
# несколько сотрудников в отдел, после чего выводит список всех сотрудников в отделе
# и их описания.
#    emp_count = 0
#    def __init__(self, last_name):
#        self.last_name = last_name
#        Otdel.emp_count += 1
#    def display_count(self):
#        print('Всего сотрудников: %d' % Otdel.emp_count)
#    def display_otdel(self):
#        print(f'Фамилия: {self.last_name})
# emp1 = Otdel('Ivanova')
#emp2 = Otdel('Petrova')
#emp1.display_otdel()
#emp2.display_otdel()
#print("Всего сотрудников: %d" % Otdel.emp_count)

# Затем функция предлагает пользователю удалить одного из сотрудников
# и выводит обновленный список сотрудников и их описания.



