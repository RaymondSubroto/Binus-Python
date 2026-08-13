age = int(input("Input your age = "))
if ( age >= 0 and age <= 1 ):
    print("Baby")
elif ( age >= 2 and age <= 3 ):
    print("Toddler")
elif ( age >= 4 and age <= 5 ):
    print("Preeschooler")
elif ( age >= 6 and age <= 12 ):
    print("Child")
elif ( age >= 13 and age <= 17 ):
    print("Teenager")
elif ( age >= 18 and age <= 21 ):
    print("Young Adult")
elif ( age >= 22 and age <= 30 ):
    print("Pre-adult")
elif ( age >= 31 and age <= 50 ):
    print("Adult")
elif ( age >= 51 and age <= 70 ):
    print("Pre-elderly")
else:
    print("Elderly")