c = input()
r = "PER"
r_index = 0
count = 0
for i in range(len(c)):
    if c[i] != r[r_index]:
        count += 1
    r_index = (r_index + 1) % 3
print(count)