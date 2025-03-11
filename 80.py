from decimal import Decimal, getcontext
getcontext().prec = 110
total = 0
for i in range(1,101):
   if i in [1,4,9,16,25,36,49,64,81,100]:
      continue
   num = Decimal(i)
   val = str(num.sqrt())
   val = val.replace('.','')
   val = val[:100]
   summer = 0
   for j in val:
      summer+=int(j)
   total+=summer
print(total)
