# Задайте список из n чисел последовательности (1 + 1/n)^n и 
# выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

def f(x):
    return pow (1 + 1/x, x)
n = int(input('Enter the number: '))
s = 0
for i in range(1, n + 1):
    s += f(i)
    print(round(f(i), 2), end= ' : ')
print(round(s, 2))