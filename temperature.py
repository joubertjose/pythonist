'''
Author:Joubert Jose
Date:25-10-2024
Discription:Python program to convert temperature values back and forth between Celsius and Fahrenheit.
The user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit using the formula
'''
temperature=int(input("Enter temperature:"))
c= input("Is this in (C)elsius or (F)ahrenheit?")
if c=="C":
    F=(9/5*(temperature)+32)
    print(temperature,"Celsius is",F,"Farenheit")
elif c=="F":
    C=(5/9*(temperature-32))
    print(temperature,"Fahrenheit is",C,"Celsius")
else:
    print("invalid temperature")