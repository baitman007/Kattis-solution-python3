def s():
    n = int(input())
    s = map(int, input().split(" "))

    res, q = 0, 1

    x, y = 2 ** (-3 / 4), 2 ** (-5 / 4)

    for i in s:
        res += q * x

        temp = y
        y = x
        x = temp

        y /= 2

        q = q * 2 - i

        if (q <= 0):
            print(res)
            return

    print("impossible")

s()