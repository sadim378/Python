# Write a python program to find the sum of the numbers passed as parameters.

def find_sum(a, b, c):
    return a + b + c

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

total = find_sum(x, y, z)

print("The sum of the numbers is:", total)
