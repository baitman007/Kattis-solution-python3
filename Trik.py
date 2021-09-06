n = list(input())
z = [1, 0, 0]
for i in range(len(n)):
    if n[i] == 'A':
        if z[0] == 1:
            z = [0, 1, 0]
        elif z[1] == 1:
            z = [1, 0, 0]

    if n[i] == 'B':
        if z[1] == 1:
            z = [0, 0, 1]
        elif z[2] == 1:
            z = [0, 1, 1]

    if n[i] == 'C':
        if z[0] == 1:
            z = [0, 0, 1]
        elif z[2] == 1:
            z = [1, 0, 0]
print(int(z.index(1))+1)