a = int(input("Masukkan nilai = "))
x = ""
for i in range(int(a),0,-1):
    for b in range(i):
        x = x + str(i)
    print(x)
    x = ""

for i in range(2,int(a)+1):
    for b in range(i):
        x = x + str(i)
    print(x)
    x = ""