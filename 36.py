result = 0
for i in range(1,1000001):
   if str(i)==str(i)[::-1]:
      binary = bin(i)[2:]
      if binary==binary[::-1]:
         result+=i
         print(i)

print(result)
