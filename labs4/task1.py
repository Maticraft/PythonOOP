import complex

def main():
    c1 = complex.Complex(3, 4)
    c2 = complex.Complex(1, 2)
    
    c3 = c1 / c2
    c1 /= c2
    print(c1)
    print(c3)
   

if __name__ == '__main__':
    main()