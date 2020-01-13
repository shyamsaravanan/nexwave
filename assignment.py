list1=[1,3,5,16,8]
list2=[6,5,9,4,13,12]
s=set(list1+list2)
l=list(s)
print(l)
def search(a):
    if a in l:
        print('Number is: ',a,'Index is: ',l.index(a))
    else:
        for j in l:
            if j>int(a):
                print('Number is: ',j,'Index is: ',l.index(j))
                break
        else:
                print('Not found')

b=int(input('Enter the number: '))
search(b)
