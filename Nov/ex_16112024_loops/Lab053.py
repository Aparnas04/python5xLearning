# match statement, which is similar to switch in Java
#match the O/p and execute
# match is applicable in python 3.10
# match variable:
#    case pattern1:
         #code block

# Ask a user which browser he want to run an automation
browser_name=input("Enter the browser name\n")
match browser_name:
     case "firefox":
         print("Run with firefox")
     case "Internet Explorer":
         print("Run with IE")
     case _: # for other cases use underscore, if it doesn't match with any other browser
         print("No browser found")





