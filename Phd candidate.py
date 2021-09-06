n=int(input())
y=[]
for _ in range(n):
    x=list(input().split('+'))
    y.append(x)
for i in range(len(y)):
    if y[i][0] != 'P=NP':
        print(int(y[i][0])+int(y[i][1]))
    else:
        print('skipped')