n = int(input())
z = list(map(int, input().split()))
res = []
for i in range(len(z)):
    if z[i] <0:
      res.append(z[i])
if len(res) == 0:
    print('0')
else:
    print(len(res))

