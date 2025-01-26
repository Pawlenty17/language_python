# Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print("Введите трёхзначное число: ")
num = int(input())
sum = 0

if (num > 99 and num < 1000):
    firstNum = num / 100
    secondNum = (num / 10) % 10
    thirdNum = num % 10
    sum = firstNum + secondNum + thirdNum
    print(int (sum))
else:
    print("Ошибка! Вы ввели не трёхзначное число.")