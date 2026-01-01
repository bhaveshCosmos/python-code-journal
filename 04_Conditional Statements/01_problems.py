# Age Group Categorisation
# Child (<13), Teenager (13-19), Adult (20-59), Senior Citizen (>60)
age = int(input("Enter Your Age: "))
if(age<13):
    print("You are a Child")
elif(age<=19):
    print("You are a Teenager")
elif(age<=59):
    print("You are an Adult")
else:
    print("You are a Senior Citizen")

# Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: ₹120 for adults (18 and over), ₹80 for children. Everyone gets a ₹20 discount on Friday.

your_age = int(input("Enter Your Age: "))
fri_day = ["friday", "fri", "F"]
day = input("Enter day")

price = 120 if age>=18 else 80

if(day in fri_day):
    price-=20

print(f"Ticket Price for you is ₹{price}")

# Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = input("Enter Fruit: ").lower()
color = input("Enter Color of your fruit: ").lower()

if fruit == "banana":
    if(color == "yellow"):
        print("Ripe")
    elif(color == "green"):
        print("Unripe")
    elif(color == "brown"):
        print("Overripe")

# Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("Enter Password... ")
pass_len = len(password)
if pass_len < 6:
    print("Weak")
elif pass_len <=10:
    print("Medium")
else:
    print("Strong")

# 9. Leap Year Checker
# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")   