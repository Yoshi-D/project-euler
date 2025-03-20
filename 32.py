summer = set()
for i in range(1,10):
   for j in range(1000,10000):
      set1 = set()
      
      prod = i*j
      if len(str(prod))>4:
         break
      for k in str(i)+str(j)+str(prod):
         if k=='0':
            
            break
         set1.add(k)
      if len(set1)==9:
         summer.add(prod)

for i in range(10,100):
   for j in range(100,1000):
      set1 = set()
      
      prod = i*j
      if len(str(prod))>4:
         break
      for k in str(i)+str(j)+str(prod):
         if k=='0':
            break
         set1.add(k)
      if len(set1)==9:
         summer.add(prod)
print(sum(summer))
