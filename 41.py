import math
import itertools

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

string = "987654321"
for i in range(len(string)):
   li = [''.join(p) for p in itertools.permutations(string[i:])]
   flag = False
   for j in li:
      if is_prime(int(j)):
         print(j)
         flag = True
         break
   if flag:
      break

