print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                 Calсulator                ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

while True:
    try:
        number1 = float(input("Введите первое число:"))
        number2 = float(input("Введите второе число:"))
    except ValueError:
        print("Некоректно введено значение, повторите попытку")
        number1 = float(input("Введите первое число:"))
        number2 = float(input("Введите второе число:"))
    
    x = input("Выберите действие: + - / * ")

    if x == "++":
        print("Error - Что то пошло не так повторите!!!")
        continue

    elif x == "+":
        res = number1 + number2
        break

    elif x == "--":
        print("Error - Что то пошло не так повторите ввод оператора!!!")
        continue

    elif x == "-":
        res = number1 - number2
        break

    elif x == "**":
        print("Error - Что то пошло не так повторите ввод оператора!!!")
        continue

    elif x == "*":
        res = number1 * number2
        break

    elif x == "//":
        print("Error - Что то пошло не так повторите ввод оператора!!!")
        continue

    elif x == "/":
        try:
            res = number1 / number2
        except ZeroDivisionError:
            print("Деление на ноль запрещено!")
        break
r = input("Введите знак равенства: ")    
if r == "=":
    print(f"Результат будет {res}")
