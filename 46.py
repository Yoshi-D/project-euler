import math
def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize all entries as True
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False  # 0 and 1 are not prime numbers

    # Start from the first prime number, 2
    for p in range(2, int(n**0.5) + 1):
        if prime[p]:  # If prime[p] is still True, it's a prime
            # Mark all multiples of p as False (not prime)
            for i in range(p * p, n + 1, p):
                prime[i] = False

    # Collect all prime numbers
    primes = [p for p in range(n + 1) if prime[p]]
    return primes

# Example usage
primes = sieve_of_eratosthenes(10**5)

for number in range(1,10**5,2):
   if number in primes:
      continue
   flag = False
   for prime in primes:
      
      new = number - prime
      if new<0:
         break
      new = new//2
      if math.sqrt(new)==int(math.sqrt(new)):

         flag = True
         break
   if flag==False:
      print(number)
