# Создайте класс Human.
# class Human:
# # Определите для него два статических поля: default_name и default_age.
#     default_name = 'USER'
#     default_age = None
# # Создайте метод __init__(), который помимо self принимает еще два параметра: name и age. Для этих параметров задайте значения по умолчанию, используя свойства default_name и default_age. В методе __init__() определите четыре свойства: Публичные - name и age. Приватные - money и house.
#     def __init__(self, name = default_name, age = default_age):
#         #Динамические поля
#         #Публичные
#         self.name = name
#         self.age = age
#         #Приватные
#         self.__house = False
#         self.__money = 0
# # Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.
#     def info(self):
#         print(f'Имя: {self.name}, возраст: {self.age}, наличие дома: {self.__house}, денег: {self.__money}')
# # Реализуйте справочный статический метод default_info(), который будет выводить статические поля default_name и default_age.
#     @staticmethod
#     def default_info():
#         print(f'Имя по умолчанию: {Human.default_name}, возраст по умолчанию: {Human.default_age}')
#
# # Реализуйте метод earn_money(), увеличивающий значение свойства money.
#     def earn_money(self, amount):
#         self.__money += amount
#         print(f'Получили {amount} рублей. Текущий счет: {self.__money} рублей')
# # Тесты
# # Вызовите справочный метод default_info() для класса Human()
# Human.default_info()
# # Создайте объект класса Human
# Evgeniy = Human('Евгений',29)
# # Выведите справочную информацию о созданном объекте (вызовите метод info()).
# Evgeniy.info()
# # Поправьте финансовое положение объекта - вызовите метод earn_money()
# Evgeniy.earn_money(100)
# # Посмотрите, как изменилось состояние объекта класса Human
# Evgeniy.info()
# # print(Evgeniy._Human__money) #обращение к защищенному свойству вне класса (Object._Class__private_method)


# В задаче про класс Human дописать 2 класса: класс House для создания дома, класс Buy_House
# для его покупки. Для того, чтобы в классе Human свойство __house сделать True,
# нужно использовать наследование классов. Но каких? :)

# class Human:
#     default_name = 'USER'
#     default_age = None
#     def __init__(self, name = default_name, age = default_age):
#         self.name = name
#         self.age = age
#         self.__house = False
#         self.__money = 0
#     def __str__(self):
#         return f'Имя: {self.name}, возраст: {self.age}, наличие дома: {self.__house}, денег: {self.__money}'
#
#     def earn_money(self, amount):
#         self.__money += amount
#         print(f'Получили {amount} рублей. Текущий счет: {self.__money} рублей')
#
#     def check_money(self, house):
#         price = house.final_price()
#         if price <= self.__money:
#             self.__buy_house(house, price)
#             print('Дом куплен!')
#         else:
#             print('Нет денег!')
#     def __buy_house(self, house, price):
#         self.__money -= price
#         self.__house = house
#
# class House: #создали класс для создания дома
#     def __init__(self, area, price):
#         self._area = area
#         self._price = price
#     def final_price(self):
#         return self._price
#
# class Buy_House(House):
#     def __init__(self, area, price):
#         super().__init__(area, price)
#     def __str__(self):
#         return f'Информация о доме: Площадь - {self._area}'
# Evgeniy = Human('Евгений',29)
# print(Evgeniy)
# small_house = Buy_House(200, 5000)
# Evgeniy.check_money(small_house)
# Evgeniy.earn_money(5000)
# Evgeniy.check_money(small_house)
# print(Evgeniy)


# Два метода в классе, один принимает в себя либо строку, либо число.
# Если передают строку, то смотрим: если произведение гласных и согласных букв меньше
# или равно длине слова, выводить все гласные, иначе согласные; если число то,
# произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе
vowel = 'euioa'
class Test:
    def __init__(self):
        pass
    def first(self, item):
        if isinstance(item, str):
            vowelQuan = 0
            vowels = ''
            consonants = ''
            for i in item:
                if i in vowel:
                    vowelQuan += 1
                    vowels += i
                else:
                    consonants += i
            if vowelQuan * (self.second(item) - vowelQuan) <= self.second(item):
                print(vowels)
            else:
                print(consonants)
        elif isinstance(item, int):
            sum = 0
            for i in str(item):
                if int(i) % 2 == 0:
                    sum += int(i)
            print(sum * self.second(str(item)))
    def second(self, item):
        return len(item)
if __name__ == '__main__':
    obj1 = Test()
    obj1.first(23457)
    obj2 = Test()
    obj2.first('python')


    # Пример обычного и статического метода:
    # class MyClass:
        #     def __init__(self, x):
    #         self.x = x
    #     def instance_method(self, y):
    #         return self.x + y
        #     @staticmethod
    #     def static_method(z):
    #         return z * 2
    # obj = MyClass(10)
    # print(obj.instance_method(20))
    # print(MyClass.static_method(40))
    # class MyClass1:
    #     class_attr = 0
     #     def __init__(self, x):
    #         self.x = x
    #     def instance_method(self, y):
    #         return self.x + y
    #     @classmethod            #декоратор для создания класс-метода
    #     def class_method(cls,z):
    #         cls.class_attr = z
    #         return cls.class_attr
        # obj = MyClass1(5)
    # print(obj.instance_method(10))
    # print(MyClass1.class_method(400))
    # print(MyClass1.class_attr)


#class Example:
#     def __init__(self, a,b,c):
#         self.a = a            #публичное свойство
#         self.__b = b          #приватное свойство
#         self._c = c           #protected свойство
#     def change(self):
#         self.__b += 100 #могу обратиться к этому приватному свойству, так как нахожусь внутри класса
#         self._c += 1000
#         print(self.__b, self._c)
#         return self.__hyper()
#     def __hyper(self):
#         print('Это приватный метод')
# ex = Example(10,20,30)
# print(ex.a) #обращение к public свойству
# ex.change()








