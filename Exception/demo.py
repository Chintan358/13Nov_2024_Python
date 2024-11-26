

print("program started")

try:
    a = 10
    b = a/0
    print(b)
except:
    print("err")

finally:
    print("always executable block")

    
print("Program ended")