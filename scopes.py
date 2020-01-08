x=10
def f1():
   #x=20 #ENCLOSED
    def f2():
        #nonlocal x #refers to the enclosed variable
        #x=200
        global y
        y=200
        print('F2= ',x)
    f2()
    print('F1= ',x)
f1()
print('Global= ',x,y)
print(dir(__builtins__))#print the built ins available

