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
    modelis = input("Modelis: ")
    pagaminimo_metai = input("Pagaminimo metai: ")
    variklio_turis = float(input("Variklio turis: "))
    variklio_galia = int(input("Variklio galia: "))
    automobilis = Automobilis(gamintojas=gamintojas, modelis=modelis, pagaminimo_metai=pagaminimo_metai, variklio_turis=variklio_turis, variklio_galia=variklio_galia, savininko_id=savininkas_id)
    session.add(automobilis)
    session.commit()

def pasirinkti_servisa():
    print("--- Autoservisai ---")
    servisai = session.query(Autoservisas).all()
    for servisas in servisai:
        print(servisas)

def prideti_darbuotoja():
    pasirinkti_servisa()
    serviso_id = int(input("Pasirinkite autoserviso ID: "))
    print("--- Prideti darbuotoja ---")
    vardas = input("Vardas: ")
    pavarde = input("Pavarde: ")
    asmens_kodas = int(input("Asmens kodas: "))
    tel_numeris = input("Telefono numeris: ")
    darbuotojas = Darbuotojas(vardas=vardas, pavarde=pavarde, asmens_kodas=asmens_kodas, tel_numeris=tel_numeris, autoserviso_id=serviso_id)
    session.add(darbuotojas)
    session.commit()

def perziura():
    print("1: Asmenis")
    print("2: Autoservisus")
    print("3: Automobilius")
    print("4: Darbuotojus")
    pasirinkti = int(input("Pasirinkite: "))

    if pasirinkti == 1:
        asmenys = session.query(Savininkas).all()
        for asmuo in asmenys:
            print(asmuo)

    elif pasirinkti == 2:
        autoservisai = session.query(Autoservisas).all()
        for servisas in autoservisai:
            print(servisas)

    elif pasirinkti == 3:
        automobiliai = session.query(Automobilis).all()
        for automobilis in automobiliai:
            print(automobilis)

    elif pasirinkti == 4:
        darbuotojai = session.query(Darbuotojas).all()
        for darbuotojas in darbuotojai:
            print(darbuotojas)

def istrinti():
    print("1: Asmeni")
    print("2: Autoservisa")
    print("3: Automobili")
    print("4: Darbuotoja")
    pasirinkti = int(input("Pasirinkite: "))

    if pasirinkti == 1:
        asmenys = session.query(Savininkas).all()
        for asmuo in asmenys:
            print(asmuo)
        pasirikite = int(input("Pasirinkite asmens ID:"))
        istr_asmeni = session.query(Savininkas).get(pasirikite)
        session.delete(istr_asmeni)
        session.commit()

    elif pasirinkti == 2:
        autoservisai = session.query(Autoservisas).all()
        for servisas in autoservisai:
            print(servisas)
        pasirikite = int(input("Pasirinkite autoserviso ID:"))
        istr_autoserv = session.query(Autoservisas).get(pasirikite)
        session.delete(istr_autoserv)
        session.commit()

    elif pasirinkti == 3:
        automobiliai = session.query(Automobilis).all()
        for automobilis in automobiliai:
            print(automobilis)
        pasirikite = int(input("Pasirinkite automobilio ID:"))
        istr_auto = session.query(Automobilis).get(pasirikite)
        session.delete(istr_auto)
        session.commit()

    elif pasirinkti == 4:
        darbuotojai = session.query(Darbuotojas).all()
        for darbuotojas in darbuotojai:
            print(darbuotojas)
        pasirikite = int(input("Pasirinkite darbuotojo ID:"))
        istr_darbuotoja = session.query(Darbuotojas).get(pasirikite)
        session.delete(istr_darbuotoja)
        session.commit()

def prideti_i_klientu_sarasa():
    klientai = session.query(Savininkas).all()
    for klientas in klientai:
        print(klientas)
    kliento_id = int(input("Pasirinkite kliento ID: "))

    kliento_masina = session.query(Savininkas).get(kliento_id)
    for masina in kliento_masina.masinos:
        print(masina)
    masinos_id = int(input("Pasirinkite automobilio ID: "))
    klient = Klientas(kliento_id=kliento_id, automobilio_id=masinos_id)
    session.add(klient)
    # auto_klient = Autoservisas(kliento_id=klient)
    # session.add(auto_klient)
    session.commit()

