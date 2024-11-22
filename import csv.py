import csv
import random
from datetime import datetime, timedelta
from faker import Faker

# Initialize Faker
faker = Faker()

# Define constraints
num_records = 950
start_date = datetime(1979, 1, 1)
end_date = datetime(1996, 12, 31)
nationalities = ['USA', 'Canada', 'England', 'Australia', 'Germany', 'France', 'Spain', 'Brazil', 'Italy', 'Argentina']

# Function to generate a random date between two dates
def random_date(start, end):
    delta = end - start
    random_days = random.randrange(delta.days)
    return start + timedelta(days=random_days)

# Generate data and write to CSV
with open('players.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['PlayerID', 'FirstName', 'LastName', 'DateofBirth', 'Nationality', 'Height', 'Weight', 'PositionID']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()
    for i in range(1, num_records + 1):
        player = {
            'PlayerID': i,
            'FirstName': faker.first_name(),
            'LastName': faker.last_name(),
            'DateofBirth': random_date(start_date, end_date).strftime('%Y-%m-%d'),
            'Nationality': random.choice(nationalities),
            'Height': random.randint(172, 210),
            'Weight': random.randint(75, 110),
            'PositionID': random.randint(1, 4),
        }
        writer.writerow(player)
