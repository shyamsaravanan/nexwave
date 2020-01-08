#POSITIONAL ARGS
#with default values
def add(a,b=10):
    return a+b
r=add(10)
print('r= ',r)
def get_ips(file_path,mode='r'):
    f=open(file_path)
    if file_path.endswith('.csv'):
        ips=[line.split(',')[0] for line in f]
        return ips
    else:
        ips=[line.split()[0] for line in f]
        return ips
r=get_ips('log_report.txt','r')
print('r= ',r)
