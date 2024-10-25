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
    "manslaughter", 
    "threatening", 
    "burglary", 
    "fraud", 
    "money laundering", 
    "tax evasion", 
    "identity theft"
]

possible_ways_of_zdarzenie=["personally", "by phone"]

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
        #numer_odznaki
        id_analizy=random.randint(0,len(analizy_tablica)-1)
        zgloszenia_tablica.append((zgloszenie_id,zgloszenie_sposob,zgloszenie_data,id_zdarzenia,id_analizy))
    return zgloszenia_tablica

zdarzenia=generate_zdarzenie_data_later(10)
analizy=generate_analiza_data(10)
zgloszenia=generate_zgloszenia_data(20,zdarzenia,analizy)
print(zgloszenia)

