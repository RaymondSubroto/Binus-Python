import math
while True:
    print("Menghitung Nilai Diskriminan")
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

    if a == 0:
        print("Bukan fungsi kuadrat.")
        break

    print(f"f(x) = {a}x^2 + {b}x + {c}")

    D = b ** 2 - 4*a*c

    print("Nilai Diskriminan =", D)

    if D > 0:
        print("Garis memotong kurva")

        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)

        print(("x1 ="), x1)
        print(("x2 ="), x2)
        break

    elif D == 0:
        print("Garis menyinggung kurva")

        x = -b / (2 * a)
        print(("x ="), x)
        break

    else:
        print("Garis tidak memotong dan tidak menyinggung kurva.")

        print("x1 = (-b + math.sqrt(D)) / (2 * a)")
        print("x2 = (-b - math.sqrt(D)) / (2 * a)")
        break





