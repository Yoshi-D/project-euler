
def compute_totients_sieve(limit):
    phi = list(range(limit + 1))  # Initialize φ(n) = n for all n
    for p in range(2, limit + 1):
        if phi[p] == p:  # p is a prime
            for k in range(p, limit + 1, p):
                phi[k] *= (p - 1)
                phi[k] //= p
    return phi

# Example usage
limit = 10000000
totients = compute_totients_sieve(limit)

# Print results
fraction = float('inf')
result= -1
for n in range(2, limit + 1):
    if fraction>n/totients[n]:
          fraction = n/totients[n]
          result = n
print(result)
          
