# List of Squares
nums = list(range(1,11))
sq_list = []
for num in nums:
    sq_list.append(num*num)
print(sq_list) 

# List of Cubes
print([num**3 for num in nums])

# Even term square
print([i**2 if i%2 == 0 else i for i in range(1,11)])

string = "Python is a Programming Language"
# split_string = string.split()
# res = []
# for word in split_string:
#     if len(word)>=5:
#         res.append(word.upper())
#     else:
#         res.append(word)
# print(res)

print([word.upper() if len(word)>=5 else word for word in string.split()])