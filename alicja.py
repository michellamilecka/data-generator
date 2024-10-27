from sqlalchemy import create_engine,NVARCHAR,ForeignKey, Column, Integer, Date, Enum, DateTime, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import relationship
import pyodbc
import enum

# TO DO
# 1. ogarnac dziedziczenie po 'is a'
# 2. polaczyc sie z baza danych

# Definiowanie bazowej klasy dla modeli
Base = declarative_base()

# enum dla sposobu zgloszenia
class SposobZgloszenia(Base):
    __tablename__ = 'reporting_methods'

    ID_sposobuZgloszenia = Column(Integer, primary_key=True, autoincrement=True)
    nazwa = Column(NVARCHAR(10), nullable=False)
    # definiowanie relacji z Zgloszenie
    zgloszenia = relationship("Zgloszenie", back_populates="sposob")
    

class Zgloszenie(Base):
    __tablename__ = 'reports'
    
    numerZgloszenia = Column(Integer, primary_key=True, autoincrement=True)
    ID_sposobuZgloszenia = Column(Integer, ForeignKey('reporting_methods.ID_sposobuZgloszenia'), nullable=False)  # Klucz obcy do SposobZgloszenia
    dataZgloszenia = Column(Date, nullable=False)
    opis = Column(NVARCHAR(600), nullable=False)
    ID_Posterunku = Column(Integer, nullable=False)
    ID_Osoby = Column(Integer, nullable=False)
    numerOdznaki = Column(Integer, nullable=False)
    #foreign keys
    ID_zdarzenia = Column(Integer, ForeignKey('incidents.ID_zdarzenia'), primary_key=False)
    ID_analizyZgloszenia = Column(Integer, ForeignKey('analysis_of_reports.ID_analizyZgloszenia'), primary_key=False)
    # relacja
    sposob = relationship("SposobZgloszenia", back_populates="zgloszenia")

class RodzajZdarzenia(Base):
    __tablename__ = 'types_of_incidents'

    ID_rodzajuZdarzenia = Column(Integer, primary_key=True, autoincrement=True)
    nazwa = Column(NVARCHAR(20), nullable=False)
    zdarzenia = relationship("Zdarzenie", back_populates="rodzaj")


class Zdarzenie(Base):
    __tablename__ = 'incidents'

    ID_zdarzenia = Column(Integer, primary_key=True, autoincrement=True)
    dataZdarzenia = Column(Date, nullable=False)
    ID_rodzajuZdarzenia = Column(Integer, ForeignKey('types_of_incidents.ID_rodzajuZdarzenia'), nullable=False)
    opis = Column(NVARCHAR(1500), nullable=False)
    godzina = Column(DateTime, nullable=False)
    adres = Column(NVARCHAR(50), nullable=False)
    #foreign keys
    numerSledztwa = Column(Integer, ForeignKey('investigations.numerSledztwa'), primary_key=False)
    # relacja
    rodzaj = relationship("RodzajZdarzenia", back_populates="zdarzenia")


class AnalizaZgloszenia(Base):
    __tablename__ = 'analysis_of_reports'

    ID_analizyZgloszenia = Column(Integer, primary_key=True, autoincrement=True)
    rozpoczecieSledztwa = Column(Boolean, nullable=False)
    #tu dodatkowa tabela raczej bedzie ale narazie dam nvarchar
    podstawy = Column(NVARCHAR(200), nullable=False)
    # foreign keys
    numerSledztwa = Column(Integer, ForeignKey('investigations.numerSledztwa'), primary_key=False)
    # relacja
    czynnosci = relationship("PrzeprowadzonaWRamachAnalizy", back_populates="analiza")


# enum dla statusów śledztwa
class StatusSledztwa(Base):
    __tablename__ = 'investigation_status'

    ID_statusuSledztwa = Column(Integer, primary_key=True, autoincrement=True)
    nazwa = Column(NVARCHAR(20), nullable=False)


class Sledztwo(Base):
    __tablename__ = 'investigations'

    numerSledztwa = Column(Integer, primary_key=True, autoincrement=True)
    dataRozpoczecia = Column(Date, nullable=False)
    dataZakonczenia = Column(Date, nullable=False)
    ID_statusuSledztwa = Column(Integer, ForeignKey('investigation_status.ID_statusuSledztwa'), nullable=False)
    numerOdznaki = Column(Integer, nullable=False)
    status = relationship("StatusSledztwa")


# enum dla rodzaju materiału dowodowego
class RodzajMaterialuDowodowego(Base):
    __tablename__ = 'type_of_evidence'

    ID_rodzajuMaterialuDowodowego = Column(Integer, primary_key=True, autoincrement=True)
    nazwa = Column(NVARCHAR(15), nullable=False)

    materialy = relationship("MaterialDowodowy", back_populates="rodzaj")


class MaterialDowodowy(Base):
    __tablename__ = 'evidence'

    ID_materialuDowodowego = Column(Integer, primary_key=True, autoincrement=True)
    dataZebrania = Column(Date, nullable=False)
    miejsceZebrania = Column(NVARCHAR(50), nullable=False)
    raport = Column(NVARCHAR(600), nullable=False)
    ID_rodzajuMaterialuDowodowego = Column(Integer, ForeignKey('type_of_evidence.ID_rodzajuMaterialuDowodowego'), nullable=False)
    # foreign keys
    ID_czynnosci = Column(Integer, ForeignKey('operations.ID_czynnosci'), primary_key=False)

    # relacja
    rodzaj = relationship("RodzajMaterialuDowodowego", back_populates="materialy")


class Czynnosc(Base):
    __tablename__ = 'operations'

    ID_czynnosci = Column(Integer, primary_key=True, autoincrement=True)
    dataWykonania = Column(Date, nullable=False)
    dataZakonczenia = Column(Date, nullable=False)
    numerOdznaki = Column(Integer, nullable=False)
    # foreign keys
    ID_analizyZgloszenia = Column(Integer, ForeignKey('analysis_of_reports.ID_analizyZgloszenia'), primary_key=False)
    numerSledztwa = Column(Integer, ForeignKey('investigations.numerSledztwa'), primary_key=False)

    # A polymorphic identity that identifies this class in the inheritance chain
    __mapper_args__ = {
        'polymorphic_identity': 'operation',
        'polymorphic_on': 'ID_czynnosci'
    }

class LokalizacjaPrzesluchania(Base):
    __tablename__ = 'hearing_location'

    ID_lokalizacjiPrzesluchania = Column(Integer, primary_key=True, autoincrement=True)
    nazwa = Column(NVARCHAR(100), nullable=False)

    przesluchania = relationship("Przesluchanie", back_populates="lokalizacja")

class CelPrzesluchania(Base):
    __tablename__ = 'interrogation_purpose'

    ID_celu = Column(Integer, primary_key=True, autoincrement=True)
    nazwa = Column(NVARCHAR(10), nullable=False)

    przesluchania = relationship("Przesluchanie", back_populates="cel")

class Przesluchanie(Czynnosc):
    __tablename__ = 'interrogations'

    ID_przesluchania = Column(Integer, ForeignKey('operations.ID_czynnosci'), primary_key=True)  # Inherits ID from Czynnosc
    godzina = Column(DateTime, nullable=False)
    ID_lokalizacji = Column(Integer, ForeignKey('hearing_location.ID_lokalizacjiPrzesluchania'), nullable=False)
    ID_celu = Column(Integer, ForeignKey('interrogation_purpose.ID_celu'), nullable=False)
    ID_osoby = Column(Integer, nullable=False)

    lokalizacja = relationship("LokalizacjaPrzesluchania", back_populates="przesluchania")
    cel = relationship("CelPrzesluchania", back_populates="przesluchania")

    czynnosc = relationship("Czynnosc", backref="interrogations")

    # Polymorphic identity for this subclass
    __mapper_args__ = {
        'polymorphic_identity': 'interrogation'
    }


# enum dla priorytetów
class Priorytet(Base):
    __tablename__ = 'priority'

    ID_priorytetu = Column(Integer, primary_key=True, autoincrement=True)
    nazwa = Column(NVARCHAR(10), nullable=False)
    weryfikacje = relationship("WeryfikacjaInformacji", back_populates="priorytet")

# enum dla wyników weryfikacji informacji
class WynikWeryfikacji(Base):
    __tablename__ = 'verification_outcome'

    ID_wynikuWeryfikacji = Column(Integer, primary_key=True, autoincrement=True)
    nazwa = Column(NVARCHAR(10), nullable=False)
    weryfikacje = relationship("WeryfikacjaInformacji", back_populates="wynik")

class RodzajWeryfikacjiInformacji(Base):
    __tablename__ = 'verification_type'

    ID_rodzajuWeryfikacji = Column(Integer, primary_key=True, autoincrement=True)
    nazwa = Column(NVARCHAR(200), nullable=False)

    weryfikacje = relationship("WeryfikacjaInformacji", back_populates="rodzaj")


class WeryfikacjaInformacji(Czynnosc):
    __tablename__ = 'information_verifications'
    #dziedziczy klucz glowny po Czynnosc

    ID_weryfikacjiInformacji = Column(Integer, ForeignKey('operations.ID_czynnosci'), primary_key=True)
    ID_priorytetu = Column(Integer, ForeignKey('priority.ID_priorytetu'), nullable=False)
    opis = Column(NVARCHAR(200), nullable=False)
    ID_wynikuWeryfikacji = Column(Integer, ForeignKey('verification_outcome.ID_wynikuWeryfikacji'), nullable=False)
    ID_rodzajuWeryfikacji = Column(Integer, ForeignKey('verification_type.ID_rodzajuWeryfikacji'), nullable=False)

    priorytet = relationship("Priorytet", back_populates="weryfikacje")
    wynik = relationship("WynikWeryfikacji", back_populates="weryfikacje")
    rodzaj = relationship("RodzajWeryfikacjiInformacji", back_populates="weryfikacje")

    __mapper_args__ = {
        'polymorphic_identity': 'verification'
    }
   

class OgledzinyMiejscaZdarzenia(Czynnosc):
    __tablename__ = 'site_inspections'
    #dziedziczy klucz glowny po Czynnosc

    ID_ogledzinMiejscaZdarzenia = Column(Integer, ForeignKey('operations.ID_czynnosci'), primary_key=True)
    godzina = Column(DateTime, nullable=False)
    adres = Column(NVARCHAR(50), nullable=False)
    przebieg = Column(NVARCHAR(1500), nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'site_inspection'
    }

class ZwiazanyZ(Base):
    __tablename__ = 'connected_with'

    numerSledztwa = Column(Integer, ForeignKey('investigations.numerSledztwa'), primary_key=True)
    ID_materialuDowodowego = Column(Integer, ForeignKey('evidence.ID_materialuDowodowego'), primary_key=True)
   
    czynnosc = relationship("Czynnosc", backref="connected_material")
    dowod = relationship("MaterialDowodowy", backref="connected_with")


# class PrzeprowadzonaWRamachAnalizy(Base):
#     __tablename__ = 'carried_out_bc_of_analysis'

#     ID_analizyZgloszenia = Column(Integer, ForeignKey('analysis_of_reports.ID_analizyZgloszenia'), primary_key=True)
#     ID_czynnosci = Column(Integer, ForeignKey('operations.ID_czynnosci'), primary_key=False)
    
#     analiza = relationship("AnalizaZgloszenia", back_populates="czynnosci")
#     czynnosc = relationship("Czynnosc", backref="analysis_related")


# class PrzeprowadzonaWRamachSledztwa(Base):
#     __tablename__ = 'carried_out_bc_of_investigation'

#     numerSledztwa = Column(Integer, ForeignKey('investigations.numerSledztwa'), primary_key=True)
#     ID_czynnosci = Column(Integer, ForeignKey('operations.ID_czynnosci'), primary_key=False)

#     sledztwo = relationship("Sledztwo", backref="investigation_related")
#     czynnosc = relationship("Czynnosc", backref="investigation_conducted")


# class RozpoczeteNaPodstawie(Base):
#     __tablename__ = 'started_based_on'

#     numerSledztwa = Column(Integer, ForeignKey('investigations.numerSledztwa'), primary_key=True)
#     ID_analizyZgloszenia = Column(Integer, ForeignKey('analysis_of_reports.ID_analizyZgloszenia'), primary_key=False)

#     sledztwo = relationship("Sledztwo", backref="started_based_on")
#     analiza = relationship("AnalizaZgloszenia", backref="basis_for_investigation")


# class SledztwoDotyczy(Base):
#     __tablename__ = 'investigation_concerns'

#     numerSledztwa = Column(Integer, ForeignKey('investigations.numerSledztwa'), primary_key=True)
#     ID_zdarzenia = Column(Integer, ForeignKey('incidents.ID_zdarzenia'), primary_key=False)
    
#     zdarzenie = relationship("Zdarzenie", backref="related_investigations")
#     sledztwo = relationship("Sledztwo", backref="concerned_events")


# class ZabezpieczonyWTrakcie(Base):
#     __tablename__ = 'collected_while'

#     ID_czynnosci = Column(Integer, ForeignKey('operations.ID_czynnosci'), primary_key=True)
#     ID_materialuDowodowego = Column(Integer, ForeignKey('evidence.ID_materialuDowodowego'), primary_key=False)

#     czynnosc = relationship("Czynnosc", backref="secured_during")
#     dowod = relationship("MaterialDowodowy", backref="secured_in_action")