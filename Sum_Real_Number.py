# Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.
# Пример:
# 0,56 -> 11

s = 0
n = input('Enter the number: ')
n = n.split(",")
a = int(n[0])
b = int(n[1])
while (a > 0):
    s += a % 10
    a = a // 10
while (b > 0):
    s += b % 10
    b = b // 10
print(f'{s}')