p = 3
q = 2
count = 0
for _ in range(1000):
   p,q = p + 2*q,q+p
   
   #print(p,q)
   if len(str(p))>len(str(q)):
      count+=1
print(count)
