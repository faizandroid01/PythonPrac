import pandas as p

t1 = p.DataFrame(
    {"faiz": p.Series([1, 2, 3], index=['A', 'B', 'C']),
     "dravi": p.Series([10, 20, 30], index=['A', 'B', 'C']),
     "pari": p.Series([100, 200, 300], index=['A', 'B', 'C']),
     "hima": p.Series([1000, 2000, 3000], index=['A', 'B', 'C'])
     })

print(t1)
print('--------------')

print(t1.pop('dravi'))
# to get any row info in table

# a = t1.get('hima')


















