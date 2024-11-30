
a = int(input("Enter number between 1 to 10"))


class MyException(Exception):
        
        def __init__(self):
            print("number should be between 1 and 10")
        pass

try : 
    if(a<1 or a>10):
        raise MyException()
except MyException:
    pass
else:
    print("Valid number")

print("something after code....")