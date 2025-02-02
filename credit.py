salary = float(input(":"))
rating = float(input(":"))

if salary > 50000:
    if rating > 700:
        print("Кредит одобрен с низкой процентной ставкой.")
    else:
        print("Кредит одобрен,но с высокой процентной ставкой.")