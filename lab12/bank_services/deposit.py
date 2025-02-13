def calculate_deposit(principal, rate, term, custom_rates=None):
    """
    Рассчитывает вклад с ежемесячной капитализацией процентов.
    
    :param principal: Начальная сумма вклада
    :param rate: Годовая процентная ставка (в %) (используется, если custom_rates=None)
    :param term: Срок вклада (в месяцах)
    :param custom_rates: Список индивидуальных ставок для каждого месяца (может быть None)
    :return: График накоплений (список кортежей: (месяц, ставка, сумма на счёте))
    """
    balance = principal
    schedule = []

    for month in range(1, term + 1):
        current_rate = custom_rates[month - 1] if custom_rates else rate
        monthly_rate = current_rate / 12 / 100
        balance += balance * monthly_rate
        schedule.append((month, round(current_rate, 2), round(balance, 2)))

    return schedule