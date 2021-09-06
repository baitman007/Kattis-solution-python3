n = int(input())
z = []
for _ in range(n):
    z.append(int(input()))
k = sum(z)-(n-1)
print(k)
