#2
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

sum = 0
count = 0

for num in range(a, b+1):
    sum += num * 2
    count += 1

average = sum / count
print("Среднее арифметическое удвоенных натуральных чисел на отрезке [a, b]:", average)