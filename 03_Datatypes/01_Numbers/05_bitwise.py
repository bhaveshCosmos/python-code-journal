num1 = 10 # 0b1010
num2 = 6 # 0b0110

# Bitwise AND (&)
print(f"{num1}&{num2}: {num1 & num2}") # 2 = 0b0010

# Bitwise OR (|)
print(f"{num1}|{num2}: {num1 | num2}") # 14 = 0b1110

# Bitwise  XOR (^)
print(f"{num1}^{num2}: {num1 ^ num2}") # 12 = 0b1100

# Bintwise NOT {~}
print(f"~{num1}: {(~num1)}")

# Left Shift (<<)
# << n = multiply by 2^n
print(f"{bin(num1)}<<2: {bin(num1 << 2)}")

# Right Shift (>>)
# << n = divide by 2^n
print(f"{bin(num1)}>>2: {bin(num1 >> 2)}") 