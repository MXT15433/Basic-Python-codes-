n = int(input("Enter the number upto which you want pibonacci series: "))
a=0
b=1
i=1
while i<=n:
    print(a,end=" , ")
    c=a+b
    a=b
    b=c
    i=i+1

a=0
b=1
for j in range (1,n+1):
    print(a,end=" , ")
    c=a+b
    a=b
    b=c