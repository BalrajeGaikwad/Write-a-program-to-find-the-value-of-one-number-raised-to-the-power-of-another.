#Write a program to find the value of one number raised to the power of another.

# Take input from the user
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# Initialize result as 1
result = 1

# Calculate power using a for loop
for i in range(exponent):
    result *= base

# Output the result
print(f"The value of {base} raised to the power of {exponent} is {result}")
