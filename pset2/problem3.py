# https://courses.edx.org/courses/course-v1:MITx+6.00.1x+1T2020/courseware/0de4fecc5a9a4749923133fcf4de181f/e137765987514da7851a59dedeb5ecec/1?activate_block_id=block-v1%3AMITx%2B6.00.1x%2B1T2020%2Btype%40vertical%2Bblock%40091c114ae1b944aa81dd73b9199845cc


def root(lowerBound, upperBound, eps, f):
    """
    Calculates the given function root (i.e equation f(x) = 0 solution)
    within the given segment with the given accuracy

    Input:
    lowerBound, float - lower bound of the segment
    upperBound, float - upper bound of the segment
    eps, float - accuracy
    f - monotonic within the given segment function
    """
    increasing = f(upperBound) > f(lowerBound)

    while (upperBound - lowerBound > eps):
        midPoint = (lowerBound + upperBound) / 2

        if f(midPoint) == 0:
            return midPoint

        if increasing:
            if f(midPoint) > 0:
                upperBound = midPoint
            else:
                lowerBound = midPoint
        else:
            if f(midPoint) < 0:
                upperBound = midPoint
            else:
                lowerBound = midPoint

    return midPoint


def finalBalance(startBalance, annualInterestRate, monthlyPayment, months = 12):
    """
    Input:
    startBalance - the initial balance on the credit card
    annualInterestRate - annual interest rate
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


balance = 150593
annualInterestRate = 0.21


def balanceFunc(monthlyPayment):
    return finalBalance(balance, annualInterestRate, monthlyPayment)


lowerPaymentBound = balance / 12 # initial monthlyPayment lower guess

# initial monthlyPayment upper guess
upperPaymentBound = (balance * (1 + annualInterestRate / 12) ** 12) / 12

monthlyPayment = round(
    root(lowerPaymentBound, upperPaymentBound, 0.01, balanceFunc), 2
)

print("Lowest Payment: {}".format(monthlyPayment))
