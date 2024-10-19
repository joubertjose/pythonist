'''
Author:Joubert jose
Date:19-10-2024
Title: Create, concatenate, and print a string and access a sub-string from a given string.
'''
name1=input("Enter your first name :")
name2=input("Enter your last name :")
name3=(name1+" "+name2)
print(name3)
name1_length=len(name1)
print(name3[name1_length: ])