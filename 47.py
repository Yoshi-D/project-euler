def sieve_of_eratosthenes(n):
    prime = [True] * (n + 1)
    prime[0] =prime[1] = False  # 0 and 1 are not prime numbers

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

count2 = 0
for i in range(10**5,10**10):
	
    
            count = 0
            for k in primes:
                    if (i)%k==0:
                            count+=1
            if count==4:
                    count2 += 1
                    #print(i)
                    if count2 == 4:
                        print("WOOOHOOOOO", i)
                        break
            else:
                count2 = 0
            
