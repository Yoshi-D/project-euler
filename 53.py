import math
count = 0
for i in range(1,101):
   for j in range(i):
      if math.comb(i,j)>1000000:
         count+=1
print(count)
