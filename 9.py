import math

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

gcd = math.gcd(num1, num2)
lcm = math.lcm(num1, num2)

print("Numbers:", num1, "and", num2)
print("Greatest Common Divisor (GCD):", gcd)
print("Least Common Multiple (LCM):", lcm)
