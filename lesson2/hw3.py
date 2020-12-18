print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                 Calkulator                ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

while True:
    try:
        number1 = float(input("Enter the first number:"))
        number2 = float(input("Enter the second number:"))
    except ValueError:
        print("Некоректно введено значение, повторите попытку")
        
        print("Введеный символ может быть только числом")
        number1 = float(input("Enter the first number:"))
        number2 = float(input("Enter the second number:"))
    x = input("Choose an action: + - / * ")

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
            print("Нельзя делить на ноль!")
        break
r = input("Введите знак равенства: ")    
if r == "=":
    print(f"Результат будет {res}")