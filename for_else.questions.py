"""

Q14. Search Number Using for-else 
Search for number 100 in a list. 
If found, print "Found". 
If not found, print "Not Found". 

list = [25,45,63,85,45,1020,250,100]
for i in list:
    if i == 100:
        print("found")
        break
else:
    print("not found!")

Q15. Prime Number Check 
Take a number from the user and check whether it is prime using for-else.


"""
num = int(input("Enter the number: "))
count = 0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
if count==2:
    print("Prime number")
else:
    print("Not a prime number")
