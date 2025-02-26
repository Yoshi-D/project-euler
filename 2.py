t1 = 1
t2 = 2
result = 2
while t1+t2<4000000:
   if (t1+t2)%2==0:
      result+=t1+t2
   t1,t2  = t2,t1+t2
print(result)
