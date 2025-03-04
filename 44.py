pentagonals = []
for n in range(1,10000):
   pentagonals.append(n*(3*n -1 )//2)
mini = float('inf')

for i in range(len(pentagonals)):
   
   for j in range(i+1,len(pentagonals)):
      if pentagonals[j] - pentagonals[i] in pentagonals and pentagonals[j] + pentagonals[i] in pentagonals:
         print(pentagonals[j] - pentagonals[i])
 
