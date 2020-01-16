a = 10
b = 0
try:
    r = a/b
    print('r= ', r)
except:
    print('Some error')
d={}
try:
    print(d['A'])
    r2=a/b
    print('r2=',r2)
except ZeroDivisionError:
    print('In ZDE')
except NameError as n:
    print('NE= ',n)
except(KeyError,IndexError):
    print('KE or IE')
l=[]
try:
    print(l[1])
except Exception as e:#generic exception which tells all types of exceptions
    print('e= ',e)
    print('Type= ',type(e))
c=10
d=10
try:
    r=c/d
except:
    print('In except')
else:#try-else like for-else,while-else
    r=c/c
    print('In else')
try:
    r=c/d
except:
    print('In except')
finally:#In all cases this finally block will be executed
    print('In Finally')
#try-finally(order of execution)
#try-except-finally
#try-except-else-finally
e=10
f=0
try:
    if f==0:
        raise ZeroDivisionError
    print('stmt-100')
    r=e/f
except ZeroDivisionError:
    print('From raise')
result='Test case failed'
try:
    assert 'Success' in result,'Some test failed'
    print('Test case success')
except AssertionError as ae:
    print('ae= ',ae)
class MyError(Exception):
    def __init__(self,m):
        self.msg=m
    def __str__(self):
        return 'ERROR DETAILS: '+self.msg
try:
    if 'Success' not in result:
        raise MyError('Test Failed')
    else:
        print('Execution Success')
except MyError as me:
    print('me= ',me)