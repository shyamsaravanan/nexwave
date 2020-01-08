count = 0
def create_Acc():
    global count
    count+=1
def delete_Acc():
    global count
    count-=1
create_Acc()
create_Acc()
count=100
delete_Acc()
print('Total Accounts= ',count)
def Acc():
    c=0;
    def CA():
        nonlocal c
        c+=1
    def DA():
        nonlocal c
        c-=1
    def TA():
        print('Total= ',c)
    return CA,DA,TA
x=(10,20)
x,y=(10,20)
f1,f2,f3=Acc()
f1()
f1()
c=100
f2()
f3()


