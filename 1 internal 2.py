n=int(input("Enter how many numbers to be inputted:"))
num=int(input("Enter your first number:"))
smallest=num
second_smallest=smallest
largest=num
second_largest=largest

while n>1:
    num=int(input("Enter next number:"))
    if num>largest:
        second_largest = largest
        largest = num

    elif num>second_largest:
        second_largest=num
    if num<smallest:
        second_smallest = smallest
        smallest = num

    elif num<second_smallest:
        second_smallest = num
    n=(n-1)

print(f"Largest is:{largest}")
print(f"Smallest is:{smallest}")
print(f"Second Largest is:{second_largest}")
print(f"Second Smallest is:{second_smallest}")

