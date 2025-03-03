# 1 jan 1900 = monday
# wednesday
a = 6
count = 156
for i in range(1901,2001):
   if i%4==0:
      a = (a+2)%7
   else:
      a = (a+1)%7
   if a==0:
      count+=1
print(count)
