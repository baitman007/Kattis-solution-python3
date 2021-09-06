
a,b = map(int,input().split())

if a==b:
    print(a+1)
else:
    pro = abs(a-b)+1
    start = min(a,b)+1
    for i in range(start,start+pro):
        print(i)