from auto_funkcijos import *

while True:
    print("Pasirinkite")
    print("1: Prideti asmeni")
    print("2: Prideti automobili")
    print("3: Prideti autoservisa")
    print("4: Prideti darbuotoja")
    print("5: Prideti i autoserviso klientu sarasa")
    print("6: Perziureti")
    print("7: Istrinti")
    print("9: Perziureti masinas")
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
        prideti_i_klientu_sarasa()
    elif pasirinkimas == 6:
        perziura()
    elif pasirinkimas == 7:
        istrinti()
    elif pasirinkimas == 9:
        perziurejimas()
    elif pasirinkimas == 0:
        break