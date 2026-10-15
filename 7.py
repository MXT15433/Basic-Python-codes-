print("ax^2 + bx + c = 0")
a = int(input("Enter value of a in accordance to the above equation: "))
b = int(input("Enter value of b in accordance to the above equation: "))
c = int(input("Enter value of c in accordance to the above equation: "))

nature = (b**2) - (4 * a * c)

if nature > 0:
  print("Real and Distinct Roots")
  x1 = (-b + (nature**0.5)) / (2 * a)
  x2 = (-b - (nature**0.5)) / (2 * a)
  print("ROOTS ARE:", x1, "and", x2)

elif nature == 0:
  print("Equal Roots")
  x1 = -b / (2 * a)
  print("ROOTS ARE:", x1, "and", x1)

else:
  print("Imaginary Roots")
