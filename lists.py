'''
Name:Joubert
Date:22-11-24
'''
list1 =[43,21,22,44,67,21]
list2 =[34,21,34,56,87,21]
print("Enter list1:",list1)
print("Enter list2:",list2)
combined_list =list1+list2
even_list=[]
odd_list=[]
for i in combined_list:
    if i%2==0:
        even_list.append(i)
    elif i%2!=0:
        odd_list.append(i)
odd_list.sort()
even_list.sort()
merged_list=even_list+odd_list
print("merged_list:",merged_list)