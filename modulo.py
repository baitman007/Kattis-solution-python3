z = []
l = []
for _ in range(10):
    z.append(int(input()))
k = []
for i in range(len(z)):
    y = z[i] % 42
    k.append(int(y))
k = set(k)
print(len(k))
