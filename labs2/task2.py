def multiply(a, b):
    return a * b

# a)
print("Multiplication of ints:")
try:
    print(multiply(1, 2), '\n')
except TypeError as e:
    print("Error: ", e, '\n')

print("Multiplication of floats:")
try:
    print(multiply(1.7, 2.5), '\n')
except TypeError as e:
    print("Error: ", e, '\n')

print("Multiplication of strings:")
try:
    print(multiply('a', 'b'), '\n')
except TypeError as e:
    print("Error: ", e, '\n')

print("Multiplication of int and string:")
try:
    print(multiply(5, 'b'), '\n')
except TypeError as e:
    print("Error: ", e, '\n')

print("Multiplication of string and int:")
try:
    print(multiply("b", 5), '\n')
except TypeError as e:
    print("Error: ", e, '\n')


# b)
print("Multiplication of int and tuple:")
try:
    print(multiply(3, (2, 3)), '\n')
except TypeError as e:
    print("Error: ", e, '\n')

print("Multiplication of string and list:")
try:
    print(multiply("test", [2, 3]), '\n')
except TypeError as e:
    print("Error: ", e, '\n')

print("Multiplication of list and int:")
try:
    print(multiply([2, 3], 3), '\n')
except TypeError as e:
    print("Error: ", e, '\n')

# c)
print("Multiplication of tuples:")
try:
    print(multiply((1,), (2, 3)), '\n')
except TypeError as e:
    print("Error: ", e, '\n')

print("Multiplication of lists:")
try:
    print(multiply([1], [2, 3]), '\n')
except TypeError as e:
    print("Error: ", e, '\n')