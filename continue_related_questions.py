"""

Q9. Skip 5 
Print numbers from 1 to 10. 
Skip number 5. 

for i in range(1,11):
    if i==5:
        continue
    print(i)

Q10. Skip Even Numbers 
Print numbers from 1 to 20. 
Skip all even numbers. 

for i in range(1,21):
    if i%2==0:
        continue
    print(i)

Q11. Skip Letter 
Print each character of the string "PYTHON". 
Skip the letter "O"


"""
st = "PYTHON"
for i in st:
    if i=="O":
        continue
    print(i)

