# Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card
# balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month,
# but instead is a constant amount that will be paid each month.
#
# In this problem, we will not be dealing with a minimum monthly payment rate.
#
# The following variables contain values as described below:
#
# balance - the outstanding balance on the credit card
#
# annualInterestRate - annual interest rate as a decimal
#
# The program should print out one line: the lowest monthly payment that will pay off all debt
# in under 1 year, for example:
#
# Lowest Payment: 180

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
            newBalance = bal - lowestPay
            interest = newBalance * (annualInterestRate / 12)
            bal = newBalance + interest
    print('Lowest Payment: ' + str(round(lowestPay, 2)))
