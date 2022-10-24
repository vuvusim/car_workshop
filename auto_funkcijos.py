from autoservisas_model import *
from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)()

def sukurti_savininka():
    print("--- Prideti asmeni ---")
    vardas = input("Vardas: ")
    pavarde = input("Pavarde: ")
    tel_nr = input("Telefono numeris: ")
    el_pastas = input("Elektroninis pastas: ")
    savininkas = Savininkas(vardas, pavarde, tel_nr, el_pastas)
    session.add(savininkas)
    session.commit()

