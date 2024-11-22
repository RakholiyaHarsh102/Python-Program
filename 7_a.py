num1 = int(input("Enter starting number: "))
num2 = int(input("Enter ending number: "))
while (num1 <= num2):
    if( num1 > 1):  
        is_prime = True
        for i in range(2, num1):
            if num1 % i == 0:
                is_prime = False
                break
        if(is_prime):
            print( num1)
    num1 += 1