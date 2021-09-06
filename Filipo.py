z = []
(x, y) = map(int, input().split())
Reverse = 0
Revers = 0
while x > 0:
    Reminder = x % 10
    Reverse = (Reverse *10) + Reminder
    x = x // 10
while y > 0:
    Reminder = y % 10
    Revers = (Revers *10) + Reminder
    y = y // 10

z.append(max(int(Reverse), int(Revers)))
print(str(z[0]))
