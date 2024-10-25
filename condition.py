'''Author:Joubert Jose
Date:25-10-2024
Discription:Python program to find the largest of three numbers. The program should take three numbers as input
from the user and determine which one is the largest. '''
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
num3=int(input("Enter the third number"))
if num1>num2 and num1>num3:
    print(num1,"is greater than the other two")
elif num2>num3:
    print(num2,"is greater than the other two")
else:
    print(num3,"is greater than the other two")
