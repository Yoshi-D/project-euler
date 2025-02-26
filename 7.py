def is_prime(n):
   for i in range(2,n//2+1):
      if n%i==0:
         return False
   return True

count = 0
num = 2
while True:
   if is_prime(num):
      count+=1
      if count==10001:
         print(num)
         break
   num+=1
