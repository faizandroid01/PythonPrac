def getMaxContiguos(b):
    c = []
    i = 0

    while i <= (len(b) - 4):
        c.append(b[i:(i + 4)])
        i += 1

    d = ()
    for i in c:
        d = d + (i.__getitem__(0),)

    max_item = max(d)

    for item in c:
        if item.__getitem__(0) == max_item:
            print(str(item))
            break
            

# Driver code
if __name__ == '__main__':
    a = [1, 3, 5, 9, 10, 8, 7, 10]
    getMaxContiguos(a)
