"""

Q16. Star Pattern 
Print: 
* 
** 
*** 
**** 
***** 

for i in range(1,6):
    print("*"*i)

Q17. Reverse Star Pattern 
Print: 
***** 
**** 
*** 
** 
* 

for i in range(5,0,-1):
    print("*"*i)

Q18. Number Pattern 
Print: 
1 
12 
123 
1234 
12345 

st = ""
for i in range(1,6):
    st = st+str(i)
    print(st)

Q19. Same Number Pattern 
Print: 
1 
22 
333 
4444 
55555 

st = ""
for i in range(1,6):
    print(str(i)*i)

Q20. Pyramid Pattern 
Print: 
        * 
       *** 
      ***** 
     ******* 
    ********* 

for i in range(1,6):
    print(" "*(5-i),"*"*(2*(i-1)+1))

Q21. Inverted Pyramid 
Print: 
********* 
 ******* 
  ***** 
   *** 
    *

for i in range(1,6):
    print(" "*(i),"*"*(2*(5-i)+1))

Q22. Inverted Pyramid 
Print:

      *
     * *
    * * *
   * * * *
  * * * * *
   * * * *
    * * *
     * *
      * 

for i in range(1,6):
    print(" "*(5-i),"* "*i)
for j in range(4,0,-1):
    print(" "*(4-j)," *"*j)
"""


