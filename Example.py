# working with user defined Exceptions :

class TooYoungException(BaseException):
    def __init__(self,arg):
        self.arg=arg


class TooOldException(BaseException):
    def __init__(self,arg):
        self.arg=arg

age = int(input("enter a AGE of the person"))

if age>60:
    # raise userdefine exception: raise exceptionclassname("own statements")
    raise TooOldException("Plz wait some more time .. u get the marriege ")
elif age<18:
    raise TooOldException("hello man .. u r already crossed marriege age. no option")
else:
    print("you will get the job soon... attend the interviews perfctly ")







