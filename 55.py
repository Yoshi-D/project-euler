def is_palindrome(n):
   return n==int(str(n)[::-1])
def lychrel(n):
   for i in range(50):
      val = n+int(str(n)[::-1])
      if is_palindrome(val):
         return False
      n = val
   return True

count = 0
for i in range(1,10000):
   if lychrel(i):
      count+=1
print(count)
