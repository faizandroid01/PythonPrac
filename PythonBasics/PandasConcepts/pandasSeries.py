import pandas as p

# Empty series
series = p.Series()
print(series)

# 1D Array
s = p.Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])
print(s)

# dict as input for series keys will be then index of series
s1 = p.Series({'a': 15, 'b': 56, 'c': 89})
print(s1)

# slicing series
print(s1[:2])
