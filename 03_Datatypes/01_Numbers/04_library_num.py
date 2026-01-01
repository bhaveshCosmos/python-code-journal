# Math Library
import math
print(math.floor(3.9)) # G.I.F
print(math.trunc(-3.9)) # Towards 0

# Random Library
import random
print(random.randint(1,100))

lis1 = ["Python", "Java", "C", "Rust", "C++"]
print(random.choice(lis1))

print(f"Before Shuffle {lis1}")
random.shuffle(lis1)
print(f"After Shuffle {lis1}")
