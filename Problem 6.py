sum_of_squares = 0
square_of_sums = 0

for i in range (101):
    sum_of_squares = sum_of_squares + i*i
    square_of_sums = square_of_sums + i
answer = (square_of_sums*square_of_sums - sum_of_squares)
print (answer)
