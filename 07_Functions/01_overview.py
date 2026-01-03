def factorial(x):
    if x <= 1:
         return 1
    return x * (factorial(x-1))

print(factorial(5))

def even_sum(ls,sum = 0):
    for i in ls:
          if i%2 == 0:
               sum+=i
    return sum

print(even_sum([1,2,3,4,5,6,7,8,9,10]))
               