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