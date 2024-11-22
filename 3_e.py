str2=str(input("enter string to check string is palindrome or not : "))
rev=''
for char in str2:
    rev=char+rev
print("Reverse string  is : " ,rev)
if(rev==str2):
    print("Given string is palindrome")
else:
    print("Given string is no palindrome")
