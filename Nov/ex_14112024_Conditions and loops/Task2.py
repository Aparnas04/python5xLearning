#Checking for a Leap Year, 2024 → Yes
#Leap day occurs #in each year that is a multiple of 4, except for years evenly divisible by 100 but not by 400.
Year=int(input("Enter the year"))

if Year%4==0 and Year%100!=0:
    print("Yes,", Year," is a Leap Year")
elif Year%400==0:
    print("Yes,", Year, " is a Leap Year")
else:
    print("No,", Year, " is not a Leap Year")


