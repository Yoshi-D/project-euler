import itertools
primes = [2,3,5,7,11,13,17]

string = "9876543210"

li = [''.join(p) for p in itertools.permutations(string)]
summer = 0

for number in li:
   if number[0]=='0':
      break
   flag = True
   for i in range(1,8):
      sub = int(number[i:i+3])
      if sub%primes[i-1]!=0:
         flag  = False
         break
   if flag:
      summer+=int(number)
print(summer)
