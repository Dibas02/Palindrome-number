n = int(input("Enter a number: "))
length = len(str(n))

temp = n
sum = 0

while n>0:
    digit = n%10
    sum = sum*10 + digit
    n= n//10

if temp==sum:
    print(temp, "is a palindrome number.")
else:
    print(temp, "is not a palindrome number")
