# Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.
# # Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Enter the number '))
for i in range(1, n + 1):
    p = 1
    for j in range(1, i + 1):
        p *= j
        if (j == 1):
            print(j, end=' ')
        else:
            print('*', j, end=' ')
    print('=', p)