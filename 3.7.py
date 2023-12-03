#3
n = int(input("Введите количество чисел в последовательности: "))

sum = 0

for i in range(n):
    num = int(input("Введите число: "))
    if num % 5 == 0:
        sum += num

print("Сумма чисел, кратных 5:", sum)