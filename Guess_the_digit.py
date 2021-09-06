(m, n, p, q) = input().split()
flag = 0
if int(m) >= int(n) and int(m) > 0 and int(q) > 0 and int(p) > 0 and int(n) >= 0:
    if int(n) == 0:
        for i in range(10 ** (int(m) - 1), int(10 ** int(m))):
            z = list(str(i))
            s = ''
            for c in range(len(z)):
                s = s + z[c]
                a = ''
            for k in range(len(z)):
                a = a + z[k]
            a = a + p
            if int(a) * int(q) == int(s):
                print(s)
                flag = 1
                break
    else:
        for i in range(10 ** (int(m) - 1), int(10 ** int(m))):
            z = list(str(i))
            s = ''
            for c in range(len(z)):
                s = s + z[c]
            for j in range(int(n)):
                z[j] = '0'
                a = ''
            for k in range(len(z)):
                a = a + z[k]
            a = a + p
            if int(a) * int(q) == int(s):
                print(s)
                flag = 1
                break
if flag == 0 and int(m) >= int(n) and int(m) > 0 and int(q) > 0 and int(p) > 0 and int(n) >= 0:
    print("IMPOSSIBLE")
if int(m) < int(n) or int(m) <= 0 or int(q) <= 0 or int(p) <= 0 or int(n) < 0:
    print("IMPOSSIBLE")
