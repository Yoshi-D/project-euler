def calculate_sum_squares(n):
   return int(n*(n+1)*(2*n+1)/6)

def calculate_square_of_sum(n):
   return int(n*(n+1)/2)
sum_of_squares = calculate_sum_squares(100)

square_of_sum = calculate_square_of_sum(100)**2
print(square_of_sum - sum_of_squares)
