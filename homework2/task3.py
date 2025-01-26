# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

print("Введите целое число: ")
num = int(input())
degree = 0


for i in range(num):
    x = 2 ** degree
    if x <= num:
        degree += 1
        print(x)
        