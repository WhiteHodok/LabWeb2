#4
sum = 0
num = int(input("Введите число: "))

while num != 0:
    if num % 4 == 0 and num % 10 == 6:
        sum += num
        num = int(input("Введите число: "))

print("Сумма чисел, кратных 4 и оканчивающихся на 6:", sum)