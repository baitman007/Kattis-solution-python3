n = int(input())
res = ""
for i in range(n):
    num = int(input())
    if num % 2 == 0:
        newString = str(num) + " is even \n"
    else:
        newString = str(num) + " is odd \n"
    res += newString
print(res)
