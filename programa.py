from auto_funkcijos import *

while True:
    print("Pasirinkite")
    print("1: Prideti asmeni")
    print("2: Prideti automobili")
    print("3: Prideti autoservisa")
    print("4: Prideti darbuotoja")
    print("5: Perziureti")
    print("6: Istrinti")
    print("0: Iseiti")
    pasirinkimas = int(input())
    if pasirinkimas == 1:
        prideti_savininka()
    elif pasirinkimas == 2:
        prideti_automobili()
    elif pasirinkimas == 3:
        prideti_autoservisa()
    elif pasirinkimas == 4:
        prideti_darbuotoja()
    elif pasirinkimas == 5:
        perziura()
    elif pasirinkimas == 6:
        istrinti()
    elif pasirinkimas == 0:
        break
