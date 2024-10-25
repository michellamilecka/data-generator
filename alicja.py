from sqlalchemy import create_engine,NVARCHAR,ForeignKey, Column, Integer, Date, Enum, DateTime, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import relationship
import pyodbc
import enum

# dodac michelli komentarze żeby:
# 1. zmieniła sposob zgloszenia 'in person'
# 2. usunela z rodzajow zdarzen 'manslaughter'

# TO DO
# 1. ogarnac dziedziczenie po 'is a'
# 2. polaczyc sie z baza danych

# Definiowanie bazowej klasy dla modeli
Base = declarative_base()

# enum dla sposobu zgloszenia
# class SposobZgloszenia(enum.Enum):
#     telefonicznie = "by phone"
#     osobiscie = "in person"
    

# class Zgloszenie(Base):
#     __tablename__ = 'reports'
    
#     numerZgloszenia = Column(Integer, primary_key=True, autoincrement=True)
#     sposob = Column(Enum(SposobZgloszenia), nullable=False)
#     dataZgloszenia = Column(Date, nullable=False)
#     opis = Column(NVARCHAR(600), nullable=False)
#     ID_Posterunku = Column(Integer, nullable=False)
#     ID_Osoby = Column(Integer, nullable=False)
#     numerOdznaki = Column(Integer, nullable=False)


# # enum dla rodzajów zdarzeń
# class RodzajZdarzenia(enum.Enum):
#     kradziez = "theft"
#     porwanie = "kidnapping"
#     zaginiecie = "disappearance"
#     morderstwo = "murder"
#     napasc = "assault"
#     przemocDomowa = "domestic violence"
#     przemocNaTleSeksualnym = "rape"
#     grozby = "threatening"
#     wlamanie = "burglary"
#     oszustwo = "fraud"
#     praniePieniedzy = "money laundering"
#     unikaniePodatkow = "tax evasion"
#     kradziezTozsamosci = "identity theft"


# class Zdarzenie(Base):
#     __tablename__ = 'incidents'

#     ID_Zdarzenia = Column(Integer, primary_key=True, autoincrement=True)
#     dataZdarzenia = Column(Date, nullable=False)
#     rodzaj = Column(Enum(RodzajZdarzenia), nullable=False)
#     opis = Column(NVARCHAR(1500), nullable=False)
#     godzina = Column(DateTime, nullable=False)
#     adres = Column(NVARCHAR(50), nullable=False)


# class AnalizaZgloszenia(Base):
#     __tablename__ = 'analysis of reports'

#     ID_analizyZgloszenia = Column(Integer, primary_key=True, autoincrement=True)
#     rozpoczecieSledztwa = Column(Boolean, nullable=False)
#     #tu dodatkowa tabela raczej bedzie ale narazie dam nvarchar
#     podstawy = Column(NVARCHAR(200), nullable=False)


# # enum dla statusów śledztwa
# class StatusSledztwa(enum.Enum):
#     wTrakcie = "in progress"
#     zamknieteNierozwiazane = "closed-unresolved"
#     zamknieteRozwiazane = "closed-resolved"
#     otwarteRozwiazane = "open-resolved"


# class Sledztwo(Base):
#     __tablename__ = 'investigations'

#     numerSledztwa = Column(Integer, primary_key=True, autoincrement=True)
#     dataRozpoczecia = Column(Date, nullable=False)
#     dataZakonczenia = Column(Date, nullable=False)
#     status = Column(Enum(StatusSledztwa), nullable=False)
#     numerOdznaki = Column(Integer, nullable=False)


# # enum dla rodzaju materiału dowodowego
# class RodzajMaterialuDowodowego(enum.Enum):
#     zeznanie = "testimony"
#     biologiczny = "biological"
#     rzeczowy = "material"
#     dokument = "document"


# class MaterialDowodowy(Base):
#     __tablename__ = 'evidence'

#     ID_materialuDowodowego = Column(Integer, primary_key=True, autoincrement=True)
#     dataZebrania = Column(Date, nullable=False)
#     miejsceZebrania = Column(NVARCHAR(50), nullable=False)
#     raport = Column(NVARCHAR(600), nullable=False)
#     rodzaj = Column(Enum(RodzajMaterialuDowodowego), nullable=False)
    

class Czynnosc(Base):
    __tablename__ = 'operations'

    ID_czynnosci = Column(Integer, primary_key=True, autoincrement=True)
    dataWykonania = Column(Date, nullable=False)
    dataZakonczenia = Column(Date, nullable=False)
    numerOdznaki = Column(Integer, nullable=False)

    # A polymorphic identity that identifies this class in the inheritance chain
    __mapper_args__ = {
        'polymorphic_identity': 'operation',  # This is the discriminator value for this class
        'polymorphic_on': ID_czynnosci  # Column to be used for polymorphism
    }


class Przesluchanie(Czynnosc):
    __tablename__ = 'interrogations'

    ID_przesluchania = Column(Integer, ForeignKey('operations.ID_czynnosci'), primary_key=True)  # Inherits ID from Czynnosc
    godzina = Column(DateTime, nullable=False)
    lokalizacja = Column(NVARCHAR(100), nullable=False)
    cel = Column(NVARCHAR(140), nullable=False)
    ID_osoby = Column(Integer, nullable=False)

    # Relationship can be added if necessary
    czynnosc = relationship("Czynnosc", backref="interrogations")

    # Polymorphic identity for this subclass
    __mapper_args__ = {
        'polymorphic_identity': 'interrogation',  # This is the discriminator value for this class
    }


# enum dla priorytetów
# class Priorytet(enum.Enum):
#     wysoki = "high"
#     sredni = "medium"
#     niski = "low"


# # enum dla wyników weryfikacji informacji
# class WynikWeryfikacji(enum.Enum):
#     pozytywny = "positive"
#     negatywny = "negative"
#     niejednoznaczny = "ambiguous"


# class WeryfikacjaInformacji(Czynnosc):
#     __tablename__ = 'information verifications'
#     #dziedziczy klucz glowny po Czynnosc

#     ID_weryfikacjiInformacji = Column(Integer, ForeignKey('czynnosci.ID_czynnosci'), primary_key=True)
#     priorytet = Column(Enum(Priorytet), nullable=False)
#     opis = Column(NVARCHAR(200), nullable=False)
#     wynik = Column(Enum(WynikWeryfikacji), nullable=False)
#     rodzaj = Column(NVARCHAR(200), nullable=False)
   

# class OgledzinyMiejscaZdarzenia(Czynnosc):
#     __tablename__ = 'site inspections'
#     #dziedziczy klucz glowny po Czynnosc

#     ID_ogledzinMiejscaZdarzenia = Column(Integer, ForeignKey('czynnosci.ID_czynnosci'), primary_key=True)
#     godzina = Column(DateTime, nullable=False)
#     adres = Column(NVARCHAR(50), nullable=False)
#     przebieg = Column(NVARCHAR(1500), nullable=False)