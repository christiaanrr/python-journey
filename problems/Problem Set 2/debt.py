# Write a program to calculate the credit card balance after one year if a person only pays the
# minimum monthly payment required by the credit card company each month.
# The following variables contain values as described below:
#
# balance - the outstanding balance on the credit card
#
# annualInterestRate - annual interest rate as a decimal
#
# monthlyPaymentRate - minimum monthly payment rate as a decimal
#
# For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months,
# print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print
#
# Remaining balance: 813.41

def newBalance(balance, annualInterestRate, monthlyPaymentRate):
    """
    :param balance: balance on card
    :param annualInterestRate: annual interest
    :param monthlyPaymentRate: minimum monthly payment
    :return: remaining balance after month
    """
    for i in range(12):
        minimumPayment = balance * monthlyPaymentRate
        unpaidBalance = balance - minimumPayment
        interest = unpaidBalance * annualInterestRate/12
        newBalance = unpaidBalance + interest
        balance = newBalance
    return round(newBalance,2)
