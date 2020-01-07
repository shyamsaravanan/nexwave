#dict-class
d={'course':'python','dur':10,'loc':'blr'}
print(d['course'])
#add or update
d['course']=['c++','java']
print(d)
e=d.copy()
#remove
r1=d.pop('course')
print('pop=',r1,d)
del d['dur']
print('After del=',d)
r2=d.popitem()
print('r2=',r2,d)
k=e.keys()
v=e.values()
i=e.items()
print(k,v,i,sep='\n')
