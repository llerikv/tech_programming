import math
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
    print("9. disc")
    
    choice = input("Введите номер операции (1/2/3/4/5/6/7/8/9): ")
    if choice in ['1', '2', '3', '4', '6']:
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
        x = float(input("Введите число для вычисления квадратного корня:"))
        sqrt = x ** (0.5) 
        print(f"{x} = {sqrt}")
    elif choice == '6':
        if y != 0:
            print(f"{x} / {y} = {x / y}")
        else:
            print("Ошибка!Деление на ноль нельзя!")
    elif choice == '7':
        x = float(input("Введите число для возведения в квадрат:"))
        print(f"{x} ** {2} = {x ** 2}")
    elif choice == '8':
        x = float(input("Введите число для возведение в куб:"))
        print(f"{x} ** {3} = {x ** 3}")      
    if choice == '9':
        a = float(input("Введите коэффициент a: "))
        b = float(input("Введите коэффициент b: "))
        c = float(input("Введите коэффициент c: "))       
        D = b**2 - 4*a*c
        print(f"Дискриминант = {D}")       
    if D > 0:
        x1 = (-b + math.sqrt(D) / (2*a))
        x2 = (-b - math.sqrt(D) / (2*a))
        print(f"Корни уровнения:x1 и x2 = {x1} , {x2}")
    elif D == 0:
        x = -b / (2*a)
        print(f"Единственный корень: x = {x}")
    elif D < 0:
        print("Корней нет (D < 0)")
    else:
        print("Неверный ввод!")
        
if __name__ == "__main__":
    calculator()