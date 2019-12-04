# conversion of any char to ascii
# param should be str
print('conversion of any char to ascii')

listOfChars = [' ', 'a', 'A', '1']

for i in listOfChars:
    print('Ascii Val of :' + i + ' is ' + str(ord(i)))


# conversion of ascii to str
# param should be valid int
print('conversion of ascii to str \n --------------')

listOfInts = [32, 97, 65, 49]

for i in listOfInts:
    print('Char Val for ascii val :' + str(i) + ' is ' + chr(i))
