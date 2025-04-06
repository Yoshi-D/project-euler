n = 1 #number of digits
count = 0
while True:
   i=0
   while len(str(i**n))<=n:
      if len(str(i**n)) == n:
         print(n,i**n)
         count+=1
      i+=1
   n+=1
   print(count)
#loop till i get 
