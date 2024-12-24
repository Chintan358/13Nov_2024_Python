
class Test:

    def __init__(self,a):
        self.a = a
    
    def display(self):
        print(self.a)

    @property
    def set_val(self):
        return self.a*20

    @set_val.setter
    def set_val(self,k):
        self.a =k


t = Test(10)


t.set_val=400
print(t.set_val)
print(t.a)

