def calculate_installment(principal, term):
    """
    Рассчитывает равномерные платежи по рассрочке (без процентов).
    
    :param principal: Сумма покупки
    :param term: Срок рассрочки (в месяцах)
    :return: График платежей (список кортежей: (месяц, платеж, остаток долга))
    """
    monthly_payment = principal / term
    balance = principal
    schedule = []

    for month in range(1, term + 1):
        balance -= monthly_payment
        schedule.append((month, round(monthly_payment, 2), round(balance, 2)))

    return schedule