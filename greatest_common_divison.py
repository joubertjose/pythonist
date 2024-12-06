'''
name:joubert
date:06-12-2024
description:Recursive function to find the greatest common divisor of two positive numbers.
'''
def gcd(num1,num2):
    if num1 >= 0 and num2 >= 0:
        if num2 ==0:
            return num1
        else:
            return gcd(num2,num1%num2)
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
print(gcd(num1,num2))
