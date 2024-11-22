no=int(input("enter a number : " ))
for row in range(no):
    for col in range(row,no):
        print(end=' ')
    for col in range(row):
        print("*",end=' ')
    for col in range(row+1):
        print("*",end=' ')
    print()