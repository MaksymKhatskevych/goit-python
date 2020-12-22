print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                 Calkulator                ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

x = None
res = 0
while x != "=":
    try:
        number = float(input("Введите число: "))
    except ValueError:
        print("Введите число дробное либо целое")
        continue
    if x == None:
        res = number
    elif x == "+":
        res += number
    elif x == "-":
        res -= number
    elif x == "*":
        res *= number
    elif x == "/":
        try:
            res /= number
        except ZeroDivisionError:
            print("Нельзя делить на ноль")
            continue
    x = input("Введите операнд: ")
    while x not in ('+', "-", '*', '/', '='):
        print("Неправельный операнд, попробуйте снова +,-,*,/ or =...")
        x = input("Введите операнд: ")
    if x == "=":
        continue
print(f"Результат = {res} ")
