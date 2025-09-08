from calculator import Calculator

def main():
    calc = Calculator()
    print("3 + 2 =", calc.add(3, 2))
    print("3 - 2 =", calc.subtract(3, 2))
    print("3 * 2 =", calc.multiply(3, 2))
    print("3 / 2 =", calc.divide(3, 2))

if __name__ == "__main__":
    main()
