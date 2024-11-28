

# try : 
#     a = 10
#     b = a/0
#     # a = int(input("Enter number : "))
# except ZeroDivisionError:
#     print("divison err")
# except ValueError:
#     print("value error")

# print("Program ended")



# a = 10
# try:
#    print(10/0)
# except NameError:
#    print("variable a is not defined")
# except:
#    print("something else ")
# else:
#    print("Hello user")
# finally:
#    print("Finally block")


def test():
    try : 
        a = int(input("Enter number : "))
        print(a)
        return True
    except : 
        return False
    finally : 
        print("Print something...")







k = test()
print(k)