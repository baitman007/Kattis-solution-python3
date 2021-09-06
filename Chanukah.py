n = int(input())
f = []
res = []
for _ in range(n):
    x = list(map(int, input().split()))
    f.append(x)
for i in range(len(f)):
    k = int(f[i][1])
    q = ((k * (k + 1)) / 2) + k
    res.append(int(q))
for j in range(len(res)):
    print(j+1, res[j])
