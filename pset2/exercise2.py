# https://courses.edx.org/courses/course-v1:MITx+6.00.1x+1T2020/courseware/0de4fecc5a9a4749923133fcf4de181f/62f08cc899344863a1ab678aee506dec/

print('Please think of a number between 0 and 100!')

lower = 1
upper = 100

while True:
    mid = (lower + upper) // 2
    while True:
        print("Is your secret number {}?".format(mid))
        print("Enter 'h' to indicate the guess is too high.",
            "Enter 'l' to indicate the guess is too low.",
            "Enter 'c' to indicate I guessed correctly. l")
        answer = input().lower()
        if answer not in ('h', 'l', 'c'):
            print('Sorry, I did not understand your input.')
        else:
            break

    if answer == 'h':
        upper = mid - 1
    elif answer == 'l':
        lower = mid + 1
    else:
        break

    if lower == upper:
        mid = lower
        break

print("Game over. Your secret number was: {}".format(mid))
