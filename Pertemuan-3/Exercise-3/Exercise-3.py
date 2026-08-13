while True:
    suhu = input("Suhu awal celcius? (Celcius/Fahrenheit/Kelvin) ")
    if suhu == "Celcius":
        celcius1 = int(input("Input Celcius = "))

        konversi1 = input("Konversi ke? (Fahrenheit/Kelvin) ")
        if konversi1 == "Fahrenheit":
            fahrenheit1 = print(("Fahrenheit ="), (celcius1 * 9/5) + 32)
            break
        elif konversi1 == "Kelvin":
            kelvin1 = print(("Kelvin ="), celcius1 + 273)
            break
        else:
            break

    elif suhu == "Fahrenheit":
        fahrenheit2 = int(input("Input Fahrenheit = "))

        konversi2 = input("Konversi ke? (Celcius/Kelvin) ")
        if konversi2 == "Celcius":
            celcius2 = print(("Celcius ="), (fahrenheit2 - 32) * 5/9)
            break
        elif konversi2 == "Kelvin":
            kelvin2 = print(("Kelvin = "), (fahrenheit2 - 32) * 5/9 + 273)
            break
        else:
            break

    elif suhu == "Kelvin":
        kelvin3 = int(input("Input Kelvin = "))
        
        konversi3 = input("Konversi ke? (Celcius/Fahrenheit) ")
        if konversi3 == "Celcius":
            celcius3 = print(("Celcius ="), kelvin3 - 273)
            break
        elif konversi3 == "Fahrenheit":
            fahrenheit3 = print(("Fahrenheit ="), (kelvin3 - 273) * 9/5 + 32)
            break
        else:
            break