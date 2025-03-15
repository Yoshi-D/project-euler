from decimal import Decimal, getcontext

getcontext().prec = 1001
val = str(Decimal(13).sqrt())
val = val.replace('.','')
summer = 0
for i in range(1,1001):
	summer+=int(val[i])
print(summer)
