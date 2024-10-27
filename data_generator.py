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

def generate_zdarzenie_data(num_of_zdarzenie, typy_zdarzen, sledztwa):
    zdarzenia_tablica=[]
    num_of_sledztwa = len(sledztwa)
    sledztwa_przypisane = set()


    for i in range(num_of_zdarzenie):
        start_date = '-30y'  
        end_date = '-10y'  
        ID_zdarzenia=i 
        data_zdarzenia = fake.date_between(start_date=start_date, end_date=end_date)
        ID_rodzajuZdarzenia=random.choice(typy_zdarzen)["id"] # nie mam pewnosci czy to tak zadziala
        opis_zdarzenia = fake.text() # opisowe, dodac do append
        godzina_zdarzenia=fake.time()
        adres_zdarzenia=fake.address()
        # foreign key

        if len(sledztwa_przypisane) < num_of_sledztwa:
            dostepne_sledztwa = [sl for sl in sledztwa if sl[0] not in sledztwa_przypisane]
            numer_sledztwa = random.choice(dostepne_sledztwa)[0]
            sledztwa_przypisane.add(numer_sledztwa)
        else:
            if random.random() < 0.65:  # 65% szans
                numer_sledztwa = random.choice(sledztwa)[0]  # wybierz losowe sledztwo
            else:
                numer_sledztwa = None  # brak przypisanego sledztwa
        

        zdarzenia_tablica.append((ID_zdarzenia, data_zdarzenia, ID_rodzajuZdarzenia, opis_zdarzenia, godzina_zdarzenia, adres_zdarzenia, numer_sledztwa))
    
    return zdarzenia_tablica


# def generate_zdarzenie_data_later(num_of_zdarzenie, typy_zdarzen):
#     zdarzenia_tablica=[]
#     for i in range(num_of_zdarzenie):
#         start_date = '-30y'  
#         end_date = 'today'
#         ID_zdarzenia=i
#         data_zdarzenia = fake.date_between(start_date=start_date, end_date=end_date)
#         ID_rodzajuZdarzenia=random.choice(typy_zdarzen)["id"]   
#         opis_zdarzenia = fake.text()
#         godzina_zdarzenia=fake.time()
#         adres_zdarzenia=fake.address()
#         # foreign keys
#         numer_sledztwa =
#         zdarzenia_tablica.append((ID_zdarzenia, data_zdarzenia, ID_rodzajuZdarzenia, opis_zdarzenia, godzina_zdarzenia, adres_zdarzenia, numer_sledztwa))
#     return zdarzenia_tablica

def generate_analiza_data(num_of_analizy, sledztwa):
    analizy_tablica=[]
    num_of_sledztwa = len(sledztwa)
    min_true = num_of_sledztwa
    max_true = min(num_of_analizy, int(num_of_sledztwa*1.5))
    num_of_true = random.randint(min_true, max_true)

    # Losujemy unikalne indeksy dla analiz, które będą miały wartość True
    true_indices = random.sample(range(num_of_analizy), num_of_true)

    # Użyte śledztwa
    used_sledztwa = set()


    for i in range(num_of_analizy):
        analiza_id=i
        rozpoczecieSledztwa_value = analiza_id in true_indices

        podstawy = fake.text() if rozpoczecieSledztwa_value == True else "BRAK"

        # foreign keys
        if rozpoczecieSledztwa_value:
            # Przypisujemy najpierw dostępne śledztwa, które nie zostały jeszcze użyte
            available_sledztwa = [sledztwo for sledztwo in sledztwa if sledztwo[0] not in used_sledztwa]
            if available_sledztwa: # czy lista zawiera jakiekolwiek elementy
                numer_sledztwa = random.choice(available_sledztwa)[0]  # Wybieramy jedno dostępne
                used_sledztwa.add(numer_sledztwa)  # Dodajemy do użytych
            else:
                numer_sledztwa = random.choice(sledztwa)[0]  # Jeśli nie ma już dostępnych, wybieramy losowo
        else:
            numer_sledztwa = None  # Brak przypisania do sledztwa
        
        analizy_tablica.append((analiza_id,rozpoczecieSledztwa_value,podstawy, numer_sledztwa))
        
    return analizy_tablica

#tu ponizej jest wersja chata
################################################################################
# def generate_zgloszenia_data(num_of_zgloszenia, zdarzenia_data, analizy_tablica, sposoby_zgloszenia):
#     zgloszenia_tablica = []
#     used_zdarzenia = set()  # Zestaw do śledzenia, które zdarzenia już były użyte
#     used_analizy = set()    # Zestaw do śledzenia, które analizy zostały użyte
#     zdarzenia_count = len(zdarzenia_data)
#     analizy_count = len(analizy_tablica)

#     for i in range(num_of_zgloszenia):
#         numer_zgloszenia = i
#         ID_sposobuZgloszenia = random.choice(sposoby_zgloszenia)["id"]

#         # Przypisywanie zdarzenia (każde zdarzenie musi być użyte co najmniej raz)
#         if len(used_zdarzenia) < zdarzenia_count:
#             id_zdarzenia = random.choice([z for z in zdarzenia_data if z[0] not in used_zdarzenia])[0]
#             used_zdarzenia.add(id_zdarzenia)  # Dodajemy do użytych zdarzeń
#         else:
#             id_zdarzenia = random.choice(zdarzenia_data)[0]  # Losowo przypisujemy zdarzenia

#         data_z = zdarzenia_data[id_zdarzenia][1]  # Data zdarzenia
#         end_date = data_z.replace(year=data_z.year + 8)
#         zgloszenie_data = fake.date_between(start_date=data_z, end_date=end_date)
#         opis = fake.text()
#         id_posterunku = random.randint(10000, 99999)
#         id_osoby = random.randint(10000, 99999)
#         numer_odznaki = random.randint(10000, 99999)

#         # Sprawdzamy, czy zdarzenie ma przypisane śledztwo
#         numer_sledztwa = zdarzenia_data[id_zdarzenia][6]

#         if numer_sledztwa:  # Zdarzenie ma przypisane śledztwo
#             # Szukamy analizy z TRUE i przypisanym numerem śledztwa
#             available_analizy = [a for a in analizy_tablica if a[1] == True and a[3] == numer_sledztwa and a[0] not in used_analizy]

#             if available_analizy:  # Jeśli są dostępne analizy do tego śledztwa
#                 id_analizy = random.choice(available_analizy)[0]
#                 used_analizy.add(id_analizy)
#             else:
#                 id_analizy = None  # Brak przypisania do analizy
#         else:  # Zdarzenie bez śledztwa
#             # Szukamy analizy z FALSE
#             available_analizy_false = [a for a in analizy_tablica if a[1] == False and a[0] not in used_analizy]

#             if available_analizy_false:
#                 id_analizy = random.choice(available_analizy_false)[0]
#                 used_analizy.add(id_analizy)
#             else:
#                 id_analizy = None  # Brak przypisania do analizy

#         zgloszenia_tablica.append((numer_zgloszenia, ID_sposobuZgloszenia, zgloszenie_data, opis,
#                                    id_posterunku, id_osoby, numer_odznaki, id_zdarzenia, id_analizy))

#     return zgloszenia_tablica

def generate_zgloszenia_data(num_of_zgloszenia, zdarzenia_data, analizy_tablica, sposoby_zgloszenia):
    zgloszenia_tablica=[]

    for i in range(num_of_zgloszenia):
        numer_zgloszenia=i
        ID_sposobuZgloszenia = random.choice(sposoby_zgloszenia)["id"]
        data_z=zdarzenia_data[id_zdarzenia][0]
        end_date = data_z.replace(year=data_z.year + 8)  
        zgloszenie_data = fake.date_between(start_date=data_z, end_date=end_date)
        opis = fake.text()
        id_posterunku =random.randint(10000, 99999)
        id_osoby =random.randint(10000, 99999)
        numer_odznaki=random.randint(10000, 99999)
        # foreign keys
        id_zdarzenia = 
            
        id_analizy =

        zgloszenia_tablica.append((numer_zgloszenia,ID_sposobuZgloszenia,zgloszenie_data,opis,id_posterunku,id_osoby,numer_odznaki,id_zdarzenia, id_analizy))
    
    return zgloszenia_tablica


def generate_sledztwo_data(num_of_sledztwa, statusy_sledztwa):
    sledztwa_tablica=[]
    ##tu tez sie pozbylam doatkowej tabeli
    #yes_analizy = [analiza for analiza in analiza_data if analiza[1] == "yes"]

    for i in range(num_of_sledztwa):
        numer_sledztwa=i
        data_ropoczecia = fake.date()
        data_zakoczenia = fake.date()
        ID_statusuSledztwa = random.choice(statusy_sledztwa)["id"]
        numer_odznaki=random.randint(10000, 99999)
        
        sledztwa_tablica.append((numer_sledztwa,data_ropoczecia,data_zakoczenia,ID_statusuSledztwa,numer_odznaki))
    
    return sledztwa_tablica

# def generate_czynnosc_data(num_of_czynnosci):
#     czynnosci_tablica = []

#     for i in range(num_of_czynnosci):
#         id_czynnosci = i
#         # c = 
#         numerOdznaki = random.randint(10000, 99999)
#         #foreign keys
#         ID_analizyZgloszenia = 
#         numer_sledztwa= 
#         czynnosci_tablica.append(id_czynnosci,ID_analizyZgloszenia,numerOdznaki,ID_analizyZgloszenia, numer_sledztwa)
#     return czynnosci_tablica

# def generate_przesluchanie_data(num_przesluchanie,czynnosci_tablica,powody_przesluchania):
#     przesluchania_tablica=[]

#     for i in range(przesluchania_tablica, miejsca_przesluchania):
#         #losowanie krotki i jej usuniecie z tablicy
#         wylosowana_czynnosc = czynnosci_tablica.pop(random.randrange(len(czynnosci_tablica)))
#         id_czynnosci= wylosowana_czynnosc[0]
#         godzina_przesluchania=fake.time()
#         ID_lokalizacjiPrzesluchania=random.choice(miejsca_przesluchania)["id"]
#         cel_przeslchania=random.choice(powody_przesluchania)["id"]
#         #id_osoby
#         przesluchania_tablica.append(id_czynnosci, godzina_przesluchania,ID_lokalizacjiPrzesluchania,cel_przeslchania,id_osoby)
    
#     return przesluchania_tablica

# def generate_weryfikacjaInformacji_data(num_of_weryfikacjaInformacji, czynnosci_tablica,typy_priorytetow,wyniki_weryfikacji):
#     weryfikacjaInformacji_tablica = []
#     for i in range(num_of_weryfikacjaInformacji):
#         #losowanie krotki i jej usuniecie z tablicy
#         wylosowana_czynnosc = czynnosci_tablica.pop(random.randrange(len(czynnosci_tablica)))
#         id_weryfikacjiInformacji = wylosowana_czynnosc[0]
#         # a pozniej bedziemy generowac np 1. przesluhcanie i tam bedziemy wyrzucac z tablicy juz te id ktore zostaly wykrozystane i przekazywac do weryfikacji informacji itd 
#         ID_priorytetu = random.choice(typy_priorytetow)["id"]
#         opis = fake.text()
#         ID_wynikuWeryfikacji = random.choice(wyniki_weryfikacji)["id"]
#         ID_rodzajuWeryfikacji = random.choice(sposoby_weryfikacji)["id"]
#         weryfikacjaInformacji_tablica.append(id_weryfikacjiInformacji, ID_priorytetu, opis, ID_wynikuWeryfikacji, ID_rodzajuWeryfikacji)

#     return weryfikacjaInformacji_tablica

# def generate_ogledzinyMiejscaZdarzenia_data(num_of_ogledzinyMiejscaZdarzenia, czynnosci_tablica):
#     ogledzinyMiejscaZdarzenia_tablica = []

#     for i in range(num_of_ogledzinyMiejscaZdarzenia):
#         #losowanie krotki i jej usuniecie z tablicy
#         wylosowana_czynnosc = czynnosci_tablica.pop(random.randrange(len(czynnosci_tablica)))
#         id_ogledzinMiejscaZdarzenia = wylosowana_czynnosc[0]
#         godzina = fake.time() # zastanowic sie czy nie dodac ze musi byc pozniej niz godzina zdarzenia i 
#         adres = fake.address() # zostawiac tak czy pobierac miejsce zdarzenia
#         przebieg = fake.text()
#         ogledzinyMiejscaZdarzenia_tablica.append(id_ogledzinMiejscaZdarzenia, godzina, adres, przebieg)
    
#     return ogledzinyMiejscaZdarzenia_tablica

# # funckcja pomocna w trakcie tworzenia materialow dowodowych zeby szybciej znalezc o ktorej czynnosci mowa, zeby moc przypisac jej dateZebrania
# def znajdz_czynnosc_po_id(czynnosci_tablica, szukane_id):
#     for czynnosc in czynnosci_tablica:
#         if czynnosc[0] == szukane_id:
#             return czynnosc
#     return None


# # najpierw przypisujemy KAZDEMU przesluchaniu dowod z rodzajem "zeznanie",a pozniej dla pozostalej liczby dowodow przypisujemy do ogledzin
# def generate_materialDowodowy_data(num_of_materialDowodowy, przesluchania, ogledzinyMiejscaZdarzenia, czynnosci_tablica, typy_materialow_dowodowych):
#     materialDowodowy_tablica = []
#     total_num_of_przesluchania = len(przesluchania)
#     # zastanawia mnie jak tu bedzie pozniej wiadomo dla ktorego sledztwa jakie sa materialy dowodowe bo to jest w tej osobnej tablicy w bazie danych
    
#     for i, przesluchanie in enumerate(przesluchania):
#         ID_materialuDowodowego = i
#         ID_czynnosci = przesluchanie[0]

#         #szukamy ktorej czynnosci odpowiada dane przesluchanie
#         czynnosc = znajdz_czynnosc_po_id(czynnosci_tablica,ID_czynnosci)

#         if czynnosc:
#             dataZebrania = czynnosc[1]
#         else:
#             continue


#         miejsceZebrania = przesluchanie[1]
#         # dla zeznania ID jest zawsze 0 (jest jako pierwsze)
#         rodzaj = "zeznanie"
#         ID_rodzajuMaterialuDowodowego = 0
#         raport = fake.text()
#         materialDowodowy_tablica.append(ID_materialuDowodowego, dataZebrania, miejsceZebrania, raport, ID_rodzajuMaterialuDowodowego, ID_czynnosci)
    
#     pozostala_num_of_dowody = num_of_materialDowodowy - total_num_of_przesluchania
    
#     #jesli nadal są dostępne dowody, przypisujemy je do oględzin do tego momentu az bedzie ich 0
#     while pozostala_num_of_dowody > 0:
#         ogledziny = random.choice(ogledzinyMiejscaZdarzenia)
#         ID_materialuDowodowego = len(materialDowodowy_tablica)  #indeks nowego materiału dowodowego
#         ID_czynnosci = ogledziny[0]

#         #szukamy ktorej czynnosci odpowiadaja dane ogledziny
#         czynnosc = znajdz_czynnosc_po_id(czynnosci_tablica,ID_czynnosci)

#         if czynnosc:
#             dataZebrania = czynnosc[1]
#         else:
#             continue

#         miejsceZebrania = ogledziny[2]
#         # uwzgledniamy ze mozliwosci dla ogledzin sa wszystkie z wyjatkiem zeznania
#         ID_rodzajuMaterialuDowodowego = random.choice([typ for typ in typy_materialow_dowodowych if typ["name"] != "zeznanie"])["id"]
#         raport = fake.text()

#         materialDowodowy_tablica.append(ID_materialuDowodowego, dataZebrania, miejsceZebrania, raport, ID_rodzajuMaterialuDowodowego, ID_czynnosci)
#         pozostala_num_of_dowody -= 1
    
#     return materialDowodowy_tablica

# def generate_zwiazany_z_data(sledztwa_dane,material_dowodowy_dane):
#     zwiazany_z_tablica=[]
#     for numer_sledztwa, _, _,_,_,_ in sledztwa_dane:
#     # Randomly determine the number of metairly dowodowe dla danego sledztwa
#         num_materialy = 0  # Initialize as 0 by default

#         # Randomly select the number of metairly based on specified probabilities
#         probability = random.random()
#         if probability <= 0.5:
#             num_materialy = 0  # 50% chance of no mateiraly
#         elif probability <= 0.7:
#             num_materialy = 1  # 20% chance of one mateiral
#         elif probability <= 0.85:
#             num_materialy = 2  # 15% chance of two materialy
#         elif probability <= 0.95:
#             num_materialy = 3  # 10% chance of three materialy
#         elif probability <= 0.99:
#             num_materialy = 4  # 5% chance of four materialy
#         else:
#             num_materialy = 5  # 1% chance of five materialy

#         # Randomly select mateiraly
#         materialy_dowodowe=  random.sample(material_dowodowy_dane, num_materialy)
#         # Create records 
#         for id_materialu, _, _, _, _, _ in materialy_dowodowe:
#             zwiazany_z_tablica.append((numer_sledztwa, id_materialu))
#     return zwiazany_z_tablica

#zostaw ta funkcje jesli faktycznie bedzie dodatkowa encja a jesli nie to odkomentuj w generate_materail linijke z id_czynnosci
# def generate_zabezpieczony_w_trakcie_data(materialy_dane,czynnosci_dane):
#     zabezpieczony_w_trakcie_tablica=[]
#     #przypisujemy dla kazdego materialu czynnosc przy ktorej zostal zabeczpiecozny
#     for i in range(len(materialy_dane)):
#         id_czynnosci=random.randint(0, len(czynnosci_dane)-1)
#         id_materialu=i
#         zabezpieczony_w_trakcie_tablica.append((id_czynnosci,id_materialu))
#     return zabezpieczony_w_trakcie_tablica

        
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


# generowanie danych
# 1. zdarzen musi byc > niz sledztw
# 2. analiz musi byc > niz sledztw & musi byc tyle samo lub < co zgłoszeń

sledztwa = generate_sledztwo_data(10, statusy_sledztwa)
zdarzenia = generate_zdarzenie_data(20, typy_zdarzen, sledztwa)
analizy_zgloszen = generate_analiza_data(50, sledztwa)


# Wypisanie zdarzeń i ich ID śledztw
# print("ID Zdarzenia i numer śledztwa:")
# for zdarzenie in zdarzenia:
#     id_zdarzenia = zdarzenie[0]  # Pobieranie ID zdarzenia
#     id_sledztwa = zdarzenie[-1]  # Pobieranie numeru śledztwa z ostatniego elementu
#     print(f"ID Zdarzenia: {id_zdarzenia}, Numer Śledztwa: {id_sledztwa}")


# Wypisanie analiz z informacjami o ich statusie i przypisanym śledztwie
print("Analizy i ich statusy:")
for analiza in analizy_zgloszen:
    analiza_id, rozpoczecie_sledztwa, podstawy, numer_sledztwa = analiza
    status = "TAK" if rozpoczecie_sledztwa else "NIE"
    if numer_sledztwa is not None:
        print(f"ID Analizy: {analiza_id}, Status Rozpoczęcia Śledztwa: {status}, Numer Śledztwa: {numer_sledztwa}")
    else:
        print(f"ID Analizy: {analiza_id}, Status Rozpoczęcia Śledztwa: {status}, Numer Śledztwa: Brak przypisania")


















# zdarzenia=generate_zdarzenie_data_later(10)
# analizy=generate_analiza_data(10)
# zgloszenia=generate_zgloszenia_data(20,zdarzenia,analizy)
# print(zgloszenia)

# liczba czynnosci musi byc podzielna przez 3 to po rowno rozdzielimy sobie te czynnosci po isa
# zalozmy ze liczba czynnosci to bedzie 40 002 (wiem, ze musi byc wiecej ale narazie tak zakladamy)
# 3 mozna zrobic jako zmienna
# num_of_czynnosci = 40002
# num_of_przesluchanie = num_of_czynnosci/3
# num_of_weryfikacjaInformacji = num_of_czynnosci/3
# num_of_ogledzinyMiejscaZdarzenia = num_of_czynnosci/3

# czynnosci = generate_czynnosc_data(num_of_czynnosci)
# czynnosci_copy = czynnosci
# przesluchania = generate_przesluchanie_data(num_of_przesluchanie,czynnosci_copy)
# weryfikacjaInformacji = generate_weryfikacjaInformacji_data(num_of_weryfikacjaInformacji, czynnosci_copy)
# ogledzinyMiejscaZdarzenia = generate_ogledzinyMiejscaZdarzenia_data(num_of_ogledzinyMiejscaZdarzenia, czynnosci_copy)
# at this point czynnosci_copy powinna byc pusta
# teraz jak sie losuje material dowodowy to tylko dla przesluchania i ogledzin miejsca zdarzenia, wiec damy obie te tablice do generowania materialu dowodowego