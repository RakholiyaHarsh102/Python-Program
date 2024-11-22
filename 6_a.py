dict1={"name":"dhyey","age":21,"div":"A"}
print("Dictionary is : ",dict1)


key1=input("enter key you want to search in dictionary : ")
if key1 in dict1.keys():
    print("your key already exist!")
else:
    print("your key not exist!!")