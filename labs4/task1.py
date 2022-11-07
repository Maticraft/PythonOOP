import complex

def main():
    c1 = complex.Complex()
    c2 = complex.Complex()
    
    print(c1.get_real())
    c1.set_real(4)
    c1.set_imaginary(5)
    print(c1.get_real())
    print(c1.get_imaginary())
    print(c1.module())
    print(c1.argument())

if __name__ == '__main__':
    main()