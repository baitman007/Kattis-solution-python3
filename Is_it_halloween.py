import sys
month = " "
date = 0
for i in sys.stdin:
    dt = i.split(" ")
    month = dt[0]
    date = (int)(dt[1])
    break

if (month == "OCT" and date == 31) or (month == "DEC" and date == 25):
    print("yup")
else:
    print("nope")
