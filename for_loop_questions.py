"""

Q1. Print Numbers 
Use a for loop to print numbers from 1 to 10. 

for i in range(1,11):
    print(i)

Q2. Print Even Numbers 
Print all even numbers between 1 and 20. 

for i in range(1,21):
    if i%2==0:
        print(i)

Q3. Find Sum 
Print the sum of numbers from 1 to 10 using a for loop. 

sum = 0
for i in range(1,11):
    sum += i
print("Total sum: ",sum)

Q4. Multiplication Table 
Take a number from the user and print its multiplication table up to 10. 

num = int(input("Enter the table number: "))
for i in range(1,11):
    print(num,"X",i,"=",num*i)

Q5. Count Characters 
Take a string and count the total number of characters using a for loop.


"""
st = input("Enter the string: ")
count = 0
for i in st:
    count = count + 1
print("Total numberof characters: ",count)