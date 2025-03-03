from decimal import Decimal, getcontext

getcontext().prec = 1000

res = 10000000
for i in range(7,1000):
   string = str(Decimal(1)/Decimal(i))[2:]
   sub_string = string[-7:-1]
   if res>20 and res>string.count(sub_string):
      print(i)
      res = string.count(sub_string)

   

   
   
