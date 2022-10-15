def custom_sum(a, b):
    return a + b

# a)
print("Sum of ints:")
try:
    print(custom_sum(1, 2), '\n')
except TypeError as e:
    print("Error: ", e, '\n')

print("Sum of floats:")
try:
    print(custom_sum(1.7, 2.5), '\n')
except TypeError as e:
    print("Error: ", e, '\n')

print("Sum of strings:")
try:
    print(custom_sum('a', 'b'), '\n')
except TypeError as e:
    print("Error: ", e, '\n')

print("Sum of int and string:")
try:
    print(custom_sum(3, 'b'), '\n')
except TypeError as e:
    print("Error: ", e, '\n')

# b)
print("Sum of int and tuple:")
try:
    print(custom_sum(1, (2, 3)), '\n')
except TypeError as e:
    print("Error: ", e, '\n')

print("Sum of string and list:")
try:
    print(custom_sum("test", [2, 3]), '\n')
except TypeError as e:
    print("Error: ", e, '\n')

# c)
print("Sum of tuples:")
try:
    print(custom_sum((1,), (2, 3)), '\n')
except TypeError as e:
    print("Error: ", e, '\n')

print("Sum of lists:")
try:
    print(custom_sum([1], [2, 3]), '\n')
except TypeError as e:
    print("Error: ", e, '\n')