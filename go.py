def calculator():
    print("Выберите операцию:")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. %")
    print("5. sqrt")
    print("6. /")
    print("7. pow")
    print("8. cube")
    
    choice = input("Введите номер операции (1/2/3/4/5/6/7/8): ")
    
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    
    if choice == '1':
        print(f"{x} + {y} = {x + y}")
    elif choice == '2':
        print(f"{x} - {y} = {x - y}")
    elif choice == '3':
        print(f"{x} * {y} = {x * y}")
    elif choice == '4':
        print(f"{x} % {y} = {x % y}")
    elif choice == '5':
        sqrt = x ** (0.5) 
        print(f"{x} = {sqrt}")
    elif choice == '6':
        if y != 0:
            print(f"{x} / {y} = {x / y}")
        else:
            print("Ошибка!Деление на ноль нельзя!")
    elif choice == '7':
        print(f"{x} ** {2} = {x ** 2}")
    elif choice == '8':
        print(f"{x} ** {3} = {x ** 3}")      
    else:
        print("Неверный ввод!")
        
if __name__ == "__main__":
    calculator()