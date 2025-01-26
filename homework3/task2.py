# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import random

size = int(input("Введите размер массива: "))
arr = [random.randint(0, 100) for i in range(size)]
print("Случайный массив: ", arr)



num = int(input("Введите число: "))
closed_i = arr[0]
min_difference = abs(arr[0] - num)
for i in arr:
    difference = abs(i - num)
    if (difference < min_difference):
        min_difference = difference
        closed_i = i
print(closed_i)