print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                 Calkulator                ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

res = 0
while True:
    try:
        number1 = float(input("Введите первое число:"))
        number2 = float(input("Введите второе число:"))
    except ValueError:
        print("Некоректно введено значение, повторите попытку")
        
        print("Введеный символ может быть только числом")
    else:
        break

x = input("Введите оператор: ")
while x not in ('+', "-", '*', '/', '='):
    print("Оператор может быть только +,-,*,/ or =...")
    x = input("Введите оператор: ")


if x == "+":
    res = number1 + number2


elif x == "-":
    res = number1 - number2


elif x == "*":
    res = number1 * number2


elif x == "/":
    try:
        res = number1 / number2
    except ZeroDivisionError:
        print("Нельзя делить на ноль!")
       
r = input("Введите знак равенства: ")    
if r == "=":
    print(f"Результат: {res}")
