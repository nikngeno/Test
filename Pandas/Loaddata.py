import pandas as pd
import numpy as np

df_csv = pd.read_csv(r'C:\Users\nicho\vscode\vscodeprojects\NHL.csv', header=0)

print(df_csv.head())
print(pd.options.display.max_rows) 