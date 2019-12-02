import pandas as p

''' 
Add And Sub DataFrame is possible only when data is added in series
Extra index added later is not a valid index .
'''

# ADD
s1 = p.Series([1, 2, 3], index=['b', 'c', 'd'])
s2 = p.Series([10, 20, 30], index=['b', 'c', 'd'])

t = p.DataFrame({'Faiz': s1, 'Dravi': s2})
print(t)

# add into above t (other than prev indexes wont be considered)
t['Pari'] = p.Series([36, 24, 36, 56], index=['b', 'c', 'd', 'a'])
print(t)

# if in the starting it would have added , it would have taken that


# DEL


print(t.get('Pari'))
del (t['Pari'])
print(t)
