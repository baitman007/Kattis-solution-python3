x = int(input())
n = int(input())
l = []
for i in range(n):
    z = int(input())
    l.append(z)
k = sum(l)
q = x * n
s = q - k
print(s + x)
