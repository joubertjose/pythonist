'''
4. Write a Python program to reverse a string.
'''
def reverse_of_string(list):
str_1=""
str_2=len(list)
while str_2>0:
str_1+=list[str_2-1]
str_2 =str_2-1
return str_1
list=input("enter a string")
result=reverse_of_string(list)
print(("reverse_of_string:",result))
