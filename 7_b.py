terms = int(input("Enter the number of terms: "))
a= 0
b=1

print("Fibonacci Series:")
for _ in range(terms):
    print(a, end=" ")
    a, b = b, a + b