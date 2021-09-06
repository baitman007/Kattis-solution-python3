s = input()
res = s[0]
for i in range(1, len(s)):
    if s[i] == res[-1]:
        continue
    res += s[i]
print(res)
