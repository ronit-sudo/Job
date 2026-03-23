# Python Program to calculate the square root

# Note: change this value for a different result
#num = 8 

## sources/calc.py

import sys

def sqrt_value(n: float) -> float:
    return n ** 0.5

def main():
    # Try command-line argument first: python3 sources/calc.py --num 8
    if "--num" in sys.argv:
        try:
            idx = sys.argv.index("--num") + 1
            num = float(sys.argv[idx])
        except (ValueError, IndexError):
            print("Usage: python3 sources/calc.py --num <number>")
            sys.exit(2)
    else:
        # Fallback to hardcoded value or uncomment input line
        # num = float(input("Enter a number: "))
        num = 8.0

    num_sqrt = sqrt_value(num)
    print("The square root of %0.3f is %0.3f" % (num, num_sqrt))

if __name__ == "__main__":
    main()
`` To take the input from the user

