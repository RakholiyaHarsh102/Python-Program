no1=int(input("enter first number : "))
no2=int(input("enter second number : "))
max1=max(no1,no2)
while True:
    if max1%no1==0 and max1%no2==0:
        print("LCM of {} and {} is {} ".format(no1,no2,max1))
        break
    max1+=1