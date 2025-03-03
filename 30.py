def summer(n):
   result = 0
   n = str(n)
   for i in n:
      result+= int(i)**5
   return result

result = 0
for i in range(999999+1):
   if i==summer(i):
      print(i)
      result+=i
print(result)
