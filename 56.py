max_sum = 0
for i in range(1,100):
   for j in range(1,100):
      max_sum = max(sum([int(k) for k in str(i**j)]),max_sum)
print(max_sum)
      
