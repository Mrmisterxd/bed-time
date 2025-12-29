import os 
import sys 
import time 
import random
import colorama
import winsound
import msvcrt
colorama.init(autoreset=True)

seconds = 0
min = 0
hoursss = 0

red = colorama.Fore.RED
green = colorama.Fore.GREEN
yellow = colorama.Fore.YELLOW 
redL = colorama.Style.BRIGHT + colorama.Fore.RED
greenL = colorama.Style.BRIGHT + colorama.Fore.GREEN
yellowL = colorama.Fore.YELLOW + colorama.Style.BRIGHT
reset = colorama.Style.RESET_ALL 

gl = greenL
rl = redL
r = red
g = green
yl = yellowL
y = yellow
rs = reset

while True:
    os.system('cls')
    print('Choose an option:')
    print('1. Set bedtime in seconds')
    print('2. Turn off bedtime')
    print('3. Set bedtime in hours')
    print('4. Set bedtime in minutes')
    print('5. Russian roulette')
    print('6. Check bedtime')
    print('7. Exit')
    try:
        a = int(input('Enter your choice:'))
    except ValueError:
        time.sleep(1)
        print(yl + 'Numbers only. choice number 1-7')
        time.sleep(1)
        print('Press any button to return...')
        msvcrt.getch()
        time.sleep(0.3)
        continue
    if a not in range(1, 8):
        time.sleep(1)
        print(yl + 'Choice number 1-7')
        time.sleep(1)
        print('Press any button to return...')
        msvcrt.getch()
        time.sleep(0.3)
        continue

    print (a)
    
    if a == 1:
        try:
         seconds = int(input('Set time in seconds ( 1 hour - 3600 seconds) - '))
        except ValueError:
            time.sleep(1)
            print(yl + 'Numbers only')
            time.sleep(1)
            print('Press any button to return...')
            msvcrt.getch()
            time.sleep(0.3)
            continue
        min = hoursss = 0
        print('Timer will be set for ' + str(seconds) + ' seconds ')
        time.sleep(1)
        os.system('shutdown -s -t ' + str(seconds))
        print(gl + 'Command ended')
        time.sleep(1)
        print('Press any button to return...')
        msvcrt.getch()
        time.sleep(0.3)
        continue
    
    elif a == 2:
        os.system('shutdown -a')
        seconds = min = hoursss = 0
        time.sleep(1)
        print(gl + 'Command ended')
        time.sleep(1)
        print('Bedtime was off')
        time.sleep(1)
        print('Press any button to return...')
        msvcrt.getch()
        time.sleep(0.3)
        continue

    elif a == 7:
        print('Goodbye')
        time.sleep(1)
        sys.exit()
    
    elif a == 3:
        print('Set bedtime in hours (decimal values allowed, e.g. 1.5)')
        try:
            hoursss = float(input('Enter hours:'))
            hrstoscnds = int(3600 * hoursss)
            time.sleep(1)
            os.system('shutdown -s -t ' + str(hrstoscnds) )
            seconds = min = 0
            print(gl + 'Command end' ', bedtime set to ' + str(hoursss) + ' hours ( ' +str(hrstoscnds) + ' seconds )')
            time.sleep(1)
            print('Press any button to return...')
            msvcrt.getch()
            time.sleep(0.3)
            continue
        except ValueError:
            time.sleep(1)
            print(yl + 'Number, not word  ')
            time.sleep(1)
            print('Press any button to return...')
            msvcrt.getch()
            time.sleep(0.3)
            continue
    
    elif a == 5:
        print('Russian roulette.')
        while True:
            print('1 -', rl + 'Yes.')  
            print('2 -', gl + 'No.')
            try:
                choicep = int(input('Will you play?: '))             
            except ValueError:
                time.sleep(1)
                print(yl +'Number only.')
                time.sleep(1)
                print('Press any button to return...')
                msvcrt.getch()
                time.sleep(0.3)
                continue
            if choicep == 2:
                print(r + 'Wise decision.')
                time.sleep(0.5)
                break
            while True:
                for dlr in ' - Dealer: ':
                    print(dlr, end = '', flush=True)
                time.sleep(0.4)
                for dlr in 'choose 1 or 2. ':
                    print(dlr, end = '', flush=True)
                    if dlr != ' ':
                        winsound.Beep(230, 17)
                    time.sleep(0.08)
                time.sleep(0.4)
                for dlr in 'One shotgun, ':
                    print(dlr, end = '', flush=True)
                    if dlr != ' ':
                        winsound.Beep(230, 17)
                    time.sleep(0.08)
                time.sleep(0.4)
                for dlr in 'one shell... ':
                    print(dlr, end = '', flush=True)
                    if dlr != ' ':
                        winsound.Beep(230, 17)
                    time.sleep(0.08)
                print()                                
                try:                 
                 choicedie = int(input('1 or 2? '))
                except ValueError:
                    time.sleep(1)
                    print('...')
                    time.sleep(1)
                    print(r + "Don't get funny to me... only 1 or 2...")
                    time.sleep(2)
                    continue
                if choicedie not in (1, 2):
                    time.sleep(1)
                    print('...')
                    time.sleep(1)
                    print(r + "Don't get funny to me... only 1 or 2...")
                    time.sleep(2)
                    continue
                gun = random.randint(1, 2)
                if choicedie == gun:
                    print(gl + 'You survived.')
                    time.sleep(1.33)
                    break
                else:
                    print(rl + 'BANG! Never see you again.')
                    time.sleep(0.8)
                    os.system('shutdown -s -t 0')
                    print(r +'You lose.')
                    time.sleep(3)
                                    
    elif a == 4:
        print('Set bedtime in minutes (decimal values allowed, f.e. 2.5)')
        try:
            min = float(input('Enter minutes:'))
            minsec = int(60 * min)
            time.sleep(1)
            os.system('shutdown -s -t ' + str(minsec) )
            seconds = hoursss = 0
            print('Command end, bedtime set to ' + str(min) + ' minutes ( ' +str(minsec) + ' seconds. )')
            time.sleep(1)
            print('Press any button to return...')
            msvcrt.getch()
            time.sleep(0.3)
            continue
        except ValueError:
            time.sleep(1)
            print(yl + 'Number, not word')
            time.sleep(1)
            print('Press any button to return...')
            continue

    elif a == 6:
        if seconds or min or hoursss:
            print(gl +'Bedtime was set.')
            print(yl + 'This is only for this program session')
            print('If you enabled or disabled bedtime via Windows -', yl + "this is won't show here")
            print('- Option 6 is just for peace of mind and to verify the successful completion or failure of one of the items.')
            print('Press any button to return...')
            msvcrt.getch()
            time.sleep(0.3)
            continue
        else:
            print(rl +'Bedtime is not set.')
            print(yl + 'This is only for this program session')
            print('If you enabled or disabled bedtime via Windows -', yl + "this is won't show here")
            print('- Option 6 is just for peace of mind and to verify the successful completion or failure of one of the items.')
            print('Press any button to return...')
            msvcrt.getch()
            time.sleep(0.3)
            continue

