n = int(input())
z = list(map(int, input().split()))
for i in range(len(z)):
    if 1 <= n <= 10e5 and n == len(z) and 10e9 > z[i] >= 0:
     print(z.index(min(z)))
     break

