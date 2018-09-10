# working with nested try block exception :

try:
   print("this is outer try block")
   try:
      print("this is inner try block")
   except:

       print("this is inner try block except")
   else:
        print("this is inner try block else block")

   finally:
        print("this is inner try block finnaly")

except:
   print("this is an outer except block")
else:
    print("this is else block of the outer block")
finally:
    print("this outer finally block")

