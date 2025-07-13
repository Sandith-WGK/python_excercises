import pandas as pd

import matplotlib.pyplot as plt

s = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s)
print(s['a'])    # Output: 1
print(s[0:2])

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}

print(type(data))

df = pd.DataFrame(data,index=[1,2,3])

print(df)

print(df.shape)
df['Salary'] = [50000, 60000, 70000]
print(df)

df.plot(kind='bar', x='Name', y='Salary', title='Salary by Name')
plt.show()