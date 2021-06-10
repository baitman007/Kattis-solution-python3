(n, k) = map(int, input().split())
l = []
for _ in range(k):
    z = int(input())
    l.append(z)
print(float((sum(l)+(-3*(n-k)))/n), float((sum(l)+(3*(n-k)))/n))
