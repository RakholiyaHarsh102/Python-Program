dict1={"name":"Harsh","age":23,"div":"B"}
print("Dictionary is : ",dict1)


key2=input("enter key you want to remove in dictionary : ")
if key2 in dict1.keys():
    del dict1[key2]
else:
    print("your key not exist please reconfirm !!")
print("After removing Dictionary is : ",dict1)
