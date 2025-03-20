import math
from collections import defaultdict
triplets = defaultdict(int)
for i in range(1,1001):
   for j in range(1001):
      k = math.sqrt(i**2+j**2)
      if i+j+k>1000:
         break
      if k==int(k):
         
         triplets[i+j+k]+=1
answer = max(triplets.values())

for i in triplets:
   if triplets[i]==answer:
      print(i)
