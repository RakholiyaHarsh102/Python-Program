a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

print("Before swapping:")
print("a =", a)
print("b =", b)

a = a + b
b = a - b
a = a - b  
print("After swapping:")
print("a =", a)
print("b =", b)