def is_prime(n):
   for i in range(3,n//2+1,2):
      if n%i==0:
         return False
   return True

result = 2
for i in range(3,2000000,2):
   if is_prime(i):
      result+=i
      print(i, " is prime")
print(result)
