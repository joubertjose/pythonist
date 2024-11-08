n=int(input("Enter how many numbers to be inputted:"))
num=int(input("Enter your first number:"))
largest=num
smallest=num

while n>1:
    num=int(input(f"Enter next number:"))
    if num>largest:
        largest=num
    if num<smallest:
        smallest=num
    n=(n-1)
print(f"Largest is:{largest}")
print(f"Smallest is:{smallest}")
