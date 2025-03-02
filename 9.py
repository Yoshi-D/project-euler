for a in range(1,1000):
   flag = False
   for b in range(a+1,1000):
      c = 1000 - a - b
      if a*a + b*b == c*c:
         print(a*b*c)
         flag = True
         break
   if flag:
      break
