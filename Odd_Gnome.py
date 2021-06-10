def Pos(g):
    for i in range(1, len(g)):
        if g[i] != g[i - 1] + 1:
            return i + 1


res = []
for _ in range(int(input())):
    gnomes = list(map(int, input().split()))[1:]
    res.append(Pos(gnomes))

for a in res:
    print(a)
