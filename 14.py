# Palindrome 
number=int(input("Enter any number:"))
num=number
num1= number
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if number==rev:
    print(number ,'is a Palindrome')
else:
    print(number , 'Not a Palindrome')
# Armstrong number 
sum = 0
temp = num1
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num1 == sum:
   print(num1," is an Armstrong number")
else:
   print(num1," is not an Armstrong number")
# Perfect number
sum1 = 0
for i in range(1, number):
    if(number % i == 0):
        sum1 = sum1 + i
if (sum1 == number):
    print(number, " The number is a Perfect number")
else:
    print(number, " The number is not a Perfect number")