
class A:

    def __init__(self):
        print("class A const calling")
    def show(self):
        print("running show method...")

class B(A):

    def __init__(self):
        print("class B const callling")


a = A()
b = B()
b.show()