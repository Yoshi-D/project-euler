with open("22_names.txt","r") as f:
   txt = f.read().split('","')
   txt[0] = "MARY"
   txt[-1] = "ALONSO"
   txt.sort()

   result = 0
   for index,word in enumerate(txt):
      worth = 0
      for i in word:
         worth+=ord(i) - 64
      result+=worth*(index+1)
   print(result)
         
   
   
