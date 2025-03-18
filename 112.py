def bouncy_number(n):
   number= str(n)
   increasing = False
   decreasing = False
   for i in range(1,len(number)):
      if number[i]>number[i-1]:
         increasing = True
      elif number[i]<number[i-1]:
         decreasing = True
   if increasing and decreasing:
      return True
   return False

proportion = 0
num_bouncy = 0
i=1
while True:
   if bouncy_number(i):
      num_bouncy +=1
      proportion = num_bouncy/i
      if proportion==0.99:
         print(i)
         break
   i+=1

