# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
# from species import SpeciesSighting


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Wildlife')

wildlife = SHEET.worksheet('Wildlife')

class SpeciesSighting:
    def __init__(self, species_id, common_name, scientific_name, typical_habitats, 
                 estimated_population, date_and_time_of_sighting, location_of_sighting, notes):
        self.species_id = species_id
        self.common_name = common_name
        self.scientific_name = scientific_name.strip()  # To remove any extra spaces
        self.typical_habitats = typical_habitats
        self.estimated_population = estimated_population
        self.date_and_time_of_sighting = datetime.strptime(date_and_time_of_sighting, '%d/%m/%Y %H:%M')
        self.location_of_sighting = location_of_sighting
        self.notes = notes

    def __str__(self):
        return f"{self.common_name} ({self.scientific_name}) seen at {self.location_of_sighting} on {self.date_and_time_of_sighting.strftime('%d/%m/%Y %H:%M')}."


sighting1 = SpeciesSighting(14, "test ed Fox", "Vulpes vulpes", "Location of sighting", "150,000", "23/08/2023 15:30", "Cork City Park", "None")
sighting2 = SpeciesSighting(15, "test Irish Hare", "Lepus timidus hibernicus", "Woodlands, urban", "40,000", "24/08/2023 07:20", "Galway Countryside", "None")

print(sighting1)
print(sighting2)


def all_data():
    data = wildlife.get_all_values()
    print(data)



all_data()

# def main():
