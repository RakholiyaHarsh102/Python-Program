no1=int(input("enter first number : "))
no2=int(input("enter second number : "))
no3=int(input("enter three number : "))

#printing maximum number
if(no1>no2 and no1>no3):
    print("no1 is maximum")
elif(no2>no1 and no2>no3):
    print("no2 is maximum")
else:
    print("no3 is maximum")

#priniting minimum number
if(no1<no2 and no1<no3):
    print("no1 is minimum")
elif(no2<no1 and no2<no3):
    print("no2 is minimum")
else:
    print("no3 is minimum")