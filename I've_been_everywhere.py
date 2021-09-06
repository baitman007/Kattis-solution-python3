t = int(input())
res = ""
for _ in range(t):
    count = int(input())
    cities = set()
    for _ in range(count):
        city = input()
        cities.add(city)
    res = res + str(len(cities)) + "\n"
print(res.rstrip("\n"))
