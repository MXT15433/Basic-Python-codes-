n = int(input("Enter the number: ")) # same input for both loops

print("USING WHILE LOOP") # 'while' loop
i = 1
while i < 11:
    print(n,"x",i,"=",i*n)
    i=i+1 

print("USING FOR LOOP") # 'for' loop
for i in range(1,11):
    print(n,"x",i,"=",i*n)
