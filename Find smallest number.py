# Write a python program to find the smallest number from a set of numbers.

numbers = [12, 45, 3, 22, 17, 9]

smallest = numbers[0]  
for i in numbers:
    if i < smallest:
        smallest = i

print("Smallest Number:", smallest)
