n = int(input())
z = []
r = []
k = []
for _ in range(n):
    z.append(int(input()))
for i in range(len(z)):
    res = 1
    for j in range(1, z[i] + 1):
        res = res * j
    r.append(res)
print(r)
for l in range(len(r)):
    k.append(str(r[l]))
    print(k[l][-1])



