def fixedPayment(balance, annualInterestRate):
    """
    :param balance: balance on card
    :param annualInterestRate: annual interest rate
    :return: fixed payment amount monthly (doesn't change)
    """

    lowestPay = 0
    bal = balance
    while bal > 0:
        lowestPay += 10
        bal = balance
        for i in range(1, 13):
            unpaidBalance = bal - lowestPay
            interest = unpaidBalance * (annualInterestRate / 12)
            newBalance = unpaidBalance + interest
            bal = newBalance
    print('Lowest Payment: ' + str(round(lowestPay, 2)))
