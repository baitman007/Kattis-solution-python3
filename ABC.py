a, b, c = sorted(list(map(int, input().split())))
TEXT = input()
result = []
for i in TEXT:
    if i == 'A':
        result.append(a)
    elif i == 'B':
        result.append(b)
    else:
        result.append(c)

print(" ".join(map(str, result)))