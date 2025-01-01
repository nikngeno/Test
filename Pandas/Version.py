import pandas as pd

print(pd.__version__)
a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar1 = pd.Series(calories, index = ["day1", "day2"])

myvar = pd.Series(calories)

print(myvar)
print(myvar1)
print(a[1])

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)
print(df.loc[1])
print(df.loc[[0, 2]])