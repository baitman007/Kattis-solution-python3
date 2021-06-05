def more(v):
    if v > 1:
        z = "Dr. Chaz needs " + str(v) + " more pieces of chicken!"
    else:
        z = "Dr. Chaz needs " + str(v) + " more piece of chicken!"
    print(z)


def less(value):
    if value > 1:
        z = "Dr. Chaz will have " + str(value) + " pieces of chicken left over!"
    else:
        z = "Dr. Chaz will have " + str(value) + " piece of chicken left over!"
    print(z)


(m, n) = input().split()
m = int(m)
n = int(n)
if m > n & n != m & m >= 0 & m <= 1000 & n >= 0 & n <= 1000:
    more(m - n)
elif n > m & m >= 0 & m <= 1000 & n >= 0 & n <= 1000 :
    less(n - m)
