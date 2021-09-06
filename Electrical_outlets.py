n = int(input())
z = []
for _ in range(n):
    z.append(input().split())
res =[]
for i in range(len(z)):
    k = z[i]
    k = [int(f) for f in k]
    s = int(sum(k)) - int(z[i][0]) - int(z[i][0]) + 1
    res.append(s)
for j in range(len(res)):
    print(res[j])
