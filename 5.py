n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))
n3=int(input("Enter 3rd number:"))

largest=n1
smallest=n1

if n2>largest:
    largest=n2
    
if n3>largest:
    largest=n3

if n2<smallest:
    smallest=n2
    
if n3<smallest:
    smallest=n3

print("Largest=",largest)
print("Smallest=",smallest)
    
