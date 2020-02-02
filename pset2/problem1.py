# https://courses.edx.org/courses/course-v1:MITx+6.00.1x+1T2020/courseware/0de4fecc5a9a4749923133fcf4de181f/e137765987514da7851a59dedeb5ecec/2?activate_block_id=block-v1%3AMITx%2B6.00.1x%2B1T2020%2Btype%40vertical%2Bblock%40d71ae172df5d46e89ac3607d6328a45f

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate= annualInterestRate / 12.0

for i in range(12):
    minMontlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minMontlyPayment
    balance = (1 + monthlyInterestRate) * monthlyUnpaidBalance

print("Remaining balance: {}".format(round(balance, 2)))
