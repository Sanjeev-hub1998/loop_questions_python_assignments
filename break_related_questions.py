"""
Q6. Stop at 5 
Print numbers from 1 to 10. 
Stop the loop when the number becomes 5. 


for i in range(1,11):
    if i==5:
        break
    print(i)

Q7. Search in List 
Search for number 25 in a list. 
If found, print "Found" and stop the loop.

list = [215,36,45,85,96,25]
for i in list:
    if i==25:
        print("found")
        break

        
Q8. First Negative Number 
Given a list of numbers, print the first negative number and stop the loop. 


"""
list = [25,45,-25,85,64,-25,-75]
for i in list:
    if i==-25:
        print(i)
        break