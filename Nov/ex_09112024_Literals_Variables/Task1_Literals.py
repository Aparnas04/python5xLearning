# Task 1 for the Today
# Take a 2 input from the user
# Print the Quotient and Remainder
# 15 ->  num1
# 2 -> num2
# Q -> 7
# R -> 1

num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
Remainder=num1%num2 # % is used to get remainder
Quotient=num1//num2 # // is used to get quotient = dividend // divisor
print("The Remainder is:", Remainder)
print("The Quotient is:", Quotient)
