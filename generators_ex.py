t1=(10,20,30)
t2=(i for i in range(10))#generator
print('t1= ',t1)
print('t2= ',t2)
print('list(t2)= ',list(t2))
l=[1,2,3,4]
def squares(m):
    res=[]
    for j in m:
        r=j*j
        res.append(r)
    return res
r1 = squares(l)
for a in r1:
    print('a= ',a)
def gen_squares(N):
    for k in N:
        yield k*k
    for l in N:
        yield l*l#can use multiple yields
r2=gen_squares(l)
for b in r2:
    print('b= ',b)
print('r1= ',r1)
print('r2= ',list(r2))#empty list is printed as r2 is used for printing with b and its use is over.So its empty now(generator)