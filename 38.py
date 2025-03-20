answer = -1
for i in range(1,10**6):
   string = ''
   for n in range(1,10):
      if '0' in str(i*n):
         break
      if len(string)+len(str(i*n))>9:
         break
      string+=str(i*n)
   if len(set(string))==9:
      answer = max(answer,int(string))
print(answer)
      
