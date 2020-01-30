# https://courses.edx.org/courses/course-v1:MITx+6.00.1x+1T2020/courseware/0de4fecc5a9a4749923133fcf4de181f/62f08cc899344863a1ab678aee506dec/

PROMPT = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate \
the guess is too low. Enter 'c' to indicate I guessed correctly. "

print('Please think of a number between 0 and 100!')

lower = 0
upper = 100

while True:
    mid = (lower + upper) // 2
    while True:
        print("Is your secret number {}?".format(mid))
        answer = input(PROMPT).lower()
        if answer not in ('h', 'l', 'c'):
            print('Sorry, I did not understand your input.')
        else:
            break

    if answer == 'h':
        upper = mid
    elif answer == 'l':
        lower = mid
    else:
        break

##    print ('Lower: {}, upper: {}, mid = {}'.format(lower, upper, mid))

    if upper - lower == 2:
        mid = lower + 1
        break

print("Game over. Your secret number was: {}".format(mid))
