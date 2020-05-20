def insertionSort(a):
    for i in range(len(a)-1):
        j = i + 1
        key = a[j]

        while j > 0:
            if a[j] < a[j - 1]:
                a[j] = a[j - 1]
                a[j - 1] = key
            j -= 1
    return a


class Sample:
    a = insertionSort([15, 2, 14, 56, 11, 23])
    print(a)
