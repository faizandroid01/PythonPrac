import numpy as np

arr = np.array([[1, 2], [3, 4]])
print(arr)

np.savetxt('playwithexcel.csv', arr, delimiter=',')

a = np.genfromtxt('playwithexcel.csv', delimiter=',')
print(a)