print("Palindrome Number Checking")
num=int(input("Enter Number:"))
sum=0
temp=num
while(temp>0):
    r=temp%10
    sum=(sum*10)+r
    temp=temp//10

if(num==sum):
    print("Palindrome Number -",num)
else:
    print("Not a Number-",num)