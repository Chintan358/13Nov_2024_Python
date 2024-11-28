



a = int(input("Enter number between 1 to 10"))


class MyException(Exception):
        print("Exception accured....")
        pass

try : 
    if(a<1 or a>10):
        raise MyException()
except MyException:
    pass
else:
    print("Valid number")

print("something after code....")