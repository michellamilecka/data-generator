from faker import Faker
import random
fake=Faker()
number_of_stations=30
#liczba to id posterunku 

#generownie imion i nazwisk dla komendandtow glownych posterunkow
chief_names=[]

for i in range(1,number_of_stations+1):
    chief_names.append((i, fake.name()))


def generate_possible_types_of_something(possible_types_of_something):
    types_of_zdarzenia_something = []

    for i, sth in enumerate(possible_types_of_something):
        types_of_zdarzenia_something.append({
            "id": i,
            "name": sth
        })
    
    return types_of_zdarzenia_something

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
        zgloszenia_tablica.append((zgloszenie_id,zgloszenie_sposob,zgloszenie_data,id_zdarzenia,id_osoby,id_posterunku,numer_odznaki,id_analizy))
    return zgloszenia_tablica


def generate_sledztwo_data(num_of_sledztwa):
    sledztwa_tablica=[]
    ##tu tez sie pozbylam doatkowej tabeli
    yes_analizy = [analiza for analiza in analiza_data if analiza[1] == "yes"]
    for i in range(sledztwa_tablica):
        numer_sledztwa=i
        id_analizy=random.randint(0, len(analiza_data)-1)
        #data_ropoczecia
        #data_zakoczenia
        status_sledztwa=random.choice(possible_status_of_sledztwo)
        numer_odznaki=random.randint(10000, 99999)
        sledztwa_tablica.append((numer_sledztwa,data_rozp,data_zako,status_sledztwa,id_analizy,numer_odznaki))
    return sledztwa_tablica

def generate_czynnosc_data(num_of_czynnosci):
    czynnosci_tablica = []
    for i in range(num_of_czynnosci):
        id_czynnosci = i
        # data = 
        numerOdznaki = random.randint(10000, 99999)
        czynnosci_tablica.append(id_czynnosci,data,numerOdznaki)
    return czynnosci_tablica

def generate_przesluchanie_data(num_przesluchanie,czynnosci_tablica):
    przesluchania_tablica=[]
    for i in range(przesluchania_tablica):
        #losowanie krotki i jej usuniecie z tablicy
        wylosowana_czynnosc = czynnosci_tablica.pop(random.randrange(len(czynnosci_tablica)))
        id_czynnosci= wylosowana_czynnosc[0]

        godzina_przesluchania=fake.time()
        lokalizacja_przesluchania=random.choice(possible_places_of_przesluchanie)
        cel_przeslchania=random.choice(possible_purpose_of_hearing)
        #id_osoby
        przesluchania_tablica.append(id_czynnosci, godzina_przesluchania,lokalizacja_przesluchania,cel_przeslchania)
    return przesluchania_tablica

def generate_weryfikacjaInformacji_data(num_of_weryfikacjaInformacji, czynnosci_tablica):
    weryfikacjaInformacji_tablica = []
    for i in range(num_of_weryfikacjaInformacji):
        #losowanie krotki i jej usuniecie z tablicy
        wylosowana_czynnosc = czynnosci_tablica.pop(random.randrange(len(czynnosci_tablica)))
        id_weryfikacjiInformacji = wylosowana_czynnosc[0]
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
        #losowanie krotki i jej usuniecie z tablicy
        wylosowana_czynnosc = czynnosci_tablica.pop(random.randrange(len(czynnosci_tablica)))
        id_ogledzinMiejscaZdarzenia = wylosowana_czynnosc[0]
        godzina = fake.time() # zastanowic sie czy nie dodac ze musi byc pozniej niz godzina zdarzenia i 
        adres = fake.address() # zostawiac tak czy pobierac miejsce zdarzenia
        # przebieg = opisowka...
        ogledzinyMiejscaZdarzenia_tablica.append(id_ogledzinMiejscaZdarzenia, godzina, adres, przebieg)
    return ogledzinyMiejscaZdarzenia_tablica

# funckcja pomocna w trakcie tworzenia materialow dowodowych zeby szybciej znalezc o ktorej czynnosci mowa, zeby moc przypisac jej dateZebrania
def znajdz_czynnosc_po_id(czynnosci_tablica, szukane_id):
    for czynnosc in czynnosci_tablica:
        if czynnosc[0] == szukane_id:
            return czynnosc
    return None


# najpierw przypisujemy KAZDEMU przesluchaniu dowod z rodzajem "zeznanie",a pozniej dla pozostalej liczby dowodow przypisujemy do ogledzin
def generate_materialDowodowy_data(num_of_materialDowodowy, przesluchania, ogledzinyMiejscaZdarzenia, czynnosci_tablica):
    materialDowodowy_tablica = []
    total_num_of_przesluchania = len(przesluchania)
    # zastanawia mnie jak tu bedzie pozniej wiadomo dla ktorego sledztwa jakie sa materialy dowodowe bo to jest w tej osobnej tablicy w bazie danych
    
    for i, przesluchanie in enumerate(przesluchania):
        ID_materialuDowodowego = i
        ID_czynnosci = przesluchanie[0]

        #szukamy ktorej czynnosci odpowiada dane przesluchanie
        czynnosc = znajdz_czynnosc_po_id(czynnosci_tablica,ID_czynnosci)

        if czynnosc:
            dataZebrania = czynnosc[1]
        else:
            continue


        miejsceZebrania = przesluchanie[1]
        rodzaj = "zeznanie"
        # raport = ...
        materialDowodowy_tablica.append(ID_materialuDowodowego, dataZebrania, miejsceZebrania, raport, rodzaj, ID_czynnosci)
    
    pozostala_num_of_dowody = num_of_materialDowodowy - total_num_of_przesluchania
    
    
    
    #jesli nadal są dostępne dowody, przypisujemy je do oględzin do tego momentu az bedzie ich 0
    while pozostala_num_of_dowody > 0:
        ogledziny = random.choice(ogledzinyMiejscaZdarzenia)
        ID_materialuDowodowego = len(materialDowodowy_tablica)  #indeks nowego materiału dowodowego
        ID_czynnosci = ogledziny[0]

        #szukamy ktorej czynnosci odpowiadaja dane ogledziny
        czynnosc = znajdz_czynnosc_po_id(czynnosci_tablica,ID_czynnosci)

        if czynnosc:
            dataZebrania = czynnosc[1]
        else:
            continue

        miejsceZebrania = ogledziny[2]
        # uwzgledniamy ze mozliwosci dla ogledzin sa wszystkie z wyjatkiem zeznania
        rodzaj = random.choice([typ for typ in possible_type_od_material if typ != "zeznanie"])
        # raport = ...
        materialDowodowy_tablica.append(ID_materialuDowodowego, dataZebrania, miejsceZebrania, raport, rodzaj, ID_czynnosci)
        pozostala_num_of_dowody -= 1
    
    return materialDowodowy_tablica

def generate_zwiazany_z_data(sledztwa_dane,material_dowodowy_dane):
    zwiazany_z_tablica=[]
    for numer_sledztwa, _, _,_,_,_ in sledztwa_dane:
    # Randomly determine the number of metairly dowodowe dla danego sledztwa
        num_materialy = 0  # Initialize as 0 by default

        # Randomly select the number of metairly based on specified probabilities
        probability = random.random()
        if probability <= 0.5:
            num_materialy = 0  # 50% chance of no mateiraly
        elif probability <= 0.7:
            num_materialy = 1  # 20% chance of one mateiral
        elif probability <= 0.85:
            num_materialy = 2  # 15% chance of two materialy
        elif probability <= 0.95:
            num_materialy = 3  # 10% chance of three materialy
        elif probability <= 0.99:
            num_materialy = 4  # 5% chance of four materialy
        else:
            num_materialy = 5  # 1% chance of five materialy

        # Randomly select mateiraly
        materialy_dowodowe=  random.sample(material_dowodowy_dane, num_materialy)
        # Create records 
        for id_materialu, _, _, _, _, _ in materialy_dowodowe:
            zwiazany_z_tablica.append((numer_sledztwa, id_materialu))
    return zwiazany_z_tablica

#zostaw ta funkcje jesli faktycznie bedzie dodatkowa encja a jesli nie to odkomentuj w generate_materail linijke z id_czynnosci
def generate_zabezpieczony_w_trakcie_data(materialy_dane,czynnosci_dane):
    zabezpieczony_w_trakcie_tablica=[]
    #przypisujemy dla kazdego materialu czynnosc przy ktorej zostal zabeczpiecozny
    for i in range(len(materialy_dane)):
        id_czynnosci=random.randint(0, len(czynnosci_dane)-1)
        id_materialu=i
        zabezpieczony_w_trakcie_tablica.append((id_czynnosci,id_materialu))
    return zabezpieczony_w_trakcie_tablica

        
# generowanie mozliwych opcji dla "enumow"

typy_zdarzen = generate_possible_types_of_something(possible_types_of_zdarzenia)
sposoby_zgloszenia = generate_possible_types_of_something(possible_ways_of_zdarzenie)
miejsca_przesluchania = generate_possible_types_of_something(possible_places_of_przesluchanie)
powody_przesluchania = generate_possible_types_of_something(possible_purpose_of_hearing)
statusy_sledztwa = generate_possible_types_of_something(possible_status_of_sledztwo)
typy_materialow_dowodowych = generate_possible_types_of_something(possible_type_od_material)
typy_priorytetow = generate_possible_types_of_something(possible_priorities)
wyniki_weryfikacji = generate_possible_types_of_something(possible_outcome_of_verification)
sposoby_weryfikacji = generate_possible_types_of_something(possible_way_of_verification)


zdarzenia=generate_zdarzenie_data_later(10)
analizy=generate_analiza_data(10)
zgloszenia=generate_zgloszenia_data(20,zdarzenia,analizy)
print(zgloszenia)

# liczba czynnosci musi byc podzielna przez 3 to po rowno rozdzielimy sobie te czynnosci po isa
# zalozmy ze liczba czynnosci to bedzie 40 002 (wiem, ze musi byc wiecej ale narazie tak zakladamy)
# 3 mozna zrobic jako zmienna
num_of_czynnosci = 40002
num_of_przesluchanie = num_of_czynnosci/3
num_of_weryfikacjaInformacji = num_of_czynnosci/3
num_of_ogledzinyMiejscaZdarzenia = num_of_czynnosci/3

czynnosci = generate_czynnosc_data(num_of_czynnosci)
czynnosci_copy = czynnosci
przesluchania = generate_przesluchanie_data(num_of_przesluchanie,czynnosci_copy)
weryfikacjaInformacji = generate_weryfikacjaInformacji_data(num_of_weryfikacjaInformacji, czynnosci_copy)
ogledzinyMiejscaZdarzenia = generate_ogledzinyMiejscaZdarzenia_data(num_of_ogledzinyMiejscaZdarzenia, czynnosci_copy)
# at this point czynnosci_copy powinna byc pusta
# teraz jak sie losuje material dowodowy to tylko dla przesluchania i ogledzin miejsca zdarzenia, wiec damy obie te tablice do generowania materialu dowodowego