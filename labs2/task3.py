# Function that calculates the average of two numbers
def avg(a, b):
    return (a + b) / 2

# Function that calculates the average of first two numbers and then 
# combined average with the third number
def avg_avg(a, b, c):
    return avg(avg(a, b), c)


print(avg_avg(1, 2, 3))