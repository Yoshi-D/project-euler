from math import log

with open("99_numbers.txt",'r') as f:
   text = f.readlines()
numbers = [ i.strip().split(',') for i in text]

def helper(base,exp,max_res):
   if exp * log(base) > max_res:
      
      return True
   return False
line = 0
max_res = 0
i = 1
for base,exp in numbers:
   if helper(int(base),int(exp),max_res):
      max_res = int(exp) * log(int(base))
      line = i
   i+=1
print(line)
