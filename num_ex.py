#core Data types
#Numbers
a=10#int        
b=12.5#float
c=0X12#hex
d=0b1010#bin
e=0o12#octal
#Strings
'''
List
Tuple
'''
"""
Dictionary
Set
"""
print('Hello')
print('a')
print('Result=',a,b,c,d,e,sep='|',end='.')
print('Test')#file=,flush=
f=int(20)
print(f)
print(a)
print(id(a))
print(type(a))
print(type(a).__name__)
a=100
print(id(a))
b=a #reference copy
a=200
b=300
#sys.getRefcount