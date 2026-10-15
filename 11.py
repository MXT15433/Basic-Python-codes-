n=int(input(" How many times you have to add numbers: "))

print("USING WHILE LOOP")
i=1 # using while loop
s=0
while i < n+1:
    a=int(input("Enter the number to add:"))
    s=s+a
    i=i+1
print(s)

print("USING FOR LOOP")
s=0 # using for loop
for i in range(1,n+1):
    a=int(input("Enter the number to add:"))
    s=s+a
print(s)
