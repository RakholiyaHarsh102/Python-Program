numbers = [-1, 2, -3, 4, 5, 5, 6, 10]
unique_numbers = list(set(numbers))  # Remove duplicates

print("The list is:", numbers)

# Check if the unique list is empty or not
if len(unique_numbers) == 0:
    print("The unique list is empty")
else:
    print("The unique list is not empty")