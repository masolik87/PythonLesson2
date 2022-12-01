# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся
# одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0
# Реализуйте алгоритм перемешивания списка.

import random
n = int(input('Enter the number: '))
while(n!= 0):
    a = [0] * n
    for i in range(n):
        a[i] = random.randint(-n, n)
        print(a[i], end= ' ')
    ind = input()
    print(ind)
    s = 1
    for i in range(len(ind)):
       s *=a[int(ind[i])]
    print(s)
    print('type n')
    n = int(input())