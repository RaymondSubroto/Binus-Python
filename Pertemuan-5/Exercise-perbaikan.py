#void function
def namadanasal():
    print("=-=-=-=-=-=-=-=-=-=-=-=")
    print("Raymond Kenzie Subroto")
    print("        Jakarta       ")
    print("=-=-=-=-=-=-=-=-=-=-=-=")
namadanasal()

#rumus
def pertambahan(angka1: float = 5.0, angka2: float = 2.0) -> float:
    return angka1 + angka2
#print(pertambahan())

def pengurangan(angka1: float = 5.0, angka2: float = 2.0) -> float:
    return angka1 - angka2
#print(pengurangan())

def pembagian(angka1: float = 5.0, angka2: float = 2.0) -> float:
    return angka1 / angka2
#print(pembagian())

def perkalian(angka1: float = 5.0, angka2: float = 2.0) -> float:
    return angka1 * angka2
#print(perkalian())

def modulus(angka1: float = 5.0, angka2: float = 2.0) -> float:
    return angka1 % angka2
#print(modulus())

#eksekusi
while(True):
    command = input("Enter Menu (+|-|/|*|%|stop): ")

    if command == "+":
        question = input("Default/Manual? (D/M): ").upper()
        if question == "D":
            print("The default result of addition 5 + 2 is", pertambahan())
        elif question == "M":
            v1 = float(input("Enter Value 1: "))
            v2 = float(input("Enter Value 2: "))
            print("The result of addition", v1, "+", v2, "is", pertambahan(v1, v2))
        else:
            print("Error. Try Again. ")

    elif command == "-":
        question = input("Default/Manual? (D/M): ").upper()
        if question == "D":
            print("The default result of subtraction 5 - 2 is", pengurangan())
        elif question == "M":
            v1 = float(input("Enter Value 1: "))
            v2 = float(input("Enter Value 2: "))
            print("The result of subtraction", v1, "-", v2, "is", pengurangan(v1, v2))
        else:
            print("Error. Try Again. ")

    elif command == "/":
        question = input("Default/Manual? (D/M): ").upper()
        if question == "D":
            print("The default result of division 5 / 2 is", pembagian())
        elif question == "M":
            v1 = float(input("Enter Value 1: "))
            v2 = float(input("Enter Value 2: "))
            print("The result of division", v1, "/", v2, "is", pembagian(v1, v2))
        else:
            print("Error. Try Again. ")

    elif command == "*":
        question = input("Default/Manual? (D/M): ").upper()
        if question == "D":
            print("The default result of multiplication 5 * 2 is", perkalian())
        elif question == "M":
            v1 = float(input("Enter Value 1: "))
            v2 = float(input("Enter Value 2: "))
            print("The result of multiplication", v1, "*", v2, "is", perkalian(v1, v2))
        else:
            print("Error. Try Again. ")

    elif command == "%":
        question = input("Default/Manual? (D/M): ").upper()
        if question == "D":
            print("The default result of modulus 5 % 2 is", modulus())
        elif question == "M":
            v1 = float(input("Enter Value 1: "))
            v2 = float(input("Enter Value 2: "))
            print("The result of modulus", v1, "%", v2, "is", modulus(v1, v2))
        else:
            print("Error. Try Again. ")

    elif command == "stop":
        print("Program stopped. Thank you for using my program.")
        break

    else:
        print("Error. Try again.")