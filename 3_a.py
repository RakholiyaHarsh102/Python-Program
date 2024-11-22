str1 = input("Enter a string: ")  # Prompt the user for input
vowel = "aeiouAEIOU"  # List of vowels
count_vowel = 0  # Counter for vowels

# Iterate through each character in the string
for char in str1:
    if char in vowel:  # Check if the character is a vowel
        count_vowel += 1

# Print the total count of vowels
print("Number of vowels in the string is:", count_vowel)