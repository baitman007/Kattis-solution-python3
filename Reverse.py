n = int(input())
z=[]
for _ in range(n):
    x = input()
    z.append(x)
q = z[::-1]
for i in range(len(z)):
 print(q[i])
