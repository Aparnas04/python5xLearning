# FizzBuzz Test:

#Write a program that prints numbers from 1 to 100.
#However, for multiples of 3, print "Fizz" instead of the number,
#and for multiples of 5, print "Buzz." For numbers that are multiples of both 3 and 5,
# print "FizzBuzz." ( for, if)

for num in range(1, 101):
    if num%3==0 and num%5==0:
        print("FizzBuzz for", num)
    elif num%3==0:
        print("Fizz for", num)
    elif num%5==0:
        print("Buzz for", num)
    else:
        print(num)