
class Pen:

    # class variable
    clg="DRSTC"

    def __init__(self,id,name):
        # name = self.name
        # id = self.id
        self.name = name
        self.id = id
        

    def show(self):
        print("show something : ")
        print(self.id , self.name, self.clg)
    
    @staticmethod
    def display():
        print("display calling.")



Pen.clg="ABC"

p = Pen(10,"Paras")
p.show()

# p.display()

p1 = Pen(20,"Ganesh")
p1.show()
# p1.display()

Pen.display()
