# Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.
count = 0
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
for num in numbers:
    if num > 0:
        count+=1
print(f"{count}, Positive Numbers are in the List")

# Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.
n = int(input("Enter last number: "))
sum = 0
for i in range(2,n+1,2):
    sum+=i
print(f"sum of first {n} even terms is {sum}")

# Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.
num = int(input("Enter Number: "))
for i in range(1,11):
    if i==5:
        continue
    else:
        print(f"{num} X {i} = {i*num}")

# 4. Reverse a String
# Problem: Reverse a string using a loop.
str_1 = "Python"
rev = ''
for char in str_1:
    rev = char + rev
print(rev)

