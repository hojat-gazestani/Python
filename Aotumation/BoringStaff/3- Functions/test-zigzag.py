import sys, time

intend = 0
intend1 = 20
intend2 = 0
makeIntend = True

try:
    while True:
        print(' ' * intend1 , end='')
        print('**********',end='')
        print(' ' * intend , end='')
        print(' ' * intend2 , end='')
        print('**********')
        time.sleep(0.1)

        if makeIntend:
            if intend == 20:
                makeIntend = False
            else:
                intend += 1
                intend1 -=1
                intend2 +=1
        else:
            if intend == 0:
                makeIntend = True
            else:
                intend -= 1
                intend1 += 1
                intend2 -=1

except KeyboardInterrupt:
    sys.exit()

    
