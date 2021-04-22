# Задача - найти палиндром x

# Должны выполнятся следующие условия:
# x = str(x)[::-1]
# x = a * b
# a in range(100, 1000) and b in range(100, 1000)

x = 0
for a in range(100, 1000):
    for b in range(100, 1000):
        if a * b > x and str(a * b) == str(a * b)[::-1]:
            x = a * b

print(x)


def compute():
    ans = max(i * j
              for i in range(100, 1000)
              for j in range(100, 1000)
              if str(i * j) == str(i * j)[:: -1])
    return str(ans)


print(compute())
