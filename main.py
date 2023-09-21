import math

def sum_digit(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_digit(n // 10)

n = int(input("Введите число: "))
sum = sum_digit(n)
print(sum)
def is_even (number):
    if (number // 2 ):
        return True
    else:
        return False
number = int(input("Введите число, которое хотите проверить на четность: "))
chetnost = is_even(number)
print(chetnost)
def rectangle_area(width, height):
    return width * height
width = int(input("Введите ширину: "))
height = int(input("Введите длину: "))
area = rectangle_area(width, height)
print(area)
def actions():
    if (sign == 1):
        return num + num1
    elif (sign == 2):
        return num - num1
    elif (sign == 3):
        return num * num1
    elif (sign == 4):
        if (num1 != 0):
            return num / num1
        elif (num1 == 0):
            print("На ноль делить нельзя")
    elif (sign == 5):
        return num ** num1
    elif (sign == 6):
        return math.sqrt(num), math.sqrt(num1)

    elif (sign == 7):
        return math.factorial(int(num)), math.factorial(int(num1))

    elif (sign == 8):
        return math.sin(num), math.sin(num1)

    elif (sign == 9):
        return math.cos(num), math.cos(num1)

    elif (sign == 10):
        return math.tan(num), math.tan(num1)
    else:
        print("ошибка")

print("Возможные действия: ")
print("1) Сложение ")
print("2) Вычитание ")
print("3) Умножение ")
print("4) Деление ")
print("5) Возведение в степень ")
print("6) Квадратный корень ")
print("7) Факториал ")
print("8) Синус ")
print("9) Косинус ")
print("10) Тангенс ")

while (True):
    sign = int(input("Введите действие: "))
    num = float(input("Введите первое число: "))
    num1 = float(input("Введите второе число: "))
    result = actions()
    print(result)
    break
