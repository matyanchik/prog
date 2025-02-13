def calculate_credit(principal, rate, term):
    """
    Рассчитывает ежемесячный платёж аннуитетного кредита.
    
    :param principal: Сумма кредита
    :param rate: Годовая процентная ставка (в %)
    :param term: Срок кредита (в месяцах)
    :return: График платежей (список кортежей: (месяц, платеж, остаток долга))
    """
    monthly_rate = rate / 12 / 100
    annuity = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -term)
    
    schedule = []
    balance = principal
    
    for month in range(1, term + 1):
        interest = balance * monthly_rate
        principal_payment = annuity - interest
        balance -= principal_payment
        schedule.append((month, round(annuity, 2), round(balance, 2)))
    
    return schedule