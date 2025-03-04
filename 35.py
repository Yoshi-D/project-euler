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

def rotator(n,count):
   if len(str(n))==count:
      return True
   if is_prime(n):
      return rotator(int(str(n)[-1]+str(n)[:-1]),count+1)
   return False

result = 0
for i in range(2, 1000001):
   if rotator(i,0):
      result+=1
print(result)
