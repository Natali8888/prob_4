#Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
#и возвращающую True, если оно простое, и False - иначе.

def is_prime(n):
    k = 2
    while k * k <= n:
        if n % k == 0:
            return False
        k += 1
    return True
print(is_prime(120))

