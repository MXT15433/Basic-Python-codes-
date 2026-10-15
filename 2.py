p=int(input("Enter your Principal Amount: "))
t=int(input("Enter your Time: "))
r=int(input("Enter your Rate of Interest: "))

si=p*r*t/100

ci=p*(1+r/100)**t

print("SIMPLE INTERSET: ",si)
print("COMPOUND INTERSET: ",ci)
