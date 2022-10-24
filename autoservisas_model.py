from sqlalchemy import Column, Integer, String, ForeignKey, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///data/autoservisas.db")
Base = declarative_base()


class Savininkas(Base):
    __tablename__ = "savininkas"
    id = Column(Integer, primary_key=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    tel_nr = Column("tel_numeris", String)
    el_pastas = Column("el_pastas", String, unique=True)

    def __init__(self, vardas, pavarde, tel_nr, el_pastas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.tel_nr = tel_nr
        self.el_pastas = el_pastas

    def __repr__(self):
        return f"{self.id}, {self.vardas} {self.pavarde}, {self.tel_nr}, {self.el_pastas}"

# class Klientas(Base):
#     __tablename__ = "klientas"
    


class Autoservisas(Base):
    __tablename__ = "autoservisas"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column("pavadinimas", String)
    adresas = Column("adresas", String)
    tel_numeris = Column("tel_numeris", String)

    def __init__(self, pavadinimas, adresas, tel_numeris, automobilio_id):
        self.pavadinimas = pavadinimas
        self.adresas = adresas
        self.tel_numeris = tel_numeris
        self.automobilio_id = automobilio_id

    def __repr__(self):
        return f"{self.id}, {self.pavadinimas}, {self.adresas}, {self.tel_numeris}"


class Automobilis(Base):
    __tablename__ = "automobilis"
    id = Column(Integer, primary_key=True)
    gamintojas = Column("gamintojas", String)
    modelis = Column("modelis", String)
    pagaminimo_metai = Column("pagaminimo_metai", String)
    variklio_turis = Column("variklio_turis_litrais", Float)
    variklio_galia = Column("Variklio_galia_kW", Integer)
    savininko_id = Column("savininko_id", Integer, ForeignKey("savininkas.id"))
    savininkas = relationship("Savininkas")

    def __init__(self, gamintojas, modelis, pagaminimo_metai, variklio_turis, variklio_galia, savininko_id):
        self.gamintojas = gamintojas
        self.modelis = modelis
        self.pagaminimo_metai = pagaminimo_metai
        self.variklio_turis = variklio_turis
        self.variklio_galia = variklio_galia
        self.savininko_id = savininko_id

    def __repr__(self):
        return f"{self.id}, {self.gamintojas}, {self.modelis}, {self.pagaminimo_metai}, {self.variklio_turis}, {self.variklio_galia}"


class Darbuotojas(Base):
    __tablename__ = "darbuotojas"
    id = Column(Integer, primary_key=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    asmens_kodas = Column("asmens_kodas", Integer, unique=True)
    tel_numeris = Column("tel_numeris", String)
    autoserviso_id = Column("autoserviso_id", Integer, ForeignKey("autoservisas.id"))
    autoservisas = relationship("Autoservisas")

    def __init__(self, vardas, pavarde, asmens_kodas, tel_numeris, autoserviso_id):
        self.vardas = vardas
        self.pavarde = pavarde
        self.asmens_kodas = asmens_kodas
        self.tel_numeris = tel_numeris
        self.autoserviso_id = autoserviso_id

    def __repr__(self):
        return f"{self.vardas} {self.pavarde}, {self.asmens_kodas}, {self.tel_numeris}"

if __name__ == "__main__":
    Base.metadata.create_all(engine)