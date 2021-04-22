first = 1
second = 2
even_sum = 0

while second < 4000000:
    if second % 2 == 0:
        even_sum += second

    first, second = second, first + second

print(even_sum)
