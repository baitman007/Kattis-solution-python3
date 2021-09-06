if __name__ == '__main__':
    s = input()
z=0
w=0
y=0
x=0
q=0
for i in range(len(s)):
 if any(i.isalnum() for i in s):
     w=1
for i in range(len(s)):
 if any(i.isdigit() for i in s):
     z=1
for i in range(len(s)):
 if any(i.isalpha() for i in s):
     q=1
for i in range(len(s)):
 if any(i.isupper() for i in s):
     x=1
for i in range(len(s)):
 if any(i.islower() for i in s):
     y=1
if w==1:
    print("True")
else:
    print("False")
if q==1:
    print("True")
else:
    print("False")
if z==1:
    print("True")
else:
    print("False")

if y==1:
    print("True")
else:
    print("False")
if x==1:
    print("True")
else:
    print("False")
s