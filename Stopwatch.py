n = sorted([int(input()) for _ in range(int(input()))])
if len(n) % 2 == 0:
    t = 0
    for i in range(0, len(n), 2):
        t = n(i) - n[i + 1]
    print(t)
else:
    print("still running")
