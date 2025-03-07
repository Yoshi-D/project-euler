def euler_totient(n):
    result = n  
    p = 2  
    while p * p <= n:  
        if n % p == 0:  
            while n % p == 0:  
                n //= p  
            result -= result // p  
        p += 1  
    if n > 1:  
        result -= result // n  
    return result  

# Compute totient function for all numbers up to a given limit
def compute_totients(limit):
    totients = {}
    for n in range(1, limit + 1):
        totients[n] = euler_totient(n)
    return totients

# Example usage
limit = 1000000  # You can set this to any number you want
totients = compute_totients(limit)
fraction = -1
result = -1
# Print results
for n in range(1, limit + 1):
    if fraction<n/totients[n]:
       fraction = n/totients[n]
       result = n
print(result)
