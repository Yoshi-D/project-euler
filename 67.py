f = open("67_triangle.txt","r")

triangle = [[-1]]*100

txt = f.readlines()

for i in range(100):
   row = txt[i].split()
   for number in row:
      triangle[i]=triangle[i] + [int(number)]
  
f.close()

length_row = 2
for i in range(1,len(triangle)):
   for j in range(1,length_row+1):
      try:
         triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])
      except:
         triangle[i][j] += triangle[i-1][j-1]
   length_row+=1
print(max(triangle[-1]))
