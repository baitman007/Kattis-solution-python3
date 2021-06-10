n = int(input())
p = []
for _ in range(n):
    p.append(input())
if p == sorted(p):
    print("INCREASING")
elif p == sorted(p)[::-1]:
    print("DECREASING")
else:
    print("NEITHER")