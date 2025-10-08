# Write a python program to find the sum of odd and even numbers from a set of numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum_even = 0
sum_odd = 0

for num in numbers:
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

print("Sum of Even Numbers:", sum_even)
print("Sum of Odd Numbers:", sum_odd)
