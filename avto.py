# Значениями словаря могут быть и списки. Создайте словарь с ключами BMW, Tesla
# и списками из 3х моделей в качестве значений. Выведите первое и последнее значения
# каждого из ключей.

dict_1 = {'BMW': ['X5', 'X6', 'X7']}
dict_2 = {'TESLA': ['Model X', 'Model 3', 'Model Y']}
for key, value in dict_1.items():
    print(key, value[0], value[-1])
for key, value in dict_2.items():
    print(key, value[0], value[-1])


