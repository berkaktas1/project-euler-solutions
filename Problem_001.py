x = 1000
v = 1
z = 0
while x-1 > v:
    v += 1
    if v % 3 == 0 or v % 5 == 0:
        z = z + v
print(z)