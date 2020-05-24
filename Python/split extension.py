import os
file_name = 'my_file.txt'
s=os.path.splitext(file_name)
print(type(os.path.splitext(file_name)))
print(type(file_name))
print(s[1])
