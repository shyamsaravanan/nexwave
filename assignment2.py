d={'ROM':'ROM Description','HDD':'HDD Description','FDD':'FDD Description','RAM':'RAM Description','CPU':'CPU Description'}
ch=input('Enter device name: ')
f=0
for i in sorted(d.keys()):
    if i==ch:
        print(d[i])
        f+=1
    elif i.startswith(ch)==True:
        print(d[i])
        f+=1
if f==0:
    print('Device Not Found..')
