from autoservisas_model import *
from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)()

def prideti_savininka():
    print("--- Prideti asmeni ---")
    vardas = input("Vardas: ")
    pavarde = input("Pavarde: ")
    tel_nr = input("Telefono numeris: ")
    el_pastas = input("Elektroninis pastas: ")
    savininkas = Savininkas(vardas, pavarde, tel_nr, el_pastas)
    session.add(savininkas)
    session.commit()

def prideti_autoservisa():
    print("--- Prideti autoservisa ---")
    pavadinimas = input("Pavadinimas: ")
    adresas = input("Adresas: ")
    tel_numeris = input("Telefono numeris: ")
    autoservisas = Autoservisas(pavadinimas, adresas, tel_numeris)
    session.add(autoservisas)
    session.commit()

def savininkai():
    print("--- Asmenys ---")
    zmones = session.query(Savininkas).all()
    for savininkas in zmones:
        print(savininkas)

def prideti_automobili():
    savininkai()
    savininkas_id = int(input("Pasirinkite asmens ID: "))
    print("--- Prideti automobili ---")
    gamintojas = input("Gamintojas: ")
    modelis = input("Modelis")
    pagaminimo_metai = input("Pagaminimo metai: ")
    variklio_turis = float(input("Variklio turis: "))
    variklio_galia = int(input("Variklio galia: "))
    automobilis = Automobilis(gamintojas=gamintojas, modelis=modelis, pagaminimo_metai=pagaminimo_metai, variklio_turis=variklio_turis, variklio_galia=variklio_galia, savininko_id=savininkas_id)
    session.add(automobilis)
    session.commit()




while True:
    print("Pasirinkite")
    print("1: Prideti asmeni")
    print("2: Prideti autoservisa")
    print("3: Prideti automobili")
    pasirinkimas = int(input())
    if pasirinkimas == 1:
        prideti_savininka()
    elif pasirinkimas == 2:
        prideti_autoservisa()
    elif pasirinkimas == 3:
        prideti_automobili()






# pasirinkti savininka ir pasirinkti automobili ir pasirinkti kokiame servise jy tvarkyti