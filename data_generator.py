from faker import Faker
import random
fake=Faker()
number_of_stations=30
#liczba to id posterunku 

#generownie imion i nazwisk dla komendandtow glownych posterunkow
chief_names=[]

for i in range(1,number_of_stations+1):
    chief_names.append((i, fake.name()))

possible_types_of_zdarzenia = [
    "theft", 
    "kidnapping", 
    "disappearance", 
    "murder", 
    "assault", 
    "domestic violence", 
    "rape", 
    "threatening", 
    "burglary", 
    "fraud", 
    "money laundering", 
    "tax evasion", 
    "identity theft"
]

possible_ways_of_zdarzenie=["in person", "by phone"]

possible_places_of_przesluchanie=["police station", "the house of the interrogated person","area"]

possible_purpose_of_hearing=["determining the course of events", "confirming the words of another witness", "alibi"]

possible_status_of_sledztwo=["in progress","closed-unresolved","closed-resolved","open-resolved"]

possible_type_od_material=["testimony","biological","material","document"]

possible_priorities=["high","medium","low"]

possible_outcome_of_verification=["positive","negative","ambiguous"]

possible_way_of_verification=["identity confirmation","confirmation of the existence of the place indicated by reporting person"]


def generate_zdarzenie_data(num_of_zdarzenie):

    zdarzenia_tablica=[]
    for i in range(num_of_zdarzenie):
        start_date = '-30y'  
        end_date = '-10y'   
        data_zdarzenia = fake.date_between(start_date=start_date, end_date=end_date)
        rodzaj_zdarzenia=random.choice(possible_types_of_zdarzenia)
        godzina_zdarzenia=fake.time()
        adres_zdarzenia=fake.address()
        zdarzenia_id=i
        zdarzenia_tablica.append((data_zdarzenia,rodzaj_zdarzenia,godzina_zdarzenia,adres_zdarzenia,zdarzenia_id))
    return zdarzenia_tablica

def generate_zdarzenie_data_later(num_of_zdarzenie):
    zdarzenia_tablica=[]
    for i in range(num_of_zdarzenie):
        start_date = '-30y'  
        end_date = 'today'   
        data_zdarzenia = fake.date_between(start_date=start_date, end_date=end_date)
        rodzaj_zdarzenia=random.choice(possible_types_of_zdarzenia)
        godzina_zdarzenia=fake.time()
        adres_zdarzenia=fake.address()
        zdarzenia_id=i
        zdarzenia_tablica.append((data_zdarzenia,rodzaj_zdarzenia,godzina_zdarzenia,adres_zdarzenia,zdarzenia_id))
    return zdarzenia_tablica

def generate_analiza_data(num_of_analizy):
    analizy_tablica=[]
    for i in range(num_of_analizy):
        analiza_id=i
        analiza_rozpoczecie_sledztwa=random.choice(["yes", "no"])
        analizy_tablica.append((analiza_id,analiza_rozpoczecie_sledztwa))
    return analizy_tablica

def generate_zgloszenia_data(num_of_zgloszenia,zdarzenia_data,analizy_tablica):
    zgloszenia_tablica=[]
    for i in range(num_of_zgloszenia):
        id_zdarzenia=random.randint(0, len(zdarzenia_data)-1)
        zgloszenie_id=i
        zgloszenie_sposob=random.choice(possible_ways_of_zdarzenie)
        data_z=zdarzenia_data[id_zdarzenia][0]
        end_date = data_z.replace(year=data_z.year + 8)  
        zgloszenie_data = fake.date_between(start_date=data_z, end_date=end_date)
        #id_osoby
        #id_posterunku
        numer_odznaki=random.randint(10000, 99999)
        id_analizy=random.randint(0,len(analizy_tablica)-1)
        zgloszenia_tablica.append((zgloszenie_id,zgloszenie_sposob,zgloszenie_data,id_zdarzenia,id_analizy))
    return zgloszenia_tablica


def generate_sledztwo_data(num_of_sledztwa):
    sledztwa_tablica=[]
    for i in range(sledztwa_tablica):
        numer_sledztwa=i
        #data_ropoczecia
        #data_zakoczenia
        status_sledztwa=random.choice(possible_status_of_sledztwo)
        numer_odznaki=random.randint(10000, 99999)
        sledztwa_tablica.append((numer_sledztwa,status_sledztwa,numer_odznaki))
    return sledztwa_tablica

def generate_czynnosc_data(num_of_czynnosci):
    czynnosci_tablica = []
    for i in range(num_of_czynnosci):
        id_czynnosci = i
        #data = 
        numerOdznaki = random.randint(10000, 99999)
        czynnosci_tablica.append(id_czynnosci,numerOdznaki)
    return czynnosci_tablica

def generate_przesluchanie_data(num_przesluchanie,czynnosci_tablica):
    przesluchania_tablica=[]
    for i in range(przesluchania_tablica):
        #id_czynnosci
        godzina_przesluchania=fake.time()
        lokalizacja_przesluchania=random.choice(possible_places_of_przesluchanie)
        cel_przeslchania=random.choice(possible_purpose_of_hearing)
        #id_osoby
        przesluchania_tablica.append(godzina_przesluchania,lokalizacja_przesluchania,cel_przeslchania)
    return przesluchania_tablica

def generate_weryfikacjaInformacji_data(num_of_weryfikacjaInformacji, czynnosci_tablica):
    weryfikacjaInformacji_tablica = []
    for i in range(num_of_weryfikacjaInformacji):
        # id_weryfikacjiInformacji = tu trzeba bedzie wybierac liczbe czynnosci i potem rozdzielic to dobrze na pozostale encje wchodzace w sklad czynnosc
        # a pozniej bedziemy generowac np 1. przesluhcanie i tam bedziemy wyrzucac z tablicy juz te id ktore zostaly wykrozystane i przekazywac do weryfikacji informacji itd 
        priorytet = random.choice(possible_priorities)
        # opis ?????
        wynik = random.choice(possible_outcome_of_verification)
        rodzaj = random.choice(possible_way_of_verification)
        weryfikacjaInformacji_tablica.append(id_weryfikacjiInformacji, priorytet, opis, wynik, rodzaj)
    return weryfikacjaInformacji_tablica

def generate_ogledzinyMiejscaZdarzenia_data(num_of_ogledzinyMiejscaZdarzenia, czynnosci_tablica):
    ogledzinyMiejscaZdarzenia_tablica = []
    for i in range(num_of_ogledzinyMiejscaZdarzenia):
        # id_ogledzinMiejscaZdarzenia = uzaleznic od pozostalych czynnosci
        godzina = fake.time() # zastanowic sie czy nie dodac ze musi byc pozniej niz godzina zdarzenia i 
        adres = fake.address() # zostawiac tak czy pobierac miejsce zdarzenia
        # przebieg = opisowka...
        ogledzinyMiejscaZdarzenia_tablica.append(id_ogledzinMiejscaZdarzenia, godzina, adres, przebieg)
    return ogledzinyMiejscaZdarzenia_tablica

def generate_materialDowodowy_data(num_of_materialDowodowy, czynnosci_tablica):
    materialDowodowy_tablica = []
    # zastanawia mnie jak tu bedzie pozniej wiadomo dla ktorego sledztwa jakie sa materialy dowodowe bo to jest w tej osobnej tablicy w bazie danych
    for i in range(num_of_materialDowodowy):
        ID_materialuDowodowego = i
        # ID_czynnosci = ... i to sie przyda do append
        # dataZebrania = czynnosci_tablica I TU TRZEBA WYBRAC LOSOWO TE ID KTORE SA JAKO OGLEDZINY MIEJSCA ZDARZENIA LUB PRZESLUCHANIE
        # miejsceZebrania = czynnosci_tablica, w zaleznosci od id tej czynnosci pobierzemy tez adres czyli przesluchanie to atrybut nr 3, a dla ogledzin atrybut nr 3
        # raport = opisowka...
        rodzaj = random.choice(possible_type_od_material) #ale tu tez trzeba uwzglednic ze jak trafi sie przesluchanie to moze byc tylko opcja zeznanie
        materialDowodowy_tablica.append(ID_materialuDowodowego, dataZebrania, miejsceZebrania, raport, rodzaj, ID_czynnosci)


zdarzenia=generate_zdarzenie_data_later(10)
analizy=generate_analiza_data(10)
zgloszenia=generate_zgloszenia_data(20,zdarzenia,analizy)
print(zgloszenia)