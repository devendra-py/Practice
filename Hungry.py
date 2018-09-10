# example  program to user defined raise exception

user_age = int(input("enter Age"))

def given_age(user_age):
    if (user_age>=23) and (user_age<=40):
        print("This is valid Age")
    else:
        print("Invalid Age")

try:
    given_age(user_age)
except ValueError:
    print("pls enter Integers only")
finally:
    print("this is finally block")


"""
try:
   given_age(user_age)

except ValueError:
   print("pls enter enetegers only")
   """

