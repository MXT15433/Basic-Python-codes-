while True:
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))
    op = int(input("Which operation (add:1,sub:2,multi:3,div:4): "))

    if op == 1:
        print("sum =",n1+n2)

    elif op == 2:
        print("Diff =",n1-n2)

    elif op == 3:
        print("Multi =",n1*n2)

    elif op == 4:
        print("Div =",n1/n2)

    else:
        print("invalid option")
    


