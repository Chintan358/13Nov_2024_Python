
class A:

    def __init__(self,name,email):
        self.name=name
        self.email=email
    def display(self):
        print(self.name,self.email)

class A1:

    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)

class B(A1,A):

    def __init__(self,name,email):
        A.__init__(self,name,email)
        A1.__init__(self,name)
        # super().__init__(name)

class C(A):
    pass

# a = A("Paras","paras@gmail.com")
b = B("Ganesh","Ganesh@gmai.com")


b.display()
b.show()