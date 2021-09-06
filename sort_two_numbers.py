a = list(input().split())
k=[]
for i in range(len(a)):
    k.append(int(a[i]))
k = sorted(k)
for j in range(len(k)):
 print(k[j], end=' ')
