#POSITIONAL ARGS
def add(a,b):
    return a+b
r=add(10,20)
print('r= ',r)
def get_ips(file_path,mode):
    f=open(file_path)
    if file_path.endswith('.csv'):
        ips=[line.split(',')[0] for line in f]
        return ips
    else:
        ips=[line.split()[0] for line in f]
        return ips
r=get_ips('log_report.txt','r')
print('r= ',r)
