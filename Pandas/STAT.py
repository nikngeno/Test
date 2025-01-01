import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # type: ignore

stat_csv = pd.read_csv(r'C:\Users\nicho\vscode\vscodeprojects\STAT.csv', header=0, encoding='latin-1')

#print(stat_csv.head())
stat_csv.isna().sum()

stat_csv.rename(columns={'User': 'Users'},inplace=True)

stat_csv['Start time'] = pd.to_datetime(stat_csv['Start time'])
stat_csv['Completion time'] = pd.to_datetime(stat_csv['Completion time'])

stat_csv['Time used'] = stat_csv['Completion time'] - stat_csv['Start time']
stat_csv['Time used'] = stat_csv['Time used'].dt.total_seconds()
#monthly_df = stat_csv('M').sum()

print(stat_csv.head())
print(stat_csv.shape)

staff_counts = stat_csv['Staff Name'].value_counts()

# 2. Plot these counts as a bar chart
staff_counts.plot(kind='bar', title="Staff Count")
plt.xlabel('Staff Name')
plt.ylabel('Count')
plt.show()

#stat_reordered = stat_csv[['ID','Email','Staff Name','Location','User','Reason for Visit']]
#print(stat_reordered.head())