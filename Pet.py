a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
e = list(map(int, input().split()))
l = [sum(a), sum(b), sum(c), sum(d), sum(e)]
print(l.index(max(l))+1, max(l))
