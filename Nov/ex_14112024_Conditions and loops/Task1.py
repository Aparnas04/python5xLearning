#Triangle Classifier:
#Write a program that classifies a triangle based on its side lengths.
#Given three input values representing the lengths of the sides,
#determine if the triangle is equilateral (all sides are equal),
#isosceles (exactly two sides are equal), or
#scalene (no sides are equal). Use an if-else statement to classify the triangle.

s1=int(input("Enter the length of one side of triangle"))
s2=int(input("Enter the length of second side of triangle"))
s3=int(input("Enter the length of third side of triangle"))

if (s1==s2) and (s2==s3):
    print("Equilateral Triangle")
elif (s1==s2) or (s2==s3) or (s3==s1):
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

