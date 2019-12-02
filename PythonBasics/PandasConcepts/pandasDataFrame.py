import pandas as p

list = [1, 2, 3, 4, 5, 6]
table = p.DataFrame(list)
print(table)

# mulitple map -- takes list only as input (inside can be anything)
dict = {'a': 100, 'b': 25, 'c': 456, 'd': 890, 'e': 999}
t1 = p.DataFrame([dict, dict, dict])
print(t1)

#  uneven values in dict
t2 = p.DataFrame([{'a': 00, 'b': 10}, {'a': 100, 'b': 200, 'c': 3}])
print(t2)

# custom index in form of list

t3 = p.DataFrame([{'a': 00, 'b': 10}, {'a': 100, 'b': 200, 'c': 3}], index=['row-1', 'row-2'])
print(t3)

# series as constituent of dataFrame
s3 = p.Series([30, 40, 45], index=['Maths', 'Bio', 'Chem'])
s4 = p.Series([25, 45, 50, 60], index=['Maths', 'Bio', 'Chem', 'Phy'])
t4 = p.DataFrame({'Jim': s3, 'Dwight': s4})
print(t4)

