with open("0081_matrix.txt",'r') as f:
   txt = f.read()
matrix = txt.split('\n')
for i in range(len(matrix)):
   matrix[i] = matrix[i].split(',')
matrix = matrix[:-1]
for i in range(80):
   matrix[i] = [int(i) for i in matrix[i]]

dp = [[0 for _ in range(80)] for _ in range(80)]
dp[0][0] = matrix[0][0]
for i in range(1,80):
   dp[i][0] = matrix[i][0] + dp[i-1][0]
   dp[0][i] = matrix[0][i] + dp[0][i-1]
   

for i in range(1,80):
   for j in range(1,80):
      dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + matrix[i][j]
      
print(dp[-1][-1])
