y = int(input("Enter a number: "))
temp_y = y  
c = 2
list_of_prime_factors = []

if y <= 1:
    pass
    
elif y == 2:
    list_of_prime_factors.append(2)

else:

    while temp_y % c == 0:
        list_of_prime_factors.append(c)
        temp_y //= c  
        
    c = 3
   
    while c * c <= temp_y: 
        while temp_y % c == 0:
            list_of_prime_factors.append(c)
            temp_y //= c
        c += 2 

    if temp_y > 2:
        list_of_prime_factors.append(temp_y)

print(f" prime factors of {y} : {list_of_prime_factors}")