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

for i in range(1003,9999,2):
   for j in range(1,9999):
      if is_prime(i) and is_prime(i+j) and is_prime(i+2*j):
         if set(str(i))==set(str(i+j))==set(str(i+2*j)):
            if len(str(i)+str(i+j)+str(i+2*j))==12:
               print(i,i+j,i+2*j)
               break
