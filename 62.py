import itertools,math
#if permutations of n**3 check number of cubes in this permutations, if len is equal to 5 break
def is_perfect_cube(n):
    if n < 0:
        n = -n
    k = round(n ** (1/3))
    return k ** 3 == n
   
n = 1000
while True:
   print(n)
   count =0
   array = list(itertools.permutations(str(n**3)))

   for tuple1 in array:
      
      i = int(''.join(tuple1))
      if i<n**3:
         continue
#      print(i)
#      continue
   
      if is_perfect_cube(i):
#         print(i)
         count+=1
   if count==10:
      print(n**3)
      break
   n+=1
 
   
