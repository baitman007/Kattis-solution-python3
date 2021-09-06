(x,y) = map(int, input().split())
z = x*y
k = int(round(z*0.85,0))
for i in range(k,z+1):
    if y-1 < i/x < y:
        print(i)
        break
    elif i/x == y:
        print(i)
        break
