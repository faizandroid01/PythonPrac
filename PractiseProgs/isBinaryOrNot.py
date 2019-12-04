val = input('Enter a val to be checked for binary .')
flag = 'is Binary'
for char in val:
    if ord(char) not in range(48, 50):
        flag = 'is Not Binary'

print(flag)
