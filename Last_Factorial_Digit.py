n = int(input())
z = []
factorial=1
for _ in range(n):
    x = int(input())
    z.append(x)
for j in range(len(z)):
    num = z[j]
    for i in range(1, num + 1):
        factorial = factorial * i
print(factorial)