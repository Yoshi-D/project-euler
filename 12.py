def num_of_divisors(n):
   answer = 0
   for i in range(1,int(n**0.5)+1):
      if n%i==0:
         answer+=1
   if int(n**0.5)**2 == n:
      return answer*2 - 1
      
   return answer*2
answer = 0
i=1
while num_of_divisors(answer)<500:
   answer = i*(i+1)//2
   i+=1

print(answer)
