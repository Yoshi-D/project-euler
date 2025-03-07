from collections import defaultdict
from math import gcd
LIMIT = 1_500_000
counts = defaultdict(int)

for m in range(2, int((LIMIT // 2) ** 0.5) + 1):
    for n in range(1, m):
        if (m - n) % 2 == 1 and gcd(m, n) == 1:  # Ensure coprime and one odd, one even
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            perimeter = a + b + c

            k = 1
            while k * perimeter <= LIMIT:
                counts[k * perimeter] += 1
                k += 1

# Count valid perimeters
result = sum(1 for count in counts.values() if count == 1)
print(result)
