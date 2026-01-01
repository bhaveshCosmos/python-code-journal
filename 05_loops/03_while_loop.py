# Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.
fact = 1
i = 1
num = int(input("Enter Number: "))
while i<=num:
    fact*=i
    i+=1
print(f"Factorial of {num} is {fact}")

# Prime Number Checker
# Problem: Check if a number is prime.
user_num = int(input("Enter a number: "))
i, div = 1, 0
while(i<=user_num):
    if user_num%i == 0:
        div+=1
    i+=1
if div == 2:
    print(f"{user_num} is a Prime number")
else:
    print(f"{user_num} is a Composite Number")