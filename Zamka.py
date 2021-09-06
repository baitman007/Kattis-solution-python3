l = []
index = 0
while index < 3:
    line = input()
    l.append(int(line))
    index += 1


def sum_digits(n):
    total = 0
    for i in str(n):
        total += int(i)

    return total


N = l[0]
while N <= l[1]:
    if sum_digits(N) == l[2]:
        break
    N += 1

M = l[1]
while M >= l[0]:
    if sum_digits(M) == l[2]:
        break
    M -= 1

print(N)
print(M)
