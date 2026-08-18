while(True):
    number = int(input("Masukkan angka = "))
    if number %2 == 0:
        print("Angka genap")
    else:
        print("Angka ganjil")
    x = input("Apakah mau ulang? (Y/N) ")
    if x == "Y":
        continue
    else:
        print("Program berhenti.")
        print("Terimakasih sudah menggunakan.")
        break