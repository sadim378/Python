lst = []
n = int(input("Enter number of elements: "))
for i in range(n):
    while True:
        try:
            ele = int(input(f"Enter element {i+1}: "))
            lst.append(ele)
            break
        except ValueError:
            print("Invalid input! Please enter an integer.")
    
print("List:", lst)
print("Sum of elements in the list is:", sum(lst))
