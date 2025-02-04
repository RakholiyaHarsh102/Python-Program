#Odd End Even Number
try:
    number = int(input("Enter Number:::"))
    if number % 2 == 0:
        print("f{number}  is Even Number...")
    else:
        print(f"{number} Odd Number..")

except ValueError:
    print("Invalid Input...")
