import pandas as pd
import random
from faker import Faker
from datetime import datetime,timedelta


def generate_police_data_xlsx(num_officers):
    fake = Faker("pl_PL")
    police_data = []
    badge_number=10000

    for _ in range(num_officers):
        
        first_name = fake.first_name()
        last_name = fake.last_name()
        pesel = fake.pesel()
        rank = random.choice(["Posterunkowy", "Starszy Posterunkowy", "Sierżant", "Starszy Sierżant", "Aspirant"])
        one_year_ago_and_day=datetime.now()-timedelta(days=367)
        one_year_ago = datetime.now() - timedelta(days=365)

        
        end_service_start=one_year_ago_and_day
        end_service_end=one_year_ago
        probability=0.15
        name_of_file="police_data_time1.xlsx"

        
        service_start_date = fake.date_between(start_date="-30y", end_date=end_service_start)
        
        
        # Sometimes leave the end date blank to indicate active duty
        service_end_date = fake.date_between(start_date=service_start_date, end_date=end_service_end) if random.random() < probability else ""
        
        serial_number = f"{random.randint(100000, 999999):06d}"
        birth_date = fake.date_of_birth(minimum_age=22, maximum_age=60)
        phone_number = fake.random_number(digits=9, fix_len=True)
        
        city = random.choice(["Gdańsk", "Gdynia", "Sopot"])

        street = f"{fake.street_name()} {fake.building_number()}"
        postal_code = fake.postcode()
        
        current_station_id = random.randint(1, 30)

        police_data.append([
            badge_number,          # Kolumna A - Numer odznaki
            first_name,            # Kolumna B - Imię
            last_name,             # Kolumna C - Nazwisko
            pesel,                 # Kolumna D - Pesel
            rank,                  # Kolumna E - Stopień służbowy
            service_start_date.strftime("%d-%m-%Y"),   # Kolumna F - Data rozpoczęcia służby
            service_end_date.strftime("%d-%m-%Y") if service_end_date else "",   # Kolumna G - Data zakończenia służby
            serial_number,         # Kolumna H - Numer seryjny broni
            birth_date.strftime("%d-%m-%Y"),  # Kolumna I - Data urodzenia
            phone_number,          # Kolumna J - Numer telefonu
            city,                  # Kolumna K - Adres zamieszkania, miasto
            street,                # Kolumna L - Adres zamieszkania, ulica i numer
            postal_code,           # Kolumna M - Adres zamieszkania, kod pocztowy
            current_station_id     # Kolumna N - Aktualny posterunek, unikatowe ID posterunku
        ])
        badge_number=badge_number+1
    # Creating a DataFrame
    police_df = pd.DataFrame(police_data, columns=[
        "Numer odznaki", "Imię", "Nazwisko", "Pesel", "Stopień służbowy", "Data rozpoczęcia służby",
        "Data zakończenia służby", "Numer seryjny broni", "Data urodzenia", "Numer telefonu",
        "Adres zamieszkania, miasto", "Adres zamieszkania, ulica i numer", 
        "Adres zamieszkania, kod pocztowy", "Aktualny posterunek"
    ])

    # Saving to Excel
    police_df.to_excel(name_of_file, index=False)

def update_police_data_xlsx(file_path,number_new_records, probability=0.1, name_of_file="police_data_updated.xlsx"):
    fake = Faker("pl_PL")
    
    # Read existing data into a DataFrame
    existing_data = pd.read_excel(file_path)

    for index, row in existing_data.iterrows():
        # Zachowaj oryginalne dane
        badge_number = row['Numer odznaki']
        first_name = row['Imię']
        last_name = row['Nazwisko']
        pesel = row['Pesel']
        rank = row['Stopień służbowy']
        service_start_date = row['Data rozpoczęcia służby']
        service_end_date = row['Data zakończenia służby']
        serial_number = row['Numer seryjny broni']
        birth_date = row['Data urodzenia']
        phone_number = row['Numer telefonu']
        city = row['Adres zamieszkania, miasto']
        street = row['Adres zamieszkania, ulica i numer']
        postal_code = row['Adres zamieszkania, kod pocztowy']
        current_station_id = row['Aktualny posterunek']
        last_badge_number = existing_data['Numer odznaki'].dropna().iloc[-1]+1

        
        print("Service End Date:", service_end_date)  # Debug
        if pd.isna(service_end_date):
            print("Service End Date is None")
        
            # Zmiana daty zakończenia służby z określonym prawdopodobieństwem
            if random.random() < probability:
                # Generate service end date using datetime objects
                converted = pd.to_datetime(service_start_date, format='%d-%m-%Y', errors='coerce')
                if pd.isna(converted):
                    print(f"Invalid start date for badge {badge_number}: {service_start_date}")  # Debug
                    continue  # Skip this row if the date is invalid
                
                service_end_date = fake.date_between(start_date=converted, end_date=datetime.now())
                # Format service_end_date to the desired string format
                existing_data.at[index, 'Data zakończenia służby'] = service_end_date.strftime("%d-%m-%Y") if service_end_date else None
        new_records = []
    for _ in range(number_new_records):
        badge_number = last_badge_number  # Unique badge number
        first_name = fake.first_name()
        last_name = fake.last_name()
        pesel = fake.pesel()
        rank = random.choice(["Posterunkowy", "Starszy Posterunkowy", "Sierżant", "Starszy Sierżant", "Aspirant"])
        one_year_ago_and_day=datetime.now()-timedelta(days=367)
        service_start_date = fake.date_between(start_date=one_year_ago_and_day, end_date="today").strftime("%d-%m-%Y")
        converted = pd.to_datetime(service_start_date, format='%d-%m-%Y', errors='coerce')
        service_end_date = fake.date_between(start_date=converted, end_date="today").strftime("%d-%m-%Y") if random.random() < probability else None
        serial_number = f"{random.randint(100000, 999999):06d}"
        birth_date = fake.date_of_birth(minimum_age=22, maximum_age=60).strftime("%d-%m-%Y")
        phone_number = fake.random_number(digits=9, fix_len=True)
        city = random.choice(["Gdańsk", "Gdynia", "Sopot"])
        street = f"{fake.street_name()} {fake.building_number()}"
        postal_code = fake.postcode()
        current_station_id = random.randint(1, 30)

        # Append new record to the list
        new_records.append([
            badge_number, first_name, last_name, pesel, rank, 
            service_start_date, service_end_date, serial_number, 
            birth_date, phone_number, city, street, postal_code, 
            current_station_id
        ])
        last_badge_number=last_badge_number+1

    # Create a DataFrame for new records and append to existing data
    new_records_df = pd.DataFrame(new_records, columns=[
        "Numer odznaki", "Imię", "Nazwisko", "Pesel", "Stopień służbowy", 
        "Data rozpoczęcia służby", "Data zakończenia służby", "Numer seryjny broni", 
        "Data urodzenia", "Numer telefonu", "Adres zamieszkania, miasto", 
        "Adres zamieszkania, ulica i numer", "Adres zamieszkania, kod pocztowy", 
        "Aktualny posterunek"
    ])

    # Concatenate existing data with new records
    updated_data = pd.concat([existing_data, new_records_df], ignore_index=True)

    # Save to Excel
    updated_data.to_excel(name_of_file, index=False)

def generate_people_data_xlsx(num_people):
    fake = Faker("pl_PL")
    
    people_data = []

    for person_id in range(1, num_people + 1):
        first_name = fake.first_name()
        last_name = fake.last_name()
        pesel = fake.pesel()  # PESEL
        if first_name[-1].lower() == 'a':  
            gender= 'Kobieta'  
        else:
            gender= 'Mężczyzna' 
        birth_date = fake.date_of_birth(minimum_age=18, maximum_age=80).strftime("%d-%m-%Y")
        phone_number = fake.phone_number()
        city = fake.city()
        street_address = fake.street_address()
        postal_code = fake.zipcode()
        
        person_type = random.choice(['Podejrzany', 'Świadek', 'Osoba zgłaszająca'])
        
        # Wypełnianie dodatkowych kolumn w zależności od typu osoby
        if person_type == 'Świadek':
            is_convicted = random.choice(['Tak', 'Nie'])
            type_of_witness = random.choice(['Naoczny', 'Biegły', 'Charakteru', 'Sytuacyjny', 'Inny'])
            credibility = random.choice(['Mały', 'Średni', 'Duży'])
        else:
            is_convicted = None
            type_of_witness = None
            credibility = None
        
        people_data.append((person_id, first_name, last_name, pesel, gender,
                             birth_date, phone_number, city, street_address, postal_code,
                             person_type, is_convicted, type_of_witness, credibility))

    # Tworzenie DataFrame
    columns = [
        "ID osoby", "Imię", "Nazwisko", "Pesel", "Płeć",
        "Data urodzenia", "Numer telefonu", "Adres zamieszkania, miasto",
        "Adres zamieszkania, ulica i numer", "Adres zamieszkania, kod pocztowy",
        "Typ osoby", "Czy karany", "Rodzaj", "Wiarygodność"
    ]
    
    people_df = pd.DataFrame(people_data, columns=columns)

    # Zapis do pliku Excel
    people_df.to_excel("people_data.xlsx", index=False)
    


def update_people_data_xlsx(file_path, num_new_people):
    fake = Faker("pl_PL")

    existing_data = pd.read_excel(file_path)
    existing_count = len(existing_data)

    new_people_data = []

    for person_id in range(existing_count + 1, existing_count + num_new_people + 1):
        first_name = fake.first_name()
        last_name = fake.last_name()
        pesel = fake.pesel()
        gender = 'Kobieta' if first_name[-1].lower() == 'a' else 'Mężczyzna'
        birth_date = fake.date_of_birth(minimum_age=18, maximum_age=80).strftime("%d-%m-%Y")
        phone_number = fake.phone_number()
        city = fake.city()
        street_address = fake.street_address()
        postal_code = fake.zipcode()
        
        person_type = random.choice(['Podejrzany', 'Świadek', 'Osoba zgłaszająca'])
        
        if person_type == 'Świadek':
            is_convicted = random.choice(['Tak', 'Nie'])
            type_of_witness = random.choice(['Naoczny', 'Biegły', 'Charakteru', 'Sytuacyjny', 'Inny'])
            credibility = random.choice(['Mały', 'Średni', 'Duży'])
        else:
            is_convicted = None
            type_of_witness = None
            credibility = None
        
        new_people_data.append((person_id, first_name, last_name, pesel, gender,
                                 birth_date, phone_number, city, street_address, postal_code,
                                 person_type, is_convicted, type_of_witness, credibility))

    # Dodanie nowych danych do istniejącego DataFrame
    new_columns = [
        "ID osoby", "Imię", "Nazwisko", "Pesel", "Płeć",
        "Data urodzenia", "Numer telefonu", "Adres zamieszkania, miasto",
        "Adres zamieszkania, ulica i numer", "Adres zamieszkania, kod pocztowy",
        "Typ osoby", "Czy karany", "Rodzaj", "Wiarygodność"
    ]
    
    new_people_df = pd.DataFrame(new_people_data, columns=new_columns)

    # Łączenie starych i nowych danych
    updated_data = pd.concat([existing_data, new_people_df], ignore_index=True)

    # Zapis do pliku Excel
    updated_data.to_excel("people_data_updated.xlsx", index=False)




#type - okres czasu w ktorym generujemy dane o polcijantach
generate_police_data_xlsx(num_officers=100)
update_police_data_xlsx("police_data_time1.xlsx",20)
generate_people_data_xlsx(num_people=100)
update_people_data_xlsx("people_data.xlsx",20)



