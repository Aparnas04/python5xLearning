#Compare Operators
from operator import truediv

print(2==3) # ==returns True or False
print(3==3) # ==returns True or False

#Not operator
Is_Aparna_Married= True
print(not Is_Aparna_Married) # not operator returns True/False
print(Is_Aparna_Married)

#Logical Operator - returns in True/False, >, <, >=,<=
x=10
y=20
print(x>y)
print(x<y)
# OR Gate AND Gate
f= 'false'
t= 'true'
print(f or t)# returns false
print (f and t)# returns true

x=10
y=20

print(x!=y)

q,r=divmod(5,2)
print(q)
print(r)

a,b,c=1,2,3
print(a)
print(b)
print(c)

# increment and decrement operator
x=5
x+=1 # x=x+1
print(x)
x-=1
print(x)
x*=3
print(x)

age_req=int(input('enter the age'))
if age_req > 18:
     print('you are allowed to vote')
else:
     print('you are not allowed to vote')

radius=float(input('enter the radius'))
area=3.14 * (radius ** 2)# ** is power
print("Area of the circle is:", area)


