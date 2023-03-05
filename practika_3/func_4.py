#Напишите рекурсивную функцию, которая осуществляет суммирование чисел в списке.
#Список должен быть сгенерирован из 10 чисел, каждое в диапазоне от 1 до 100
def sum_arr(arr, size):
    if (size == 0):
        return 0
    else:
        return arr[size - 1] + sum_arr(arr, size - 1)
n = int(input("Введите длину списка: "))
a = []
for i in range(0, n):
    element = int(input("Введите элемент списка: "))
    a.append(element)
print("Весь список: ")
print(a)
print("Сумма элементов списка равна: ")
b = sum_arr(a, n)
print(b)



