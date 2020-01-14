'''This is Procedural Programming to
search for a id in the joint list of elements'''
l1=[1,3,5,16,8]
l2=[6,5,9,4,13,12]
l3=l1+l2
s=set(l3)
l4=list(s)
l4.sort()
while True:
    in_val=input('Enter Device ID: ')
    in_val=int(in_val)
    if in_val in l4:
        print('Device ID Found,ID= ',in_val,'ItsIndex:',l4.index(in_val))
    elif in_val>max(l4):
        print('Not Found')
    else:
        for i in l4:
            if i>in_val:
                print('Value= ',i,'Index= ',l4.index(i))
                break
    ch=input('Do you wanna Quit?(Y/N): ')
    if ch=='y':
        break