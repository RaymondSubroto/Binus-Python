while(True):
    print("Tes Bentuk Segitiga")
    a = int(input("Input Sisi a = "))
    b = int(input("Input Sisi b = "))
    c = int(input("Input Sisi c = "))

    if a + b <= c or a + c <= b or b + c <= a:
        print("Bukan segitiga.")
    
    #Sama sisi
    elif a == b and a == c and b == c:
        print ("Segitiga sama sisi.")

    #Sama kaki
    elif a == b or a == c or b == c:
        print("Segitiga sama kaki.")

    elif a**2 + b**2 == c**2:
        print("Segitiga siku-siku.")

    #Semua sisi beda
    elif a != b and a != c and b != c:
        print("Segitiga sembarang.")

    else:
        print("error.")
        break

    x = input("Apakah mau ulang? (Y/N) ")
    if x == "Y":
        continue
    else:
        print("Program berhenti.")
        print("Terimakasih sudah menggunakan.")
        break

