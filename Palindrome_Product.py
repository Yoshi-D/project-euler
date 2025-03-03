result = 0
for i in range(990,99,-11):
   for j in range(999,99,-1):
      val = str(i*j)
      if val==val[::-1]:
         result = max(int(val),result)
         
print(result)
