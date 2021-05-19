import random

name = "Enrique"
surname = "Alemany"

names = ["enal986"]

uname = ((name[0:2])+(surname[0:2])+str(random.randint(0, 999))).lower()
while uname in names:
    uname =((name[0:2])+(surname[0:2])+str(random.randint(0, 999)))

names.append(uname)
print(names)


print (uname)