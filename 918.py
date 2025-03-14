def a(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n % 2 == 0:
        memo[n] = 2 * a(n // 2)
    else:
        memo[n] = a(n // 2) - 3 * a(n // 2 + 1)
    return memo[n]

def compute_s(n):
    total = 0
    for i in range(1, n + 1):
        total += a(i)
        print(i)
    return total

# Efficiently compute the sum using memoization
print(compute_s(10**12))  # Test with smaller numbers first
