# class Test : 
    
#     # def add(self,a,b,c):
#     #     print(a+b+c)
#     # def add(self,a,b):
#     #     print(a+b)
#     def add(self,*a):
#         sum = 0
#         for i in a:
#             sum +=i
#         print(sum)

# t  =Test()
# t.add(10,20)
# t.add(10,20,30)

# class A:

#     def show(self):
#         print("Show method calling")

# class B(A):

#     def __init__(self):
#         pass
#     def show(self):
#         print("Class B show calling...")
#         super().show()

# b = B()
# b.show()


class Calc:

    def __init__(self,a,b):
        self.a = a 
        self.b = b 
    
    def __add__(self,u):
        return Calc(self.a+u.a,self.b+u.b)

    def __str__(self):
        return f"Calc(a={self.a}, b={self.b})"

c1  =Calc(10,20)
c2 = Calc(20,30)
c3 = Calc(10,20)

k = c1+c2+c3
print(k)



