no=int(input("enter number  : "))
temp=no
total=0
length=len(str(no))
while(no>0):
    rem=no%10
    total+=rem**length
    no//=10
if(temp==total):
    print("number is armstrong")
else:
    print("number is not armstrong")
