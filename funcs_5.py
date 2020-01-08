#variable Args
def add(a,b=10,*c):
    print('Extra Args passed= ',c)
    r=a+b+sum(c)
    return r
res1=add(10)
print('res1= ',res1)
print('-'*40)
res2=add(10,20,30,40,50)
print('res2= ',res2)
def telnet(host=None, port=None, *cmds): #packing
    import subprocess
    result=[]
    for each_cmd in cmds:
        r=subprocess.check_output(each_cmd,shell=True)
        result.append(r)
    return result
r=telnet(0,0,'dir','type log_report.csv')
print('r= ',r)
f=open('cmd_out.txt','w')
r=[line.decode() for line in r]
f.writelines(r)
f.close()
c=['dir','type log_report.txt']
r2=telnet(0,0,*c) #unpacking

