n = int(input())
l = []
for _ in range(int(n)):
    z = list(map(int, input().split()))
    l.append(z)
for i in range(n):
    if l[i][0] > (l[i][1] -l[i][2]):
        print('do not advertise')
    elif l[i][0] == (l[i][1] -l[i][2]):
        print("does not matter")
    else:
        print('advertise')
