f = open("59_cipher.txt","r")
cipher = [int(i) for i in f.read().strip().split(',')]

for a in range(97,123):
   for b in range(97,123):
      for c in range(97,123):
         encryption = [a,b,c]
         plaintext=''
         for i in range(len(cipher)):
            plaintext+=chr(cipher[i] ^ encryption[i%3])
         if 'Euler' in plaintext:
            print(plaintext)
            summer = 0
            for i in plaintext:
               summer+=ord(i)
            print(summer)

