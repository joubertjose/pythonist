'''
3. Write a Python function to multiply all the numbers in a list.
'''
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
        print(total)
num1=int(input("Enter a number:"))
num2=int(input("Enter a second number:"))
numbers=(num1,num2)
multiply(numbers)