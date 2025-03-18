import sys
sys.set_int_max_str_digits(10**6)
l = '123'
n = 678910

j=12780 + 1000
while n>0:
   if str(2**j//10**5)[:len(l)] == l:
      n-=1
      
   j+=1
print(j-1)
