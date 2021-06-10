n = int(input())
for _ in range(n):
    b, p = list(map(float, input().split()))

    bpm = 60 * b / p
    min = bpm - (60 / p)
    max = bpm + (60 / p)

    print(min,bpm, max)