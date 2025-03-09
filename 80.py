from decimal import Decimal, getcontext

# Set precision to be safely higher than 100
getcontext().prec = 110  

total = 0
perfect_squares = {i * i for i in range(1, 11)}  # Set of perfect squares up to 100

for i in range(1, 101):
    if i in perfect_squares:
        continue  # Skip perfect squares

    num = Decimal(i).sqrt()  # Compute sqrt with high precision
    num_str = str(num).replace('.', '')  # Remove the decimal point

    # Extract the first 100 decimal digits
    digit_sum = sum(int(digit) for digit in num_str[:100])
    total += digit_sum

print(total)
