

class Student:

    _name= "Ganesh"
    _age=None

    def __init__(self,name, age):
        self._name = name
        self._age = age

    def disp(self):
        print(f"name : {self._name}")




obj  = Student("a",20)
print(obj.name)
