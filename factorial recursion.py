'''
Name:Joubert
Date:29-11-24
Description:Program to find the factorial of a number using Recursion.
'''
def factorial(number):
    if number==0:
        return 1
    else:
        return number * factorial(number-1)

numbers=int(input("Enter a number:"))
custom=factorial(numbers)
print("The factorial of the given number is:",custom)