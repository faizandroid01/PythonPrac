tc = int(input())
tcl = []
for i in range(tc):
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    tcl.append([arr, n, s])

for i in tcl:
    a, sum, flag = i[0], i[2], 0

    for j in range(len(a)):
        si, ei, i_s, k = j + 1, 0, 0, j
        if flag == 1:
            break
        while k < len(a):
            i_s = i_s + a[k]
            if i_s == sum:
                print(si, k + 1)
                flag = 1
                break
            elif j == len(a) - 1:
                print(-1)
                flag = 1
                break

            k += 1
