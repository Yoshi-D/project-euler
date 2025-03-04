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
   
def truncation(n):
   string = str(n)
   for i in range(1,len(string)):
      if not is_prime(int(string[i:])):
         return False
      if not is_prime(int(string[:-i])):
         return False
   return True

count=0
result = 0
i=11
while count<11:
   if is_prime(i) and truncation(i):
      count+=1
      result+=i
   i+=2
print(result)

      
      
   
