x = int(input())
z = list(input().split())
l = []
for i in range(len(z)):
    if int(z[i]) >= 0:
        l.append(int(z[i]))
print(sum(l) / len(l))
