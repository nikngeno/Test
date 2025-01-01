import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\nicho\vscode\vscodeprojects\data.csv', header=0)
df.head()

print(df.head())

new_df = df.dropna()

print(new_df.to_string())

df.dropna(inplace = True)

print(df.to_string())