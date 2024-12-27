import numpy as np
import pandas as pd
import random

s1 = pd.Series([10,20,30], index =['a','b','c'])
print(s1)

s2 = pd.Series({'x':100,'y':200,'z': 300})
print(s2)

s3 = pd.Series(['Nick','Tim','Ben','Gabriel'], index =[1,2,3,4])
print(s3)


s4  = pd.Series(np.random.randint(low = 1, high = 100, size = 5))
print(s4)
print(np.mean(s4))

