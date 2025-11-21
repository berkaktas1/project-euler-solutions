def main():
    toplam_kare = 0
    kareler_toplam = 0
    x = int(input("enter a number: "))
    for i in range(1,x+1):
        toplam_kare += i 
        kareler_toplam += i**2
    temp = toplam_kare**2 - kareler_toplam
    print(temp)
main()