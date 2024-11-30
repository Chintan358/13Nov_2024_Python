class Test : 
    
    # def add(self,a,b,c):
    #     print(a+b+c)
    # def add(self,a,b):
    #     print(a+b)
    def add(self,*a):
        sum = 0
        for i in a:
            sum +=i
        print(sum)

t  =Test()
t.add(10,20)
t.add(10,20,30)