#for loop range(1,10,1)-start, stop and how many steps( how many increment or decrement loop has to do), by default it is 1 step.
'''for i in range(1,10): # it is always n-1, the index starts with 0 in range function
    print(i)'''

'''for i in range(1,10,2):
    print(i)'''

'''for i in range(3,5):
    print(i)'''

'''for i in range(10): # it will start from 0 and will go till 9
    print(i)'''

'''for i in range(-1,-10,-2):
    print(i)'''

'''for i in range(10):
    print(i)'''
year=int(input("Enter the year"))
if year % 4 ==0 and year % 100 !=0:
    print("It's a Leap Year")
elif year % 400==0 :
    print("A Leap Year")
else:
    print("It is not Leap Year")