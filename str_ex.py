a='PERSON'
print(a)
b="PERSON'S"
c='''PERSON'S Height XYZ"'''
d="""PERSON"""
print(b,c,d,sep='\n')
S1='Hello'
S2='py'
S3=S1+S2
S4=S1*10
print(S3,S4)
line='-'*40
print(line)
e='PERSON\'S'
print(e)
f=r'C:\newfolder\test.py'
print(f)
g='WEL COME'
print(g)
print(len(g))
print(g[1])
print(g[1:6])
print(g[1:])
print(g[:6])
print(g[:])
h=g[:]
print(id(h),id(g))
#step
print(g[1:6:1])
print(g[1:6:2])
#reverse
print(g[::-1])
print(g[6:1:-2])
#-ve index
print(g[-7:-2])
print(g[len(g)-4:])
print(g[-4:])
#str
i=10
j=str(i)
k=str('python')
print(i,j,k,sep='\n')
r1=g.startswith('WEL')
print('r1=',r1)
r2=g.endswith('ME')
print('r2=',r2)
r3=g.isupper()
r4=g.upper()
print(r3,r4,sep='\n')
r5=g.islower()
r6=g.lower()
print(r5,r6,sep='\n')
l='abc'
r7=l.isalpha()
m='123'
r8=m.isdigit()
n='abc123'
r9=n.isalnum()
print(r7,r8,r9,sep='\n')
r10=n[-3:].isdigit()
print(r10)
r11=g.count('E')
print('r11=',r11)
r12=g.index('E')
r13=g.find('E')
print(r12,r13)
r14=g.index('E',3)
r15=g.index('E',3,8)
print(r14,r15)
r16=g.rindex('E')
print('r16=',r16)
p=' wel come '
r17=p.strip()
r18=p.lstrip()
r19=p.rstrip()
print(r17,r18,r19,sep='\n')
q='[wel[come][]'
r20=q.strip(']w[e')
r21=q.lstrip('w[')
r22=q.rstrip('][e')
print(r20,r21,r22)
r23=g.replace('E','e')
print('r23=',r23)
r24=g.split()
r25=g.split('E')
x=10
y=20
z=x+y
r26='add of X and Y is Z'
r27='add of {} and {} is {}'.format(x,y,z)
r28='add of {1} and {0} is {2}'.format(x,y,z)
#py version>3.5
r29=f'add of {x} and {y} is {z}'
r30='-'.join(g)
r31='xyz'.join(r24)
print(r26,r27,r28,r29,r30,r31)
