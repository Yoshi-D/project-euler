start = 1000000

def helper(number,steps):
   if number==1:
      steps+=1
      return steps
   elif number%2==0:
      return helper(number/2,steps+1)
   else:
      return helper(3*number+1,steps+1)
   
result = -1
max_steps = 0
for i in range(start,0,-1):
   current = helper(i,0)
   if current>max_steps:
      max_steps = current
      result = i

print(result)
