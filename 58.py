import math

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3, 5, 7):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check divisibility using 6k ± 1 optimization
    limit = int(math.sqrt(n))
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
   
prime_nums = 0
for i in range(1,10**5):
   total = []
   for j in range(1,4):
      total.append((2*i+1)**2 - 2*i*j)
   total_numbers = 4*i+1

   for num in total:
      if is_prime(num):
         prime_nums+=1
   if prime_nums/total_numbers < 0.1:
      print(i*2+1)
      break
