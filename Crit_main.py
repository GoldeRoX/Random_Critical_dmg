import random
import time


print('Witaj w "Menu_Programowania", wpisz interesującą Cię kwestie ... Masz do wybrania: "Crit", :')

for i in range(3):
    time.sleep(0.5)
    print('.')

X = input()





if X == 'Crit':
    print("Wybierz procent ( liczba całkowita ) na pojawienie się Critica: ...")
    X = input()
    X = int(X)

    print("Masz ",X,"% szansy na DMG Crit.")


    for i in range(3):
        time.sleep(0.5)
        print('.')


    losowanie =  random.randint(1,100)
    losowanie = int(losowanie)

    if X >= losowanie:
        print('Crit.! DMG twojego ataku zostanie zwiększony o 100%')
    else:
        print("zwykły DMG")
else:
    print('Nie ma tego czego szukasz!')

