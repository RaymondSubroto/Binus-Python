#void function
def namadanasal():
    print("=-=-=-=-=-=-=-=-=-=-=-=")
    print("Raymond Kenzie Subroto")
    print("        Jakarta       ")
    print("=-=-=-=-=-=-=-=-=-=-=-=")
namadanasal()

#rumus
def pertambahan(angka1: int, angka2: int) -> int:
    return angka1 + angka2

def pengurangan(angka1: int, angka2: int) -> int:
    return angka1 - angka2

def pembagian(angka1: int, angka2: int) -> int:
    return angka1 / angka2

def perkalian(angka1: int, angka2: int) -> int:
    return angka1 * angka2

def modulus(angka1: int, angka2: int) -> int:
    return angka1 % angka2

#eksekusi
while(True):
    command = input("Enter Menu (+|-|/|*|%|stop): ")

    if command == "+":
        v1 = float(input("Enter Value 1: "))
        v2 = float(input("Enter Value 2: "))
        print(pertambahan(v1, v2))
    
    elif command == "-":
        v1 = float(input("Enter Value 1: "))
        v2 = float(input("Enter Value 2: "))
        print(pengurangan(v1, v2))

    elif command == "/":
        v1 = float(input("Enter Value 1: "))
        v2 = float(input("Enter Value 2: "))
        print(pembagian(v1, v2))

    elif command == "*":
        v1 = float(input("Enter Value 1: "))
        v2 = float(input("Enter Value 2: "))
        print(perkalian(v1, v2))

    elif command == "%":
        v1 = float(input("Enter Value 1: "))
        v2 = float(input("Enter Value 2: "))
        print(modulus(v1, v2))

    elif command == "stop":
        print("Program stopped. Thank you for using my program.")
        break

    else:
        print("Error. Try again.")