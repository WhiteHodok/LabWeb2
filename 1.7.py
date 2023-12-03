#1
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print("Сумма двух наибольших чисел:", num1 + num2)
    else:
        print("Сумма двух наибольших чисел:", num1 + num3)
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print("Сумма двух наибольших чисел:", num2 + num1)
    else:
        print("Сумма двух наибольших чисел:", num2 + num3)
else:
    if num1 >= num2:
        print("Сумма двух наибольших чисел:", num3 + num1)
    else:
        print("Сумма двух наибольших чисел:", num3 + num2)