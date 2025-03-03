import math
def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
   
def checker(a,b):
   i=0
   while is_prime(i**2 + a*i + b):
      i+=1
   return i
      
      
result = 0
holder = 0
for a in range(999,0,-1):
   for b in range(999,0,-2):
      if is_prime(b):
         if result < max(checker(a,b),checker(-a,b),checker(a,-b),checker(-a,-b)):
            result = max(checker(a,b),checker(-a,b),checker(a,-b),checker(-a,-b))
            holder = a*b
print(holder)
         
