numbers = [-1, 2, -3, 4, 5, 5, 6, 10]
print("The list is:", numbers)

# Remove duplicates to get unique numbers
unique_numbers = list(set(numbers))

if unique_numbers: 
    product = 1
    for num in unique_numbers:
        product *= num
    print("Product of all unique items in the list:", product)
else:
    print("The list is empty, cannot multiply items.")