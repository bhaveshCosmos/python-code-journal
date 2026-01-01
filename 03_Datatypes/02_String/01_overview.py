language = "Python"
print(language) # Python

# Index
print(language[1]) # y

# Slicing
str_num = "0123456789"

print(str_num[:7]) # 0123456
print(str_num[:-1]) # 9876543210
print(str_num[:9:2]) # 02468
print(str_num[:2:-2]) # 9753

# Format
str1 = "Hello, {} {}"
first_name = "Bhavesh"
last_name = "Upadhyay"
print(str1.format(first_name, last_name))

path = r"c:\user\python"
print(path+"\\")

'''
    Immutable Datatype
'''