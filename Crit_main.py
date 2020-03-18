import random
import time


print('Welcome to "Programming_Menu", enter the issues you are interested in ... You have to choose: "Crit",:')

for i in range(3):
    time.sleep(0.5)
    print('.')

X = input()





if X == 'Crit':
    print("Choose percentage (integer) for Critic to appear: ...")
    X = input()
    X = int(X)

    print("You have ",X,"% chance forCrit. DMG")


    for i in range(3):
        time.sleep(0.5)
        print('.')


    losowanie =  random.randint(1,100)
    losowanie = int(losowanie)

    if X >= losowanie:
        print("Crit.! Your attack's DMG will be increased by 100%")
    else:
        print("Normal DMG")
else:
    print('There is not what you are looking for')

