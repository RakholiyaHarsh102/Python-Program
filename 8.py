str1 = input("Enter the main string: ")
substr = input("Enter the substring you want to find in the main string: ")
if substr in str1:
    print(f"The substring '{substr}' exists in the main string.")
else:
    print(f"The substring '{substr}' does not exist in the main string.")