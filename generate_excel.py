import pandas as pd
import random
from faker import Faker
from datetime import datetime,timedelta


def generate_police_data_xlsx(num_officers):
    fake = Faker("pl_PL")
    police_data = []

    for _ in range(num_officers):
        badge_number = random.randint(100000, 999999)
        first_name = fake.first_name()
        last_name = fake.last_name()
        pesel = fake.pesel()
        rank = random.choice(["Posterunkowy", "Starszy Posterunkowy", "Sierżant", "Starszy Sierżant", "Aspirant"])
        one_year_ago_and_day=datetime.now()-timedelta(days=367)
        one_year_ago = datetime.now() - timedelta(days=365)

        
        end_service_start=one_year_ago_and_day
        end_service_end=one_year_ago
        probability=0.3
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

    # Creating a DataFrame
    police_df = pd.DataFrame(police_data, columns=[
        "Numer odznaki", "Imię", "Nazwisko", "Pesel", "Stopień służbowy", "Data rozpoczęcia służby",
        "Data zakończenia służby", "Numer seryjny broni", "Data urodzenia", "Numer telefonu",
        "Adres zamieszkania, miasto", "Adres zamieszkania, ulica i numer", 
        "Adres zamieszkania, kod pocztowy", "Aktualny posterunek"
    ])

    # Saving to Excel
    police_df.to_excel(name_of_file, index=False)

def update_police_data_xlsx(file_path,number_new_records, probability=0.3, name_of_file="police_data_updated.xlsx"):
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
        badge_number = random.randint(100000, 999999)  # Unique badge number
        first_name = fake.first_name()
        last_name = fake.last_name()
        pesel = fake.pesel()
        rank = random.choice(["Posterunkowy", "Starszy Posterunkowy", "Sierżant", "Starszy Sierżant", "Aspirant"])
        one_year_ago_and_day=datetime.now()-timedelta(days=367)
        service_start_date = fake.date_between(start_date=one_year_ago_and_day, end_date="today").strftime("%d-%m-%Y")
        converted = pd.to_datetime(service_start_date, format='%d-%m-%Y', errors='coerce')
        service_end_date = fake.date_between(start_date=converted, end_date="today") if random.random() < probability else ""
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




#type - okres czasu w ktorym generujemy dane o polcijantach
generate_police_data_xlsx(num_officers=100)
update_police_data_xlsx("police_data_time1.xlsx",20)

