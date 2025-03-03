with open("11_grid.txt",'r') as f:
   text_grid = f.readlines()
   grid = []
   for row in text_grid:
      number_row = []
      for number in row.split():
         number_row.append(int(number))
      grid.append(number_row)


   result = 1
   for i in range(20):#horizontal
      for j in range(17):
         product = 1
         for k in range(4):
            product *= grid[i][j+k]
         result = max(product,result)
   print(result)
   for i in range(17):#vertical
      for j in range(20):
         product = 1
         for k in range(4):
            product *= grid[i+k][j]
         result = max(product,result)
   print(result)
   for i in range(17):
      for j in range(17):
         product = 1
         for k in range(4):
            product *= grid[i+k][j+k]
         result = max(product,result)
   print(result)
   for i in range(17):
      for j in range(19,2,-1):
         product = 1
         for k in range(4):
            product *= grid[i+k][j-k]
         result = max(product,result)
      
   print(result)
      
      
