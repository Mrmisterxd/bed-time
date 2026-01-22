import os 
import sys 
import time 
import random
import colorama
import winsound
import msvcrt
colorama.init(autoreset=True)

seconds = 0
minutes = 0
hours = 0

red = colorama.Fore.RED
green = colorama.Fore.GREEN
yellow = colorama.Fore.YELLOW 
redLight = colorama.Style.BRIGHT + colorama.Fore.RED
greenLight = colorama.Style.BRIGHT + colorama.Fore.GREEN
yellowLight = colorama.Fore.YELLOW + colorama.Style.BRIGHT 

def PressButon():
    time.sleep(1)
    print('Press any button to return...')
    msvcrt.getch()
    time.sleep(0.3)

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
        a = int(input('Enter your choice: '))
    except ValueError:
        time.sleep(1)
        print(yellowLight + 'Numbers only. choice number 1-7')
        PressButon()
        continue
    if a not in range(1, 8):
        time.sleep(1)
        print(yellowLight + 'Choice number 1-7')
        PressButon()
        continue

    print (a)
    
    if a == 1:
        print('Set time in seconds (1 hour - 3600 seconds)')
        try:
         seconds = int(input('Enter seconds: '))
        except ValueError:
            time.sleep(1)
            print(yellowLight + 'Numbers only')
            PressButon()
        minutes = hours = 0
        time.sleep(1)
        os.system('shutdown -s -t ' + str(seconds))
        print('Command ended' ',bedtime set to ' + str(seconds) + ' seconds' )
        PressButon()
        continue
    
    elif a == 2:
        os.system('shutdown -a')
        seconds = minutes = hours = 0
        time.sleep(1)
        print(greenLight + 'Command ended')
        time.sleep(1)
        print('Bedtime was off')
        PressButon()
        continue
  
    elif a == 3:
        print('Set bedtime in hours (decimal values allowed, e.g. 1.5)')
        try:
            hours = float(input('Enter hours: '))
            hours_seconds = int(3600 * hours)
            time.sleep(1)
            os.system('shutdown -s -t ' + str(hours_seconds) )
            seconds = minutes = 0
            print('Command end' ', bedtime set to ' + str(hours) + ' hours (' +str(hours_seconds) + ' seconds)')
            PressButon()
            continue
        except ValueError:
            time.sleep(1)
            print(yellowLight + 'Number, not word')
            PressButon()
            continue

    elif a == 4:
        print('Set bedtime in minutes (decimal values allowed, f.e. 2.5)')
        try:
            minutes = float(input('Enter minutes: '))
            minute_seconds = int(60 * minutes)
            time.sleep(1)
            os.system('shutdown -s -t ' + str(minute_seconds) )
            seconds = hours = 0
            print('Command end, bedtime set to ' + str(minutes) + ' minutes (' +str(minute_seconds) + ' seconds)')
            PressButon()
            continue
        except ValueError:
            time.sleep(1)
            print(yellowLight + 'Number, not word')
            PressButon()
            continue        
    
    elif a == 5:
        while True:
            os.system('cls')
            print('Russian roulette.')
            print('1 -', redLight + 'Yes.')  
            print('2 -', greenLight + 'No.')
            try:
                choicep = int(input('Will you play?: '))             
            except ValueError:
                time.sleep(1)
                print(yellowLight +'Number only.')
                PressButon()
                continue
            if choicep == 2:
                print(red + 'Wise decision.')
                time.sleep(0.5)
                break
            while True:
                for dealer in ' - Dealer: ':
                    print(dealer, end = '', flush=True)
                time.sleep(0.4)
                for dealer in 'choose 1 or 2. ':
                    print(dealer, end = '', flush=True)
                    if dealer != ' ':
                        winsound.Beep(230, 17)
                    time.sleep(0.08)
                time.sleep(0.4)
                for dealer in 'One shotgun, ':
                    print(dealer, end = '', flush=True)
                    if dealer != ' ':
                        winsound.Beep(230, 17)
                    time.sleep(0.08)
                time.sleep(0.4)
                for dealer in 'one shell... ':
                    print(dealer, end = '', flush=True)
                    if dealer != ' ':
                        winsound.Beep(230, 17)
                    time.sleep(0.08)
                print()
                print('1 or 2?')                         
                try:                 
                 choiceDie = int(input('Enter your choice: '))
                except ValueError:
                    time.sleep(1)
                    print('...')
                    time.sleep(1)
                    print(red + "Don't get funny to me... only 1 or 2...")
                    time.sleep(2)
                    continue
                if choiceDie not in (1, 2):
                    time.sleep(1)
                    print('...')
                    time.sleep(1)
                    print(red + "Don't get funny to me... only 1 or 2...")
                    time.sleep(2)
                    continue
                gun = random.randint(1, 2)
                if choiceDie == gun:
                    print(greenLight + 'You survived.')
                    time.sleep(1.33)
                    break
                else:
                    print(redLight + 'BANG! Never see you again.')
                    time.sleep(0.8)
                    os.system('shutdown -s -t 0')
                    print(red +'You lose.')
                    time.sleep(3)

    elif a == 6:
        if seconds or minutes or hours:
            time.sleep(1)
            print(greenLight +'Bedtime was set.')
            print(yellowLight + 'This is only for this program session')
            print('If you enabled or disabled bedtime via Windows -', yellowLight + "this is won't show here")
            print('- Option 6 is just for peace of mind and to verify the successful completion or failure of one of the items.')
            PressButon()
            continue
        else:
            time.sleep(1)
            print(redLight +'Bedtime is not set.')
            print(yellowLight + 'This is only for this program session')
            print('If you enabled or disabled bedtime via Windows -', yellowLight + "this is won't show here")
            print('- Option 6 is just for peace of mind and to verify the successful completion or failure of one of the items.')
            PressButon()
            continue

    elif a == 7:
        print('Goodbye')
        time.sleep(1)
        sys.exit()
