import sys
l_battles = []
res = 0
c = 0
for i in sys.stdin:
    if i.strip() == "":
        break
    if c != 0:
        l_battles.append(i.strip())
    else:
        res = int(i)
        c += 1

for i in l_battles:
    if i.__contains__("CD"):
        res -= 1

print(res)
