def add1(a,b):
    print('Result= ')
    print(a+b+a)
    print('End of Result')
def sub1(a,b):
    print('Result= ')
    print(a-b)
    print('End of Result')
#add1(10,20)
#sub1(10,20)
#MyDecorator
def mydec(func):
    #def decorated_func(x,y):
    def decorated_func(*x, **y):
        print('Result is: ')
        func(*x,**y)
        print('End of Result')
    return decorated_func
@mydec
def add2(a,b):
    print(a+b+b)
add2(10,20)
#How @mydec works?
def add3(a,b):
    print(a+b)
f=mydec(add3)
#f-decorated_func
f(100,200)
@mydec
def add4(a,b,c):
    print(a+b+c)
add4(10,20,30)
