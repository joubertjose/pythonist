'''
Author:Joubert Jose
Date:18'-10-2024
Description: program that uses functions from the math module to perform
the following operations on a number provided by the user:
'''
import math
number=int(input("Enter a number:"))
square_root=math.sqrt(number)
print("Square root of ",number,":",square_root)
print("factorial of ",number,":",math.factorial(number))
print("Power of ",number,":",math.pow(number,2))