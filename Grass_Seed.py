r = float(input())
n = float(input())
z = []
for _ in range(int(n)):
    (x, y) = input().split()
    z.append(float(x)*float(y))
print(round(sum(z)*r, 6))


