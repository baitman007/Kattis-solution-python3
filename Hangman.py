n = input()
m = input()
c , res = 10,0
for i in m:
    if i not in n:
        c -= 1
    else:
        res += 1
    if res == len(set(n)):
        print('WIN')
        break
    if c == 0:
        print('LOSE')
        break