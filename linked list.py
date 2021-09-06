x = input()
y = []
if x != 0:
    for i in range(int(x)):
        z = input()
        y.append(z)
    k = y[::-1]
    for i in range(len(k)):
        print(k[i])
