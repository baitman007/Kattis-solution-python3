(n_parts, c) = input().split()
n_parts = int(n_parts)
c = int(c)
p = set()
res = -1
for i in range(1, c + 1):
    part = input()
    p.add(part)
    if len(p) == n_parts and res == -1:
        res = i
if len(p) < n_parts:
    print('paradox avoided')
else:
    print(res)
