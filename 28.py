result = 0
for i in range(1,1002,2):
   for j in range(4):
      result+=i**2 - j*(i-1)
print(result-3)
