# To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance
# within a year. What is a reasonable lower bound for this payment value? $0 is the obvious anwer, but you can do
# better than that. If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the
# original balance, so we must pay at least this much every month. One-twelfth of the original balance is a good
# lower bound.
# The following variables contain values as described below:
#
# balance - the outstanding balance on the credit card
#
# annualInterestRate - annual interest rate as a decimal

def payment(balance, annualInterestRate):
    """
    :param balance: balance on card
    :param annualInterestRate: annual interest rate
    :return: minimum payment monthly
    """
    low = balance / 12
    high = (balance * (1 + annualInterestRate)) / 12
    bal = balance
    epsilon = 0.01
    while abs(bal) > epsilon:
        bal = balance
        minimumPay = (low + high) / 2
        for i in range(12):
            newBalance = bal - minimumPay
            interest = newBalance * annualInterestRate / 12
            bal = newBalance + interest
        if bal > 0:
            low = minimumPay
        else:
            high = minimumPay
    print('Lowest Payment: ' + str(round(minimumPay, 2)))
