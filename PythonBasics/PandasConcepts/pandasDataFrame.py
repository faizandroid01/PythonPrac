import pandas as p

list = [1, 2, 3, 4, 5, 6]
table = p.DataFrame(list)
print(table)

#
dict = {'a': 100, 'b': 25, 'c': 456, 'd': 890, 'e': 999}
t1 = p.DataFrame([dict])
print(t1)
