import pandas as p

s1 = p.Series([1, 2, 3], index=['A', 'B', 'C'])
s2 = p.Series([4, 5, 6], index=['A', 'B', 'C'])
s3 = p.Series([7, 8, 9], index=['A', 'B', 'C'])

df = p.DataFrame({"Faiz": s1, "Dravi": s2, "Pari": s3})
print(type(df))
print(df)

#  loc behavioural attributes

a = df.loc['A']
print(a)

#  iloc behavioural attributes

print(df.iloc[1])
print(df.iloc[-1])
print('-----------')
print(df.iloc[:])
print('-----------')

print(df.iloc[2, 2])
print(df.iloc[:, 1])
print('---------------')
print(df.iloc[:, :])
print(df.iloc[-1, :])
print(df.iloc[:, 0:2])
print(df.iloc[[0, 2], :])
print('----------------')
print(df.iloc[:, :])
print(df.iloc[[0, 2], [0, 2, -1]])
print(df.iloc[0:1, 1:2])
print('--------------------------------')
# Note that .iloc returns a Pandas Series when only one row is selected,
# and a Pandas DataFrame when multiple rows are selected, or if any column in full is selected.
# To counter this, pass a single-valued list if you require DataFrame output.
# explained below

ex1 = df.iloc[1]
print(type(ex1))  # will be Series
print(ex1)
# To get ex1 as DataFrame

ex2 = df.iloc[[1]]
print(type(ex2))  # return as DataFrame
print(ex2)

print('---------------')
ex3 = df.iloc[0:1, 1:2]
print(type(ex3))  # return as DataFrame
print(ex3)

ex4 = df.iloc[0:2]
print(type(ex4))  # return as DataFrame
print(ex4)
