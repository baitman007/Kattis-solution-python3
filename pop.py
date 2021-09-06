x = input()
y = []
z = 0
if x != 0:
    for i in range(int(x)):
        z = int(input())
        y.append(z)
k=y[::-1]
f=[]
for j in range(3):
    if int(k[j]) % 2 == 0:
        f.append(int(k[j]))
print(sum(f))

