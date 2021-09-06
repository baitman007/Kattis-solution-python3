n = int(input())
z = []
for _ in range(n):
    k = list(map(int, input().split()))
    z.append(k)
for i in range(len(z)):
    w = []
    total = z[i][0] * 8
    n1 = z[i][1]
    n5 = z[i][2]
    n10 = z[i][3]
    for j in range(1, n10 + 1):
        if total >= n10 * 10:
            w.append(1)
            total = total - n10 * 10
            print(w)
        for k in range(1, n5 + 1):
            if total >= n5 * 5:
                w.append(1)
                total = total - n5 * 5
                print(w)
            for l in range(1, n1 + 1):
                if total >= n1 * 1:
                    w.append(1)
                    total = total - n1 * 1
                    print(w)
print(sum(w))
