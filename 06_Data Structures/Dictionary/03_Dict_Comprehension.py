squares_cube = {x: x**2 if x%2 == 0 else x**3 for x in range(1, 11)}
print(squares_cube)

# Swap
dict_1 = {"a":1, "b":2, "c":3}
swap = {j:i for i, j in dict_1.items()}
print(swap)

# Multiplication
res = {}
for i in range(1,6):
    table = {}
    for j in range(1,11):
        table[j] = i*j
    res[i] = table
for i in res:
    print(f"{i}: {res[i]}")

mult_tab = {i:{j:j*i for j in range(1,11)} for i in range(1,6)}
for i in mult_tab:
    print(f"{i}: {mult_tab[i]}")

