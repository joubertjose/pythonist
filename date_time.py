'''
Author:Joubert jose
Date:19-10-2024
Title: Familiarize time and date in various formats.
'''
from datetime import datetime
current_time = datetime . now()
print(current_time)
format_1=current_time. strftime("%Y-%m-%d %H:%M:%S")
print(format_1)