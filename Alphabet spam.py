n = list(input())
l = []
c = []
w = []
s = []
for i in range(len(n)):
    if n[i] == "_":
        w.append(n[i])
    if str(n[i]).islower():
        l.append(n[i])
    if str(n[i]).isupper():
        c.append(n[i])
    if not str(n[i]).isalpha() and n[i] != "_":
        s.append(n[i])
print(round(len(w) / len(n), 15))
print(round(len(l) / len(n), 15))
print(round(len(c) / len(n), 15))
print(round(len(s) / len(n), 15))
