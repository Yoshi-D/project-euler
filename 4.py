import math
def is_prime(n):
   for i in range(2,n//2+1):
      if n%i==0:
         return False
   return True

for i in range(int(math.sqrt(600851475143))+1,1,-1):
   if 600851475143%i==0 and is_prime(i):
      print(i)
      break
   
