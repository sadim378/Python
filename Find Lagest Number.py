# Write a python program to find the largest number between two numbers using function

def find_largest(a, b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

largest = find_largest(num1, num2)

print("The largest number is:", largest)
