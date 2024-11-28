# f =  open("test.txt",'r')
# data = f.read()
# print(data)
# f.close()


# f = open("Home.txt",'w')
# f.write("This is a test file.\n")
# f.close()


# f = open("Home.txt",'a')
# f.write("This is a  test file.\n")
# f.close()

# with open("Home.txt") as f:
#     data = f.read()
#     print(data)

# with open("E:\\Chintan_wok\\13nov_2024_Python\\Basic\\demo.py",'r') as f:
#     while True:
#         data = f.readline()
#         if not data:
#             break
#         print(data,end="")
    

# with open("test.txt",'r+') as f:
#     f.write("d")
#     f.seek(0)
#     data = f.read()
#     print(data)

# with open("test.txt",'w+') as f:
#     f.write("d")   
#     f.seek(0)
#     data = f.read()
#     print(data)


# f = open("test.txt",'r')
# print(f.tell())
# f.seek(5)
# print(f.tell())
# data = f.read()
# print(data)
# print(f.tell())
# f.close()

    

# f = open("fan.jfif","wb")
# data = f.read()
# print(data)

import os

# os.mkdir("test")
os.rmdir("test")

