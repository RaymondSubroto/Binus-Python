a = int(input("Masukkan nilai = "))
x = ""
for i in range(int(a),0,-1):
    for a in range(i):
        x = x + str(i)
    print(x)
    x = ""