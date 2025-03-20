import math

def has_positive_integer_root(a, b, c):
    # Calculate discriminant
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return False  # No real roots
    
    # Calculate roots
    sqrt_d = math.sqrt(discriminant)
    root1 = (-b + sqrt_d) / (2 * a)
    root2 = (-b - sqrt_d) / (2 * a)

    # Check for positive integer roots
    return (root1 > 0 and root1.is_integer()) or (root2 > 0 and root2.is_integer())

for i in range(140,10000000):
   h = i*(2*i-1)
   if has_positive_integer_root(3/2,-1/2,-h) and has_positive_integer_root(1/2,1/2,-h):
      print(i,h)
