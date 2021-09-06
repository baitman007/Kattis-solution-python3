def p(x):
    a = set()
    x = x.lower()
    for char in x:
        if char != ' ':
            a.add(char)
    if len(a) < 26:
        return 'not panorama'
    return 'pangram'


print(p(input()))
