n = int(input())
z = []
for _ in range(n):
    z.append(input().split())
for i in range(len(z)):
    if z[i][0] == 'Simon' and z[i][1] == 'says':
        del z[i][0]
        del z[i][0]
        l = z[i]
        print(*l, sep = ' ')
        l = []
