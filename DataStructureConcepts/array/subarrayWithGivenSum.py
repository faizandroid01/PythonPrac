class Main:
    tc = int(input())
    tcl = []
    n_sl = []
    for i in range(tc):
        n_s = input()
        n_sl = n_s.split(' ')
        arr = input()
        tcl.append([arr.split(' '), int(n_sl[0]), int(n_sl[1])])

    for i in tcl:
        a, no, sum = i[0], i[1], i[2]
        for j in range(len(a)):
            si, ei, i_s, k = j + 1, 0, 0, j
            while k < len(a):
                i_s = i_s + int(a[k])
                if i_s == sum:
                    print(si, k + 1)
                    break
                elif j == len(a) - 1:
                    print(-1)
                    break
                k += 1
