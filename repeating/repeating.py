print("Введите числа a и b (a < b)")
a = int(input('Введите число а'))
b = int(input('Введите число b'))
if a % 2 != 0:
    for i in range(a + 1, b + 1, 2):
        print(i)
else:
    for i in range(a, b + 1, 2):
        print(i)
x = int(input('Введите любое число в диапазоне от 1 до 9999'))
if x < 10 and x > 0:
    if x % 2 == 0:
        print(x, "четное однозначное")
    else:
        print(x, "нечетное однозначное")
elif x >= 10 and x < 100:
    if x % 2 == 0:
        print(x, "четное двухзначное")
    else:
        print(x, "нечетное двухзначное")
elif x >= 100 and x < 1000:
    if x % 2 == 0:
        print(x, "четное трехзначное")
    else:
        print(x, "нечетное трехзначное")
elif x >= 1000 and x < 10000:
    if x % 2 == 0:
        print(x, "четное четырехзначное")
    else:
        print(x, "нечетное четырехзначное")
else:
    print('Число меньше 1 или больше 9999')
