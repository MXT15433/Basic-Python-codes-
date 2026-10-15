n=int(input("Enter the number: "))
if n==1:
    print("1 is neither prime nor composite.")  
elif n>1:
    i=2
    while i<n:
        if (n % i) == 0:
            print(n,"is not a prime number")
            break
        i = i + 1
    else:
        print(n,"is a prime number")


if n==1:
    print("1 is neither prime nor composite.")  
elif n>1:
    for j in range(2, n):
        if (n % j) == 0:
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")