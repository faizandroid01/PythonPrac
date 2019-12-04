import pandas as p

# DataFrame Creation
s1 = p.Series(['faiz', 'dravi', 'dishu', 'pari'], index=[0, 1, 2, 3])
s2 = p.Series(['ahmed', 'jain', 'jain', 'mamgain'], index=[0, 1, 2, 3])
s3 = p.Series([23, 23, 22.5, 23.5], index=[0, 1, 2, 3])

df = p.DataFrame({'FirstName': s1, 'LastName': s2, 'Age': s3})
print(df)

# Applying loc knowledge
print(df.get('Age'))  # For Column dtype : float64
print(df.iloc[2])  # For rows dtype : object

# Append a new row to existing df

# one row at a time
row = p.DataFrame([['priya', 'sharma', 35]], columns=['FirstName', 'LastName', 'Age'])
df = df.append(row)
print(df)
print('---------------')

# multiple row at a time
row = p.DataFrame([['ragini', 'sharma', 24], ['mahi', 'bagi', 23.2]], columns=['FirstName', 'LastName', 'Age'])
df = df.append(row)
print(df)

print('------_DELETE---------')
#  DELETE OR DROP ROWS

df = df.drop(0)  # all 0th index value would be dropped
print(df)
