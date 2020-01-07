a=10
if a==10:
    print('a=10')
if a>10:
    print('a>10')
if a<10:
    print('a<10')

a=10
if a==10:
    print('a=10')
elif a>10:
    print('a>10')
elif a<10:
    print('a<10')

a=10
if a==10:
    print('a=10')
elif a>10:
    print('a>10')
else:
    print('a<10')
s='python'
if 'th' in s:
    print('Substring found')
if not s.startswith('java'):
    print('Not Java')
if s!='c++':
    print('Not c++')
if s[1:3]=='yt':
    print('yt found')
l1=[10,20]
l2=l1
l3=l1.copy()
if 20 in l1:
    print('20 found')
if l1 is l2:
    print('Both refers same object')
if id(l1)==id(l2):
    print('Both refers same object')
if l1==l3:
    print('Contents are same')
d={'A':10,'B':20}
if 'B' in d:
    print('Key B found')
if 'B' in d.keys():
    print('Key B found')
if 20 in d.values():
    print('20 found')
if ('A',10) in d.items(): #[('A',10),('B',20)]
    print('Item found')
if a==10:
    pass
