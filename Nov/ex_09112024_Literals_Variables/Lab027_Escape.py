#Escape sequence

print("Hello\nWorld") #\n=new line
print("Hello\tWorld") #\t=tab
print("Hello\bWorld") #\b=back space

# what is raw concept= put r in front of string where \n, \t and \b is in the link
# to avoid reading \n as new line and same applies for \t and \b.Refer below example

dir="C:\Aparna\n\hello.txt"
print(dir)
dir=r"C:\Aparna\n\hello.txt"
print(dir)

print("a\t\tb")
print(r"a\t\tb")# put r to avoid reading \t- these are called literals




