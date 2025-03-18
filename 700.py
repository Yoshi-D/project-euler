s = float('inf')
summer = 0
i = 1
while True:
   val = (1504170715041707 * i) % 4503599627370517
   if val < s:
      s = val
      summer+=val
#      print(summer)
   elif val> 4503599627370517//1504170715041707:
      break
   i+=1
   
print(summer)
