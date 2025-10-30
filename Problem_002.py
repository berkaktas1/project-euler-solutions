z = 0
v = 1
sum = 0
while z < 4000000:
    c = z + v
    z = v
    v = c
    if z % 2 == 0:
        sum += z
        print(sum)