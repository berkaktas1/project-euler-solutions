def main():
    x = int(input("Enter a Number: "))
    primes_list = []
    c = 2 
    while len(primes_list) < x:
        is_prime = True
        for a in range(2, int(c ** 0.5) + 1): 
            if c % a == 0:
                is_prime = False
                break
        if is_prime:
            primes_list.append(c) 
        c += 1     
    print(primes_list)
main()