import math

def checker(n):
   string  = str(n)
   summer = 0
   for i in string:
      summer+=math.factorial(int(i))
   return summer==n
result = 0
for i in range(10,1000000):
   if checker(i):
      result+=i
print(result)
