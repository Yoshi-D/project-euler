a = 1
b = 1
index = 2
while len(str(a+b))!=1000:
   temp = a+b
   a,b = b,temp
   index+=1
print(index)
   
