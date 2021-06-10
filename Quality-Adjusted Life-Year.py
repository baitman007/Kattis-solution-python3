n = int(input())
x = []
for i in range(n):
    q, y = map(float, input().split())
    x.append(q * y)
print(format(sum(x), '.3f'))
