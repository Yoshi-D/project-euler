length = 21
grid = [[0 for i in range(21)]]*21
for i in range(21):
   grid[i][0] = 1
   grid[0][i] = 1

for i in range(1,21):
   for j in range(1,21):
      grid[i][j] = grid[i-1][j] + grid[i][j-1]
print(grid[20][20])
