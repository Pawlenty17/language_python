# Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

print("Введите размер n: ")
n = int(input())
print("Введите размер m: ")
m = int(input())
print("Введите кол-во долек: ")
k = int(input())

if (k == n or k == m or (k < n and k < m)):
    print("No!")
else:
    print("Yes!")