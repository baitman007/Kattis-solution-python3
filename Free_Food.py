n = int(input())
days = set()
for i in range(n):

    a, b = list(map(int, input().split()))
    for j in range(a, b + 1):
        days.add(j)

print(len(days))