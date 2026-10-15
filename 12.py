n = int(input("Enter the number of which you want factorial: "))

# --- Method 1: Using the While Loop ---
fact_while = 1
i = 1  
while i <= n:
  fact_while = fact_while * i
  i = i + 1 

print("The factorial (using while loop) is: ", fact_while)


# --- Method 2: Using the For Loop ---
fact_for = 1  
for j in range(1, n + 1):
  fact_for = fact_for * j

print("The factorial (using for loop) is:   ", fact_for)
