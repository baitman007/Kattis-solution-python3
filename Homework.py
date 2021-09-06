import re
data = input()
k = []
e = []
x = data.replace(';', ' ').split()
for i in range(len(x)):
    l = []
    z = x[i]
    l = z.replace('-', ' ').split()
    k.append(l)
for j in range(int(len(k))):
    f = []
    f.append(k[j])
    if int(len(f[0])) > 1:
        for g in range(int(k[j][0]), int(k[j][1])+1):
            e.append(g)
    else:
        y= int(f[0][0])
        e.append(y)
print(len(e))


