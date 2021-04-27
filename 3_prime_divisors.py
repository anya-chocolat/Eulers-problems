# находим наибольший простой делитель числа

digit = 600851475143  # число, к которому подбираем делители



# Улучшенное решение
def max_prime_factor(num, i=2):
    while i != num:
        if num % i == 0:
            num = num // i
        else:
            i += 1
    return num

print(f"Самый большой делитель числа {digit}, являющийся простым числом: {max_prime_factor(digit))}."


      
# Решение "в лоб"
prime_factors = []  # переменная для хранения простых делителей
# начинаем с 2, так как это самое маленькое простое число
for n in range(2, int(digit**0.5)):
    # проверяем, является ли число делитетем
    if digit % n == 0:
        # проверяем, является ли делитель простым числом или нет
        for i in range(2, int(n**0.5)):
            if n % i == 0:
                break
        # если число простое, то оно становится максимальным простым делителем на этот момент
        else:
            prime_factors.append(n)
    if digit//n != 2:
        for i in range(2, int((digit//n)**0.5)):
            if digit//n % i == 0:
                break
        # если число простое, то оно становится максимальным простым делителем на этот момент
        else:
            prime_factors.append(digit//n)

# проверяем, есть ли вообще делители, удовлетворяющие условиям
if prime_factors:
    print(f"Самый большой делитель числа {digit}, являющийся простым числом: {max(prime_factors)}.")
else:
    print("Число не имеет делителей, которые являлись бы простым числом.")
