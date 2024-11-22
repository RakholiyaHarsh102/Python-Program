numbers = [-1,2,-3,4,5,5,6,10]
print("the list is : " ,numbers)

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("\nList after removing duplicates:", unique_numbers)


