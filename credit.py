salary = float(input("Введите сумму вашей зарплаты:"))
rating = float(input("Введите ваш кредитный рейтинг:"))

if salary > 50000:
    if rating > 700:
        print("Кредит одобрен с низкой процентной ставкой.")
    else:
        print("Кредит одобрен,но с высокой процентной ставкой.")
        
else:
    if rating > 700:
        print("Кредит одобрен,но с жесткими условиями")
    else:
        print("Кредит отклонен из-за низкой зарплаты и рейтинга")