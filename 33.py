for i in range(11,100):
   for j in range(i+1,100):
      if i%10==0 or j%10==0:
         continue
      
      temp= i/j
      new_i,new_j = -1,-1
     
      if str(i)[0]==str(j)[1]:
         new_i = int(str(i)[1])
         new_j = int(str(j)[0])

      elif str(i)[0]==str(j)[0]:
         new_i = int(str(i)[1])
         new_j = int(str(j)[1])
         
      elif str(i)[1]==str(j)[1]:
         new_i = int(str(i)[0])
         new_j = int(str(j)[0])
      
      elif str(i)[1]==str(j)[0]:
         new_i = int(str(i)[0])
         new_j = int(str(j)[1])
      
  #    if i==49 and j==98:
#         print(temp,new_i,new_j)
      
      if temp==new_i/new_j:
         print(i,j,new_i,new_j)
            
