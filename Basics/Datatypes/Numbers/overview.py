print(5>3>2) # 5>3 and 3>2

# Complex Numbers (represented by j)
cplx = (3 + 2j)
print(cplx*5) # (15+10j)

# Octal Numbers
print(0o34) # 28
print(oct(64)) # 0o100

# Hexa Decimal
print(0x22F) # 559
print(hex(4352)) # 0x1100

# Binary Numbers
print(0b1010) # 10
print(bin(23)) # 0b10111

# integer / base
print(int('1100',2)) # 12 
print(int('1100',8)) # 576
print(int('1100',16)) # 4352

# Math Library
import math
print(math.floor(3.9)) # G.I.F
print(math.trunc(-3.9)) # Towards 0

# Random Library
import random
print(random.randint(1,100))
lis1 = ["Python", "Java", "C", "Rust", "C++"]
print(random.choice(lis1))
print("Before Shuffle",lis1)
random.shuffle(lis1)
print("After Shuffle",lis1)
