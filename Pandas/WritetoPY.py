import pandas as pd
import numpy as np


animals ={
    'Name': ['Tiger', 'Elephant','Shark','Dog','Rooster'],
    'Species': ['Cat', 'Mammal','Fish','Mammal','Chicken'],
    'Age': [5, 10, 3, 2, 1],
    'Weight': [200, 5000, 1000, 20, 5]
}
df = pd.DataFrame(animals)

df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False, sheet_name='NewData')
