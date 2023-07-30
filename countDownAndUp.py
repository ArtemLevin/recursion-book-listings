def countDownAndUp(number):
    print(number)
    print('what do you see?')
    if number == 0:
        print('Base case is reached')
        return
    else:
        countDownAndUp(number - 1)
        print(number, 'returning')

        return


countDownAndUp(3)
