str1 = "  Python & Java "

# upper()
print(str1.upper())
# lower()
print(str1.lower())
# strip()
print(str1.strip())
s = 'www.example.com'.strip('cmow.') # strip() with combination of characters
print(s)
# replace(arg1,arg2)
print(str1.replace("Java", "C++")) # Case Sensitive
# split(arg)
languages = "Python, Java, C++, C#, C, Rust, Go, JS, TS"
print(languages.split(", ")) # Default " " (space)
# find(arg)
print(f"Java @ index {languages.find("Java")}")
print(f"R @ index {languages.find("R")}")
print(f"Z @ index {languages.find("Z")}") # -1 if not found
# join
city_list = ["New Delhi", "Mumbai", "Roorkee"]
print(", ".join(city_list))
# length
print(len(str1))
# iterate
for ch in str1:
    print(ch)
# in
lang = "Java8"
print(lang in languages) # False
# Method Chaining
raw_str = "   Python DeveloPment"
print(raw_str.strip().lower().replace("development", "Programming").upper())
