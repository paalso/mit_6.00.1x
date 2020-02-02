# https://courses.edx.org/courses/course-v1:MITx+6.00.1x+1T2020/courseware/0de4fecc5a9a4749923133fcf4de181f/e137765987514da7851a59dedeb5ecec/1?activate_block_id=block-v1%3AMITx%2B6.00.1x%2B1T2020%2Btype%40vertical%2Bblock%40091c114ae1b944aa81dd73b9199845cc


def finalBalance(startBalance, annualInterestRate, monthlyPayment, months = 12):
    """
    Input:
    startBalance - the initial balance on the credit card
    annualInterestRate - annual interest ratel
    monthlyPaymentRate - fixed monthly payment rate
    months - period in months (12 by default)

    Returns: float, rounded to 0.01 (i.e. to the cent) -
    the credit card balance after given period
    """
    monthlyInterestRate= annualInterestRate / 12.0
    balance = startBalance

    for i in range(months):
        monthlyUnpaidBalance = balance - monthlyPayment
        interest = monthlyInterestRate * monthlyUnpaidBalance
        balance = monthlyUnpaidBalance + interest

    return round(balance, 2)


balance = 3926
annualInterestRate = 0.2

monthlyPayment = int(balance / 120) * 10   # initial monthlyPayment guess
while True:
    monthlyPayment += 10
    if finalBalance(balance, annualInterestRate, monthlyPayment) <= 0:
        break

print("Lowest Payment: {}".format(monthlyPayment))
