
import math

def sum_divisors(n):
   total = 0
   for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i != n // i: 
                total += n // i
   return total - n
print(sum_divisors(220))
print(sum_divisors(284))
result = 0
for i in range(2,10001):
   temp = sum_divisors(i)
   if i==sum_divisors(temp) and i!=temp:
      result+=i 
print(result)
