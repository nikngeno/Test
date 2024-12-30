import pandas as pd

animals ={
    'Name': ['Tiger', 'Elephant','Shark','Dog','Rooster'],
    'Species': ['Cat', 'Mammal','Fish','Mammal','Chicken'],
    'Age': [5, 10, 3, 2, 1],
    'Weight': [200, 5000, 1000, 20, 5]
}

df = pd.DataFrame(animals)
print(df)
print(df.shape)
print(df.columns)
print(df.index)
