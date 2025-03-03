import math
import bisect

def sum_divisors(n):
   total = 0
   for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i != n // i: 
                total += n // i
   return total - n

result = 0
abundant = []
for i in range(1,28123):
   
   if sum_divisors(i)>i:
      abundant.append(i)
      
   flag = False
   for j in abundant:
      index = bisect.bisect_left(abundant,i-j)
      if index<len(abundant) and abundant[index] == i-j:
         flag = True
   if not flag:
      result+=i
print(result)
