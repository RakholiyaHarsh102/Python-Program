numbers = [-1, 2, -3, 4, 5, 5, 6, 10]
print("The list is:", numbers)

# Get unique numbers by converting the list to a set, then back to a sorted list (optional for order).
unique_numbers = list(set(numbers))

numbers = [-1,2,-3,4,5,5,6,10]
print("the list is : " ,numbers)

if unique_numbers:  
    largest_number = unique_numbers[0]
    smallest_number = unique_numbers[0]
    
    for num in unique_numbers:
        if num > largest_number:
            largest_number = num
        if num < smallest_number:
            smallest_number = num
            
    print("Largest number:", largest_number)
    print("Smallest number:", smallest_number)
else:
    print("The list is empty, cannot find largest or smallest numbers.")