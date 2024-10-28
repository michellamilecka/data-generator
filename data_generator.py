from faker import Faker
import random
import pandas as pd
import csv
from datetime import timedelta, datetime

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

def save_to_csv(data, filename="output.csv"):
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data)
    # Save the DataFrame to a CSV file
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
possible_types_of_podstawy = [
    "Decyzję podjęto na podstawie zeznań świadków którzy widzieli podejrzanego na miejscu zdarzenia.",
    "Wstępna weryfikacja alibi podejrzanego nie potwierdziła jego wersji wydarzeń.",
    "Zgłoszenie od anonimowego informatora wskazało na powiązania podejrzanego z przestępstwem.",
    "Wyniki przesłuchania zatrzymanego wskazały na konieczność dalszego postępowania.",
    "Potwierdzono tożsamość sprawcy po analizie nagrań z monitoringu.",
    "Na podstawie sprzecznych zeznań świadków podjęto decyzję o dalszych działaniach.",
    "Zeznania ofiary wykazały kluczowe nieścisłości wymagające dalszego dochodzenia.",
    "Wstępne sprawdzenie dowodów rzeczowych potwierdziło zasadność rozpoczęcia śledztwa.",
    "Analiza zgłoszeń z okolicy wskazała na możliwy związek podejrzanego z innymi przestępstwami.",
    "Informacje uzyskane w wyniku przesłuchania świadków potwierdziły potrzebę działań operacyjnych.",
    "BRAK"
    ]

possible_types_of_opis_zgloszenia = [
    "Zgłoszenie dotyczące głośnych hałasów dobiegających z mieszkania.",
    "Zgłoszenie o kradzieży samochodu z parkingu przy centrum handlowym.",
    "Mieszkaniec zgłosił podejrzane zachowanie grupy osób na osiedlu.",
    "Telefoniczne zgłoszenie awantury domowej w budynku wielorodzinnym.",
    "Zgłoszenie podejrzanego dymu wydobywającego się z opuszczonego magazynu.",
    "Zgłoszenie o podejrzanej osobie krążącej w pobliżu placu zabaw.",
    "Pracownik banku zgłosił podejrzenie sfałszowania dokumentów kredytowych.",
    "Mężczyzna zgłosił zaginięcie swojego psa w okolicach parku miejskiego.",
    "Zgłoszenie od kierowcy który zauważył stłuczkę drogową i uciekającego sprawcę.",
    "Sąsiad zgłosił nielegalne składowanie odpadów w pobliżu osiedla mieszkaniowego.",
    "Telefoniczne zgłoszenie anonimowego świadka o dziwnych odgłosach z piwnicy w budynku mieszkalnym."
]

possible_types_of_opis_zdarzenia = [
    "Świadkowie widzieli jak podejrzany uciekł z miejsca zdarzenia pozostawiając narzędzia włamania.",
    "Na miejscu zdarzenia znaleziono ślady krwi oraz rozbite szyby w oknach.",
    "Na parkingu centrum handlowego doszło do uszkodzenia kilku pojazdów w wyniku kolizji.",
    "Miejsce zdarzenia zostało zabezpieczone po stwierdzeniu obecności substancji niebezpiecznych.",
    "Odnaleziono porzucony bagaż na dworcu który wzbudził podejrzenia.",
    "Podejrzany próbował uciec z miejsca zdarzenia jednak został zatrzymany przez funkcjonariuszy policji.",
    "Na miejscu zdarzenia znaleziono ślady włamania i zniszczone zamki w drzwiach.",
    "Świadek opisał zdarzenie jako gwałtowną kłótnię która przerodziła się w bójkę.",
    "Na terenie parku miejskiego odnaleziono porzucony rower który wcześniej zgłoszono jako skradziony.",
    "Zdarzenie miało miejsce na przejściu dla pieszych gdzie samochód potrącił pieszego.",
    "Policja przyjechała na miejsce zdarzenia po zgłoszeniu o podejrzeniu handlu narkotykami."
]

possible_types_of_raport = [
    "Zabezpieczono odcisk buta który przekazano do analizy.",
    "Telefon komórkowy znaleziony na miejscu zdarzenia został przekazany do badania.",
    "Zabezpieczono nóż z widocznymi śladami krwi do analizy DNA.",
    "W pojeździe sprawcy znaleziono torbę ze sfałszowanymi dokumentami.",
    "Odnaleziono włos który przekazano do analizy genetycznej.",
    "Zabezpieczono kanister z substancją łatwopalną do badań chemicznych.",
    "Plik dokumentów księgowych znaleziono i przekazano biegłym do analizy.",
    "Rękawiczki ze śladami chemikaliów zabezpieczono do analizy odcisków palców.",
    "Na miejscu znaleziono zapalniczkę z inicjałami podejrzanego.",
    "Paczkę papierosów z odciskami palców zabezpieczono do dalszej analizy."
    ]

possible_types_of_przebieg_ogledzin = [
    "Na miejscu zdarzenia przeprowadzono dokładną analizę śladów pozostawionych przez podejrzanego.",
    "Zabezpieczono materiały dowodowe w tym odciski palców oraz ślady obuwia.",
    "Oględziny wykazały obecność śladów walki oraz uszkodzenia mebli w pomieszczeniu.",
    "Na miejscu zdarzenia odnaleziono porozrzucane dokumenty i ślady wskazujące na włamanie.",
    "Na parkingu odnaleziono uszkodzony samochód z którego wnętrza zniknęły cenne przedmioty.",
    "Oględziny potwierdziły że narzędzie zbrodni zostało ukryte w pobliskim lesie.",
    "Na miejscu zdarzenia odnaleziono świeże ślady opon które zabezpieczono do dalszej analizy.",
    "Przeprowadzono oględziny miejsca pożaru podczas których zabezpieczono resztki materiałów łatwopalnych.",
    "Dokładna analiza uszkodzeń drzwi wskazuje na użycie siły do wtargnięcia na teren posesji.",
    "Zabezpieczono liczne ślady biologiczne w mieszkaniu w tym krew oraz fragmenty włosów.",
    "Na miejscu zdarzenia znaleziono odciski butów które mogły należeć do sprawcy włamania."
]

possible_types_of_opis_werfikacji = [
    "Potwierdzono tożsamość podejrzanego na podstawie danych osobowych z bazy policyjnej.",
    "Zweryfikowano alibi podejrzanego poprzez analizę zapisów z kamer monitoringu.",
    "Dane z telefonu komórkowego podejrzanego wskazały jego obecność w miejscu zdarzenia.",
    "Informacje przekazane przez świadka zostały potwierdzone przez innych świadków.",
    "Sprawdzono autentyczność dokumentów dostarczonych przez podejrzanego.",
    "Zweryfikowano połączenia telefoniczne podejrzanego w czasie zdarzenia.",
    "Przeanalizowano historię bankową podejrzanego potwierdzając podejrzane transakcje.",
    "Weryfikacja adresu zameldowania wykazała niezgodność z danymi w systemie.",
    "Informacje uzyskane od informatora zostały potwierdzone przez dodatkowe dowody.",
    "Potwierdzono obecność podejrzanego w okolicy na podstawie lokalizacji GPS."
]
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

def generate_zdarzenie_data(num_of_zdarzenie, typy_zdarzen, sledztwa, T1orT2, opisy_zdarzen):
    zdarzenia_tablica=[]
    num_of_sledztwa = len(sledztwa)
    sledztwa_przypisane = set()

    for i in range(num_of_zdarzenie):
        if T1orT2 == "T1":
            start_date = datetime.now() - timedelta(days=365*5) # 5 lat temu  
            end_date = datetime.now() - timedelta(days=365*2) # 2 lata temu
        else:
            start_date = datetime.now() - timedelta(days=365) # 1 rok temu  
            end_date = datetime.now() - timedelta(days=9*30) # 9 miesiecy temu
        ID_zdarzenia=i 
        data_zdarzenia = fake.date_between(start_date=start_date, end_date=end_date)
        ID_rodzajuZdarzenia=random.choice(typy_zdarzen)["id"] # nie mam pewnosci czy to tak zadziala
        opis_zdarzenia = random.choice(opisy_zdarzen)["id"]
        godzina_zdarzenia=fake.time()
        adres_zdarzenia=fake.street_name()
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

def generate_analiza_data(num_of_analizy, sledztwa, podstawy_analizy):
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

        if rozpoczecieSledztwa_value == True:
        # Losujemy wartość z podstawy_analizy z wyłączeniem ostatniego elementu
            podstawy = random.choice(podstawy_analizy[:-1])["id"]
        else:
            # Przypisujemy ostatnią opcję w tablicy
            podstawy = podstawy_analizy[-1]["id"]

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


def generate_zgloszenia_data(num_of_zgloszenia, zdarzenia_data, analizy_tablica, sposoby_zgloszenia, opisy_zgloszen):
    zgloszenia_tablica = []
    used_zdarzenia = set()  # Zestaw do śledzenia, które zdarzenia już były użyte
    used_analizy = set()    # Zestaw do śledzenia, które analizy zostały użyte
    zdarzenia_count = len(zdarzenia_data)
    analizy_count = len(analizy_tablica)

    # Tworzymy mapę id_zdarzenia -> indeks w liście zdarzenia_data
    zdarzenia_map = {zdarzenie[0]: index for index, zdarzenie in enumerate(zdarzenia_data)}

    for i in range(num_of_zgloszenia):
        numer_zgloszenia = i
        ID_sposobuZgloszenia = random.choice(sposoby_zgloszenia)["id"]

        # Przypisywanie zdarzenia (każde zdarzenie musi być użyte co najmniej raz)
        if len(used_zdarzenia) < zdarzenia_count:
            id_zdarzenia = random.choice([z for z in zdarzenia_data if z[0] not in used_zdarzenia])[0]
            used_zdarzenia.add(id_zdarzenia)  # Dodajemy do użytych zdarzeń
        else:
            id_zdarzenia = random.choice(zdarzenia_data)[0]  # Losowo przypisujemy zdarzenia

        # Pobieramy odpowiednie dane zdarzenia za pomocą mapy
        zdarzenie_index = zdarzenia_map[id_zdarzenia]
        data_z = zdarzenia_data[zdarzenie_index][1]  # Data zdarzenia
        end_date = data_z + timedelta(days=25)
        zgloszenie_data = fake.date_between(start_date=data_z, end_date=end_date)
        opis = random.choice(opisy_zgloszen)["id"]
        
        osoby = pd.read_excel(r"C:\Users\miche\Desktop\STUDIA\V SEM\HURTOWNIE DANYCH\people_data.xlsx")
        filtered_osoby = osoby[osoby["Typ osoby"] == "Osoba zgłaszająca"]
        id_osob_zglaszajaych = filtered_osoby.to_dict(orient='records')
        id_osoby_list = [record["ID osoby"] for record in id_osob_zglaszajaych]
        id_osoby = random.choice(id_osoby_list)

        numer_odznaki = random.randint(10000, 10099)
        policjanci=pd.read_excel(r"C:\Users\miche\Desktop\STUDIA\V SEM\HURTOWNIE DANYCH\police_data_time1.xlsx")
        filtered_policjanci = policjanci[policjanci["Numer odznaki"] == numer_odznaki]
        id_policjantow = filtered_policjanci.to_dict(orient='records')
        id_polcijanta_list= [record["Aktualny posterunek"] for record in id_policjantow]
        id_posterunku=id_polcijanta_list[0]

        # Sprawdzamy, czy zdarzenie ma przypisane śledztwo
        numer_sledztwa = zdarzenia_data[zdarzenie_index][6]

        if numer_sledztwa:  # Zdarzenie ma przypisane śledztwo
            # Szukamy analizy z TRUE i przypisanym numerem śledztwa
            available_analizy = [a for a in analizy_tablica if a[1] == True and a[3] == numer_sledztwa and a[0] not in used_analizy]

            if available_analizy:  # Jeśli są dostępne analizy do tego śledztwa
                id_analizy = random.choice(available_analizy)[0]
                used_analizy.add(id_analizy)
            else:
                id_analizy = None  # Brak przypisania do analizy
        else:  # Zdarzenie bez śledztwa
            # Szukamy analizy z FALSE
            available_analizy_false = [a for a in analizy_tablica if a[1] == False and a[0] not in used_analizy]

            if available_analizy_false:
                id_analizy = random.choice(available_analizy_false)[0]
                used_analizy.add(id_analizy)
            else:
                id_analizy = None  # Brak przypisania do analizy

        zgloszenia_tablica.append((numer_zgloszenia, ID_sposobuZgloszenia, zgloszenie_data, opis,
                                   id_posterunku, id_osoby, numer_odznaki, id_zdarzenia, id_analizy))

    return zgloszenia_tablica


def generate_sledztwo_data(num_of_sledztwa, statusy_sledztwa, T1orT2):
    sledztwa_tablica=[]
    if T1orT2 == "T1":
        start_date = datetime.now() - timedelta(days=365 +10*30) # okolo rok i 10 miesiecy
        end_date = start_date +timedelta(days=10)
    else:
        start_date = datetime.now() - timedelta(days=7*30 + 10) # okolo 7 msc i 10 dni
        end_date = start_date +timedelta(days=10) #okolo 7 msc

    
    ##tu tez sie pozbylam doatkowej tabeli
    #yes_analizy = [analiza for analiza in analiza_data if analiza[1] == "yes"]

    for i in range(num_of_sledztwa):
        numer_sledztwa=i
        data_rozpoczecia = fake.date_between(start_date=start_date, end_date=end_date)
        # Logika szans na datę zakończenia
        if random.random() <= 0.25:  # 25% szans
            if T1orT2 == "T1":
                data_zakonczenia = fake.date_between(start_date=data_rozpoczecia + timedelta(days=10), end_date=(datetime.now()-timedelta(days=365)))
            else:
                data_zakonczenia = fake.date_between(start_date=data_rozpoczecia + timedelta(days=10), end_date=(datetime.now()-timedelta(days=1)))

            dostepne_statusy = [status for status in statusy_sledztwa if status["id"] in [1, 2]]
        else:
            data_zakonczenia = None
            dostepne_statusy = [status for status in statusy_sledztwa if status["id"] in [0, 4]]

        # Wybieramy losowy status z dostępnych
        ID_statusuSledztwa = random.choice(dostepne_statusy)["id"]
        numer_odznaki=random.randint(10000, 10101)
        
        sledztwa_tablica.append((numer_sledztwa,data_rozpoczecia,data_zakonczenia,ID_statusuSledztwa,numer_odznaki))
    
    return sledztwa_tablica

def update_sledztwo(sledztwa_tablica):
    for idx, sledztwo in enumerate(sledztwa_tablica,):
        numer_sledztwa, data_ropoczecia, data_zakoczenia, status, numer_odznaki = sledztwo
        
        # Jeśli status to "w toku" i z prawdopodobieństwem 0.4
        if status == 0 and random.random()<0.15:
            # Zmieniamy status na "zamknięte" i dodajemy datę zakończenia
            status = 2
            one_year_ago = datetime.now() - timedelta(days=365)
            data_zakoczenia = fake.date_between(start_date=one_year_ago, end_date='today')  # Ustawienie aktualnej daty zakończenia

            # Aktualizujemy rekord w sledztwa_tablica
            sledztwa_tablica[idx] = (numer_sledztwa, data_ropoczecia, data_zakoczenia, status, numer_odznaki)
    

    
    return sledztwa_tablica

def generate_czynnosc_data(num_of_czynnosci, analizy_tablica, sledztwa, T1orT2):
    czynnosci_tablica = []
    num_of_analizy = len(analizy_tablica)
    num_of_sledztwa = len(sledztwa)
    sledztwa_przypisane = set()
    analizy_przypisane = set()

    for i in range(num_of_czynnosci):
        id_czynnosci = i
        numerOdznaki = random.randint(10000, 10101)
        #foreign keys
        if len(sledztwa_przypisane) < num_of_sledztwa:
            dostepne_sledztwa = [sl for sl in sledztwa if sl[0] not in sledztwa_przypisane]
            sledztwo = random.choice(dostepne_sledztwa)
            numer_sledztwa = sledztwo[0]
            ID_analizyZgloszenia = None
            sledztwa_przypisane.add(numer_sledztwa)

            data_rozpoczecia_sledztwa = sledztwo[1]
            data_zakonczenia_sledztwa = sledztwo[2]  # może być None

            start_date = data_rozpoczecia_sledztwa
            if data_zakonczenia_sledztwa:
                end_date = data_zakonczenia_sledztwa - timedelta(days=1)
            else:
                if T1orT2 == "T1":
                    end_date = datetime.now() - timedelta(days=365)  # Do roku wstecz
                else:
                    end_date = datetime.now() - timedelta(days=1)

        elif len(analizy_przypisane) < num_of_analizy:
            dostepne_analizy = [an_sl for an_sl in analizy_tablica if an_sl[0] not in analizy_przypisane]
            analiza = random.choice(dostepne_analizy)
            ID_analizyZgloszenia = analiza[0]
            numer_sledztwa = None
            analizy_przypisane.add(ID_analizyZgloszenia)

            numer_sledztwa_pobrany_analiza = analiza[3]

            # Ustalanie daty dla czynności związanej z analizą zgłoszenia
            if numer_sledztwa_pobrany_analiza is not None:
                # Analiza miała śledztwo
                data_rozpoczecia_sledztwa = [sl[1] for sl in sledztwa if sl[0] == numer_sledztwa_pobrany_analiza][0]
                end_date = data_rozpoczecia_sledztwa
                start_date = end_date - timedelta(days=20)
            else:
                if T1orT2=="T1":
                    # Analiza bez śledztwa, losuj daty rok i 11 miesięcy temu
                    end_date = datetime.now() - timedelta(days=365 + 10*30)  # Rok i 10 miesięcy temu
                    start_date = datetime.now() - timedelta(days=365 + 11*30)  # Rok i 11 miesięcy temu
                else:
                    end_date = datetime.now() - timedelta(days=7*30)  # 7 msc
                    start_date = datetime.now() - timedelta(days=7*30 +10)  # 7 msc i 10 dni temu

        else:
            if random.random() < 0.5:
                # Losuj analizę
                analiza = random.choice(analizy_tablica)
                ID_analizyZgloszenia = analiza[0]
                numer_sledztwa_pobrany_analiza = analiza[3]

                if numer_sledztwa_pobrany_analiza is not None:
                    data_rozpoczecia_sledztwa = [sl[1] for sl in sledztwa if sl[0] == numer_sledztwa_pobrany_analiza][0]
                    end_date = data_rozpoczecia_sledztwa
                    start_date = end_date - timedelta(days=20)
                else:
                    if T1orT2=="T1":
                    # Analiza bez śledztwa, losuj daty rok i 11 miesięcy temu
                        end_date = datetime.now() - timedelta(days=365 + 10*30)  # Rok i 10 miesięcy temu
                        start_date = datetime.now() - timedelta(days=365 + 11*30)  # Rok i 11 miesięcy temu
                    else:
                        end_date = datetime.now() - timedelta(days=7*30)  # 7 msc
                        start_date = datetime.now() - timedelta(days=7*30 +10)  # 7 msc i 10 dni temu

                numer_sledztwa = None
            else:
                # Losuj śledztwo
                sledztwo = random.choice(sledztwa)
                numer_sledztwa = sledztwo[0]
                data_rozpoczecia_sledztwa = sledztwo[1]
                data_zakonczenia_sledztwa = sledztwo[2]

                # Ustalanie daty dla czynności związanej ze śledztwem
                start_date = data_rozpoczecia_sledztwa
                if data_zakonczenia_sledztwa:
                    end_date = data_zakonczenia_sledztwa - timedelta(days=1)
                else:
                    if T1orT2=="T1":
                        end_date = datetime.now() - timedelta(days=365)  # Do roku wstecz
                    else:
                        end_date = datetime.now() - timedelta(days=1)

                ID_analizyZgloszenia = None
        
        data = fake.date_between(start_date=start_date, end_date=end_date)
        czynnosci_tablica.append((id_czynnosci,data,numerOdznaki,ID_analizyZgloszenia, numer_sledztwa))
    return czynnosci_tablica

def generate_przesluchanie_data(num_of_przesluchanie,czynnosci_tablica,powody_przesluchania,T1orT2):
    przesluchania_tablica=[]
    ##liczba_zaokraglona=floor(num_of_przesluchanie-)
    if T1orT2 == "T1":
        liczba_przesluchan_wylosowana = random.randint(1, num_of_przesluchanie-1000)
    else:
        liczba_przesluchan_wylosowana = random.randint(1, num_of_przesluchanie-10)
    ileZostaloCzynnosci = num_of_przesluchanie-liczba_przesluchan_wylosowana
    dostepne_czynnosci = [czynn for czynn in czynnosci_tablica if czynn[4] is not None]

    wybrane_id_czynnosci = set()

    for i in range(liczba_przesluchan_wylosowana):
        wybrana_czynnosc = random.choice(dostepne_czynnosci)
        id_czynnosci = wybrana_czynnosc[0]

        # Sprawdzenie, czy już wybrano tę czynność
        if id_czynnosci in wybrane_id_czynnosci:
            continue
        
        # Dodawanie do zbioru unikalnych ID
        wybrane_id_czynnosci.add(id_czynnosci)

        # Usuwanie wybranej czynności z puli dostępnych
        dostepne_czynnosci.remove(wybrana_czynnosc)

        godzina_przesluchania=fake.time()
        ID_lokalizacjiPrzesluchania=random.choice(miejsca_przesluchania)["id"]
        cel_przeslchania=random.choice(powody_przesluchania)["id"]
        id_osoby = random.randint(1,10000)
        przesluchania_tablica.append((id_czynnosci, godzina_przesluchania,ID_lokalizacjiPrzesluchania,cel_przeslchania,id_osoby))
    
    return przesluchania_tablica, ileZostaloCzynnosci, dostepne_czynnosci

def generate_weryfikacjaInformacji_data(num_of_weryfikacjaInformacji, czynnosci_tablica,typy_priorytetow,wyniki_weryfikacji, opisy_weryfikacji,sposoby_weryfikacji):
    weryfikacjaInformacji_tablica = []
    num_of_czynnosci = len(czynnosci_tablica)
    czynnosci_dla_analizy = [czynn for czynn in czynnosci_tablica if czynn[4] is None]
    czynnosci_przypisane = set()

    for i in range(num_of_weryfikacjaInformacji):

        if len(czynnosci_przypisane) < num_of_czynnosci:
            dostepne_czynnosci = [czynn for czynn in czynnosci_dla_analizy if czynn[0] not in czynnosci_przypisane]
            if dostepne_czynnosci:  # Sprawdź, czy są dostępne czynności
                id_weryfikacjiInformacji = random.choice(dostepne_czynnosci)[0]
                czynnosci_przypisane.add(id_weryfikacjiInformacji)
            else:
                # Jeśli nie ma dostępnych czynności, przypisz losowo
                id_weryfikacjiInformacji = random.choice(czynnosci_dla_analizy)[0]
        else:
            id_weryfikacjiInformacji = random.choice(czynnosci_dla_analizy)[0]

        ID_priorytetu = random.choice(typy_priorytetow)["id"]
        opis = random.choice(opisy_weryfikacji)["id"]
        ID_wynikuWeryfikacji = random.choice(wyniki_weryfikacji)["id"]
        ID_rodzajuWeryfikacji = random.choice(sposoby_weryfikacji)["id"]
        weryfikacjaInformacji_tablica.append((id_weryfikacjiInformacji, ID_priorytetu, opis, ID_wynikuWeryfikacji, ID_rodzajuWeryfikacji))

    return weryfikacjaInformacji_tablica

def generate_ogledzinyMiejscaZdarzenia_data(num_of_ogledzinyMiejscaZdarzenia, pozostaleCzynnosciSledztwo,przebiegi_ogledzin):
    ogledzinyMiejscaZdarzenia_tablica = []

    for i in range(num_of_ogledzinyMiejscaZdarzenia):
        #losowanie krotki i jej usuniecie z tablicy
        wylosowana_czynnosc = random.choice(pozostaleCzynnosciSledztwo)
        #id_ogledzinMiejscaZdarzenia = wylosowana_czynnosc[0]
        id_ogledzinMiejscaZdarzenia = wylosowana_czynnosc[0]
        # Usuwanie wybranej czynności z puli dostępnych
        pozostaleCzynnosciSledztwo.remove(wylosowana_czynnosc)

        godzina = fake.time() # zastanowic sie czy nie dodac ze musi byc pozniej niz godzina zdarzenia i 
        adres = fake.street_name() # zostawiac tak czy pobierac miejsce zdarzenia
        przebieg = random.choice(przebiegi_ogledzin)["id"]
        ogledzinyMiejscaZdarzenia_tablica.append((id_ogledzinMiejscaZdarzenia, godzina, adres, przebieg))
    
    return ogledzinyMiejscaZdarzenia_tablica

# funckcja pomocna w trakcie tworzenia materialow dowodowych zeby szybciej znalezc o ktorej czynnosci mowa, zeby moc przypisac jej dateZebrania
def znajdz_czynnosc_po_id(czynnosci_tablica, szukane_id):
    for czynnosc in czynnosci_tablica:
        if czynnosc[0] == szukane_id:
            return czynnosc
    return None


# najpierw przypisujemy KAZDEMU przesluchaniu dowod z rodzajem "zeznanie",a pozniej dla pozostalej liczby dowodow przypisujemy do ogledzin
def generate_materialDowodowy_data(num_of_materialDowodowy, przesluchania, ogledzinyMiejscaZdarzenia, czynnosci_tablica, typy_materialow_dowodowych, raporty):
    materialDowodowy_tablica = []
    total_num_of_przesluchania = len(przesluchania)
    
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
        # dla zeznania ID jest zawsze 0 (jest jako pierwsze)
        rodzaj = "zeznanie"
        ID_rodzajuMaterialuDowodowego = 0
        raport = random.choice(raporty)["id"]
        materialDowodowy_tablica.append((ID_materialuDowodowego, dataZebrania, miejsceZebrania, raport, ID_rodzajuMaterialuDowodowego, ID_czynnosci))
    
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
        ID_rodzajuMaterialuDowodowego = random.choice([typ for typ in typy_materialow_dowodowych if typ["name"] != "zeznanie"])["id"]
        raport = "raport"

        materialDowodowy_tablica.append((ID_materialuDowodowego, dataZebrania, miejsceZebrania, raport, ID_rodzajuMaterialuDowodowego, ID_czynnosci))
        pozostala_num_of_dowody -= 1
    
    return materialDowodowy_tablica

def generate_zwiazany_z_data(sledztwa_dane, material_dowodowy_dane, czynnosci_tablica):
    zwiazany_z_tablica = []

    for material in material_dowodowy_dane:
        ID_materialuDowodowego = material[0]
        ID_czynnosci = material[5]

        czynnosc = znajdz_czynnosc_po_id(czynnosci_tablica, ID_czynnosci)

        ID_sledztwa = czynnosc[4]

        if ID_sledztwa is not None:
            zwiazany_z_tablica.append((ID_sledztwa, ID_materialuDowodowego))
    
    return zwiazany_z_tablica

def write_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        # Write header if the data is a list of named tuples
        if hasattr(data[0], '_fields'):
            writer.writerow(data[0]._fields)

        # Write data rows
        if isinstance(data[0], tuple):
            for row in data:
                writer.writerow(row)
        else:
            for item in data:
                writer.writerow(item)

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
save_to_csv(typy_zdarzen,"typy_zdarzen.csv")
sposoby_zgloszenia = generate_possible_types_of_something(possible_ways_of_zdarzenie)
save_to_csv(sposoby_zgloszenia,"sposoby_zgloszenia.csv")

miejsca_przesluchania = generate_possible_types_of_something(possible_places_of_przesluchanie)
save_to_csv(miejsca_przesluchania,"miejsca_przesluchania.csv")

powody_przesluchania = generate_possible_types_of_something(possible_purpose_of_hearing)
save_to_csv(powody_przesluchania,"powody_przesluchania.csv")

statusy_sledztwa = generate_possible_types_of_something(possible_status_of_sledztwo)
save_to_csv(statusy_sledztwa,"statusy_sledztwa.csv")

typy_materialow_dowodowych = generate_possible_types_of_something(possible_type_od_material)
save_to_csv(typy_materialow_dowodowych,"typy_materialow_dowodowych.csv")

typy_priorytetow = generate_possible_types_of_something(possible_priorities)
save_to_csv(typy_priorytetow,"typy_priorytetow.csv")

wyniki_weryfikacji = generate_possible_types_of_something(possible_outcome_of_verification)
save_to_csv(wyniki_weryfikacji,"wyniki_weryfikacji.csv")

sposoby_weryfikacji = generate_possible_types_of_something(possible_way_of_verification)
save_to_csv(sposoby_weryfikacji,"sposoby_weryfikacji.csv")
podstawy_rozpoczecia_sledztwa = generate_possible_types_of_something(possible_types_of_podstawy)
save_to_csv(podstawy_rozpoczecia_sledztwa,"podstawy_rozpoczecia_sledztwa.csv")

opisy_zgloszen = generate_possible_types_of_something(possible_types_of_opis_zgloszenia)
save_to_csv(opisy_zgloszen,"opisy_zgloszen.csv")

opisy_zdarzen = generate_possible_types_of_something(possible_types_of_opis_zdarzenia)
save_to_csv(opisy_zdarzen,"opisy_zdarzen.csv")

raporty = generate_possible_types_of_something(possible_types_of_raport)
save_to_csv(raporty,"raporty.csv")

przebiegi_ogledzin = generate_possible_types_of_something(possible_types_of_przebieg_ogledzin)
save_to_csv(przebiegi_ogledzin,"przebiegi_ogledzin.csv")

opisy_weryfikacji = generate_possible_types_of_something(possible_types_of_opis_werfikacji)
save_to_csv(opisy_weryfikacji,"opisy_weryfikacji.csv")

T1 = "T1"
T2 = "T2"

def update_indices_of_new_data(oldData, newData):
    zaktualizowane_indeksy_newData = []
    ostatni_indeks = len(oldData)

    for i in range(len(newData)):
        newID = ostatni_indeks + i

        zaktualizowane_dane = (newID,) + newData[i][1:]
    
        zaktualizowane_indeksy_newData.append(zaktualizowane_dane)

    return zaktualizowane_indeksy_newData

# generowanie danych
# 1. zdarzen musi byc > niz sledztw
# 2. analiz musi byc > niz sledztw & musi byc tyle samo lub < co zgłoszeń

sledztwa = generate_sledztwo_data(1000, statusy_sledztwa,T1)

print("Śledztwa:")
# for sledztwo in sledztwa:
#     numer_sledztwa, data_rozpoczecia, data_zakonczenia, ID_statusuSledztwa, numer_odznaki = sledztwo
#     print(f"Numer śledztwa: {numer_sledztwa}, Data rozpoczęcia: {data_rozpoczecia}, Data zakończenia: {data_zakonczenia}")
# print("-" * 40)
write_to_csv(sledztwa,"sledztwa.csv")
sledztwa1_updated=update_sledztwo(sledztwa)
sledztwa2=generate_sledztwo_data(100,statusy_sledztwa,T2)
sledztwa2updated = update_indices_of_new_data(sledztwa,sledztwa2)

sledztwa_updated=sledztwa+sledztwa2updated
write_to_csv(sledztwa_updated,"sledztwa_update.csv")

zdarzenia = generate_zdarzenie_data(1100, typy_zdarzen, sledztwa,T1,opisy_zdarzen)
zdarzenia2 = generate_zdarzenie_data(100, typy_zdarzen, sledztwa2updated,T2,opisy_zdarzen)
zdarzenia2updated = update_indices_of_new_data(zdarzenia,zdarzenia2)

zdarzenia_updated = zdarzenia+zdarzenia2updated

print("Zdarzenia:")
# for zdarzenie in zdarzenia:
#     ID_zdarzenia, data_zdarzenia, ID_rodzajuZdarzenia, opis_zdarzenia, godzina_zdarzenia, adres_zdarzenia, numer_sledztwa = zdarzenie
#     print(f"ID zdarzenia: {ID_zdarzenia}, Data zdarzenia: {data_zdarzenia}, Numer śledztwa: {numer_sledztwa}")
# print("-" * 40)
write_to_csv(zdarzenia,"zdarzenia.csv")
write_to_csv(zdarzenia_updated,"zdarzenia_updated.csv")

analizy_zgloszen = generate_analiza_data(1100, sledztwa,podstawy_rozpoczecia_sledztwa)
analizy_zgloszen2 = generate_analiza_data(100, sledztwa2updated,podstawy_rozpoczecia_sledztwa)
analizy_zgloszen2updated = update_indices_of_new_data(analizy_zgloszen,analizy_zgloszen2)
analizy_updated = analizy_zgloszen + analizy_zgloszen2updated

print("Analizy zgłoszeń:")
# for analiza in analizy_zgloszen:
#     analiza_id,rozpoczecieSledztwa_value,podstawy, numer_sledztwa = analiza
#     print(f"ID analizy: {analiza_id}, porzpoczecie czy nie: {rozpoczecieSledztwa_value}, Numer śledztwa: {numer_sledztwa}")
# print("-" * 40)
write_to_csv(analizy_zgloszen,"analizy_zgloszen.csv")
write_to_csv(analizy_updated,"analizy_updated.csv")

zgloszenia = generate_zgloszenia_data(1000,zdarzenia,analizy_zgloszen,sposoby_zgloszenia,opisy_zgloszen)
print("zgloszenie1")
zgloszenia2 = generate_zgloszenia_data(100,zdarzenia2updated,analizy_zgloszen2updated,sposoby_zgloszenia,opisy_zgloszen)
print("zgloszenie2")

zgloszenia2updated = update_indices_of_new_data(zgloszenia,zgloszenia2)
zgloszenia_updated = zgloszenia+ zgloszenia2updated

write_to_csv(zgloszenia,"zgloszenia.csv")
write_to_csv(zgloszenia_updated,"zgloszenia_updated.csv")
print("zgloszenia")
czynnosci = generate_czynnosc_data(10000, analizy_zgloszen, sledztwa,T1)
czynnosci2 = generate_czynnosc_data(3000, analizy_zgloszen2, sledztwa2updated,T2)

czynnosci2updated = update_indices_of_new_data(czynnosci,czynnosci2)
czynnosci_updated = czynnosci + czynnosci2updated

print("Czynności:")
# for czynność in czynnosci:
#     id_czynnosci, data, numerOdznaki, ID_analizyZgloszenia, numer_sledztwa = czynność
#     print(f"ID czynności: {id_czynnosci}, Data: {data}, Numer odznaki: {numerOdznaki}, ID analizy zgłoszenia: {ID_analizyZgloszenia}, Numer śledztwa: {numer_sledztwa}")
# print("-" * 40)
write_to_csv(czynnosci,"czynnosci.csv")
write_to_csv(czynnosci_updated,"czynnosci_updated.csv")

liczba_czynnosci_do_analizy = 0
liczba_czynnosci_do_sledztwa = 0


# Iteracja przez czynności, aby policzyć przypisania do analiz i śledztw
for czynnosci_item in czynnosci:
    ID_analizyZgloszenia = czynnosci_item[3]  # Indeks 2 dla ID analizy
    numer_sledztwa = czynnosci_item[4]  # Indeks 4 dla numeru śledztwa

    if ID_analizyZgloszenia is not None:  # Sprawdzamy, czy przypisano do analizy
        liczba_czynnosci_do_analizy += 1
    if numer_sledztwa is not None:  # Sprawdzamy, czy przypisano do śledztwa
        liczba_czynnosci_do_sledztwa += 1

liczba_czynnosci_do_analizy2 = 0
liczba_czynnosci_do_sledztwa2 = 0

for czynnosci_item in czynnosci2:
    ID_analizyZgloszenia = czynnosci_item[3]  # Indeks 2 dla ID analizy
    numer_sledztwa = czynnosci_item[4]  # Indeks 4 dla numeru śledztwa

    if ID_analizyZgloszenia is not None:  # Sprawdzamy, czy przypisano do analizy
        liczba_czynnosci_do_analizy2 += 1
    if numer_sledztwa is not None:  # Sprawdzamy, czy przypisano do śledztwa
        liczba_czynnosci_do_sledztwa2 += 1

print(f"LICZBA CZYNNOSCI DO ANALIZY: {liczba_czynnosci_do_analizy}")
print(f"LICZBA CZYNNOSCI DO SLEDZTWA: {liczba_czynnosci_do_sledztwa}")

print(f"LICZBA CZYNNOSCI DO ANALIZY: {liczba_czynnosci_do_analizy2}")
print(f"LICZBA CZYNNOSCI DO SLEDZTWA: {liczba_czynnosci_do_sledztwa2}")
przesluchania, ileZostajeCzynnosci, pozostaleCzynnosciSledztwo = generate_przesluchanie_data(liczba_czynnosci_do_sledztwa, czynnosci, powody_przesluchania,T1)
przesluchania2, ileZostajeCzynnosci2, pozostaleCzynnosciSledztwo2 = generate_przesluchanie_data(liczba_czynnosci_do_sledztwa2, czynnosci2updated, powody_przesluchania,T2)
#przesluchania2updated = update_indices_of_new_data(przesluchania,przesluchania2)
przesluchania_updated = przesluchania+przesluchania2

print("Przesłuchania:")
# for przesluchanie in przesluchania:
#     id_przesluchania, numer_sledztwa, data_przesluchania, ID_policjanta, opis = przesluchanie
#     print(f"ID przesłuchania: {id_przesluchania}, Numer śledztwa: {numer_sledztwa}, Data przesłuchania: {data_przesluchania}, ID policjanta: {ID_policjanta}, Opis: {opis}")
# print("-" * 40)
write_to_csv(przesluchania,"przesluchania.csv")
write_to_csv(przesluchania_updated,"przesluchania_updated.csv")


ogledzinyMiejscaZdarzenia = generate_ogledzinyMiejscaZdarzenia_data(ileZostajeCzynnosci,pozostaleCzynnosciSledztwo,przebiegi_ogledzin)
ogledzinyMiejscaZdarzenia2 = generate_ogledzinyMiejscaZdarzenia_data(ileZostajeCzynnosci2,pozostaleCzynnosciSledztwo2,przebiegi_ogledzin)
#ogledzinyMiejscaZdarzenia2updated = update_indices_of_new_data(ogledzinyMiejscaZdarzenia,ogledzinyMiejscaZdarzenia2)
updated_ogledziny = ogledzinyMiejscaZdarzenia + ogledzinyMiejscaZdarzenia2

print("Oględziny miejsca zdarzenia:")
# for ogledziny in ogledzinyMiejscaZdarzenia:
#     id_ogledzinMiejscaZdarzenia, godzina, adres, przebieg = ogledziny
#     print(f"ID oględzin: {id_ogledzinMiejscaZdarzenia}")
# print("-" * 40)
write_to_csv(ogledzinyMiejscaZdarzenia,"ogledziny.csv")
write_to_csv(updated_ogledziny,"ogledziny_updated.csv")

weryfikacjeInformacji = generate_weryfikacjaInformacji_data(liczba_czynnosci_do_analizy,czynnosci,typy_priorytetow,wyniki_weryfikacji,opisy_weryfikacji,sposoby_weryfikacji)
weryfikacjeInformacji2 = generate_weryfikacjaInformacji_data(liczba_czynnosci_do_analizy2,czynnosci2updated,typy_priorytetow,wyniki_weryfikacji,opisy_weryfikacji,sposoby_weryfikacji)
#weryfikacjeInformacji2updated = update_indices_of_new_data(weryfikacjeInformacji,weryfikacjeInformacji2)
updated_weryfikacje = weryfikacjeInformacji+weryfikacjeInformacji2

print("Weryfikacje informacji:")
# for weryfikacja in weryfikacjeInformacji:
#     id_weryfikacjiInformacji, ID_priorytetu, opis, ID_wynikuWeryfikacji, ID_rodzajuWeryfikacji = weryfikacja
#     print(f"ID weryfikacji: {id_weryfikacjiInformacji}")
# print("-" * 40)
write_to_csv(weryfikacjeInformacji,"weryfikacje.csv")
write_to_csv(updated_weryfikacje,"weryfikacje_updated.csv")


materialyDowodowe = generate_materialDowodowy_data(6000, przesluchania, ogledzinyMiejscaZdarzenia, czynnosci, typy_materialow_dowodowych,raporty)
print("Materiały dowodowe:")
for material in materialyDowodowe:
    ID_materialuDowodowego, dataZebrania, miejsceZebrania, raport, ID_rodzajuMaterialuDowodowego, ID_czynnosci = material
    print(f"ID materiału: {ID_materialuDowodowego}, ID czynności: {ID_czynnosci}")
print("-" * 40)
materialyDowodowe2 = generate_materialDowodowy_data(1800, przesluchania2, ogledzinyMiejscaZdarzenia2, czynnosci2updated, typy_materialow_dowodowych,raporty)
materialyDowodowe2updated = update_indices_of_new_data(materialyDowodowe,materialyDowodowe2)
materialy_updated = materialyDowodowe+materialyDowodowe2updated

print("Materiały dowodowe2:")
for material in materialyDowodowe2:
    ID_materialuDowodowego, dataZebrania, miejsceZebrania, raport, ID_rodzajuMaterialuDowodowego, ID_czynnosci = material
    print(f"ID materiału: {ID_materialuDowodowego}, ID czynności: {ID_czynnosci}")
print("-" * 40)
write_to_csv(materialyDowodowe,"materialy.csv")
write_to_csv(materialy_updated,"materialy_updated.csv")

zwiazanyZ = generate_zwiazany_z_data(sledztwa,materialyDowodowe,czynnosci)
zwiazanyZ2 = generate_zwiazany_z_data(sledztwa2updated,materialyDowodowe2updated,czynnosci2updated)
#zawiazanyZ2updated = update_indices_of_new_data(zwiazanyZ,zwiazanyZ2)
zwiazanyZ_updated = zwiazanyZ+zwiazanyZ2

for zwiaz in zwiazanyZ:
    ID_sledztwa, ID_materialuDowodowego = zwiaz
    ##print(f"ID materiału: {ID_materialuDowodowego}, ID sledztwa: {ID_sledztwa}")
##print("-" * 40)
write_to_csv(zwiazanyZ,"zwiaznyz.csv")
write_to_csv(zwiazanyZ_updated,"zwiazany_z_updated.csv")


# tabela_sledztwa=generate_sledztwo_data(100,statusy_sledztwa)
# write_to_csv(tabela_sledztwa,"sledztwa.csv")



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