e = int(input("Enter the number of digits: "))
x_first = 10**e
x_second = 10**(e-1)
z = 0
c = "a"
reverse_c = "b"
list_palindromes = []
for i in range(x_second , x_first):
    for b in range(x_second , x_first):
        z = i * b
        c = str(z)
        reverse_c =  c[::-1]
        if c == reverse_c:
            list_palindromes.append(z)
biggest_one = max(list_palindromes)
print(f"Largest Palindrome Product: {biggest_one}")
