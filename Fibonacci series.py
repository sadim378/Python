# Write a python program to generate Fibonacci series.

n = 10 
a, b = 0, 1

print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
