import math

try:
    num = float(input("Enter a number: "))

    # 1. Absolute Value
    abs_value = math.fabs(num)
    print("Absolute value of", num, "is:", abs_value)

    # 2. Exponential (e^x)
    expo = math.exp(num)
    print("Exponential (e^" + str(num) + ") is:", expo)

    # 3. Natural Logarithm (log base e)
    if num > 0:
        logarithm = math.log(num)
        print("Natural logarithm (ln) of", num, "is:", logarithm)
    else:
        print("Natural logarithm (ln) is undefined for", num, "(must be > 0).")

except ValueError:
    print("Invalid input! Please enter a valid numerical value.")
except OverflowError:
    print("The resulting exponential value is too large to calculate.")
