def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return (a * b) // get_gcd(a, b)

result = 1
for i in range(1, 21):
    result = get_lcm(result, i)

print(f"Smallest positive number evenly divisible by all numbers from 1 to 20: {result}")