w = set()
r = False
z = input().split()
for i in z:
    if i in w:
        print("no")
        r = True
        break
    w.add(i)
if not r:
    print("yes")
