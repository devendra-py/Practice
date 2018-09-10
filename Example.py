# welcome user defined Exception :



def given_age(user_age):
     if (user_age>=23) and (user_age>=40):
         print("The Valid Age")

     else:
         raise ValueError("pls enter a Valid age")


user_age=int(input("eneter a age"))
"""try:
    given_age(user_age)
except ValueError:
    print("valid age")

"""

