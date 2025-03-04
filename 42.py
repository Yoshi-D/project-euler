def checker(num):
   for i in range(1,1000):
      if i*(i+1) == 2*num:
         return True
   return False
f = open("42_words.txt","r")
txt = f.read().split('","')
txt[0] = "A"
txt[-1] = "YOUTH"

count = 0
for name in txt:
   summer = 0
   for char in name:
      summer+=ord(char) - 64
   
   if checker(summer):
      count+=1
print(count)

f.close()
