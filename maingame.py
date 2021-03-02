print('\t[]\t[]\t[]\nTry and guess where the ball is.')
playerinput = input('Guess a number between 1 and 3:\n')

ball_list = [0,0,1]

from random import shuffle

shuffle(ball_list)

if playerinput == '1' and ball_list[0] == 1:
    print('\t[0]\t[]\t[]')
    print('RIGHT!')
elif playerinput == '2' and ball_list[1] == 1:
    print('\t[]\t[0]\t[]')
    print('RIGHT!')
elif playerinput == '3' and ball_list[2] == 1:
    print('\t[]\t[]\t[0]')
    print('RIGHT!')
else:
    if ball_list[0] == 1:
        print('\t[]\t[]\t[]\n')
        print('\t0\tX\tX')
    elif ball_list[1] == 1:
        print('\t[]\t[]\t[]\n')
        print('\tX\t0\tX')
    elif ball_list[2] == 1:
        print('\t[]\t[]\t[]\n')
        print('\tX\tX\t0')
    else:
        pass
    print('WRONG!')