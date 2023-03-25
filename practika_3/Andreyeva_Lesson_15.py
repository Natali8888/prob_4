
class Animals:
#    lapki = 4     # статические поля (свойства)
#    nosik = 1
#    ushki = 2
#    hvost = 1
#    def jump(self):
        #pass
#        print(f'У животных {Animals.lapki} лапки и {Animals.nosik} нос')
#    def drink(self):
#        pass
#    def eat(self):
#        pass

    def __init__(self, lapki, nosik):  #динанимические поля (свойства)
       self.kolvo_lapki = lapki
       self.kolvo_nosik = nosik
givotnoe = Animals(4, 1)

print(givotnoe.kolvo_lapki, givotnoe.kolvo_nosik)







#1. Создайте класс Person, который имеет атрибуты name и age, а также метод greet()(выводит
    #приветствие на экран с именем персоны).
#class Person:
#    name = 'Natali'
#    age = 30
#    def greet(self):
#        print(f'Привет, {Person.name}')
#people = Person()
#print(people.name)
#print(people.age)
#people.greet()


#2. Создайте класс Car, который имеет атрибуты make, model и year, а также метод get_info()
# (возвращает строку, содержащую информацию о машине).
#class Car:
#    make = 'Tesla'
#    model = 'Model Y'
#    year = 2020
#    def get_info(self):
#        print(f'make - {self.make}, model - {self.model}, year - {self.year}')
#avto = Car()
#avto.get_info()
