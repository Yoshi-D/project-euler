string = ''
prod = 1
for i in range(1,200000):
   string+=str(i)
   if len(string)>1000000:
      break

for i in range(0,7):
  prod*=int(string[10**i -1])
  
 
print(prod)
   
