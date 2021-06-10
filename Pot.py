n = int(input())
z = []
a = str()
for _ in range(n):
    l = []
    l = list(map(str, input()))
    if len(l) % 2 == 0:
        a=""
        for i in range(0, len(l) - 1, 2):
            a = a + l[i] + l[i + 1]
        a = a[:len(a) - 1]
    else:
        a=""
        for i in range(0, len(l) - 1, 2):
            a = a + l[i] + l[i + 1]
    b = l[len(l) - 1]
    k = int(a) ** int(b)
    z.append(k)
print(sum(z))
