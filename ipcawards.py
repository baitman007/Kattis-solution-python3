n = int(input())
f = []
res = []
o = []
r = []
for _ in range(n):
    k = list(input().split())
    f.append(k)



def dup(f):
    for j in f:
        if type(j) == list:
            dup(j)
        else:
            o.append(j)
dup(f)
g = list(set(o))

for b in f:
    if b[0] in g:
        g.remove(b[0])
        res.append(b)
for d in range(12):
    print(*res[d], sep=' ')
