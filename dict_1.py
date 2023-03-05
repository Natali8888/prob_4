# Есть словарь песен группы Depeche Mode. Выведите общее время звучания всех песен.
# Создайте список песен, время звучаниях которых больше 5 минут
# Создайте новый словарь тех песен, в название которых состоит из одного слова
violator_songsdict = {'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56,
'Halo': 4.30, 'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6,'Policy of Truth': 4.88,
'Blue Dress': 4.18,'Clean': 5.68}
print(violator_songsdict.values())
print('общее звучание всех песен: ', sum(violator_songsdict.values()))
res = []
for x, y in violator_songsdict.items():
    if y > 5:
        res.append(x)
print('список песен со звучанием более 5 минут: ', res)
a = {k: violator_songsdict[k] for k in violator_songsdict.keys() if not ' ' in k}
print('новый словарь песен сост. из одного слова: ', a)

