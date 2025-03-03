result = 0
with open("13_numbers.txt","r") as f:
   lst = f.readlines()

   for i in range(100):
      result += int(lst[i])

   print(str(result)[:10])
   
   
