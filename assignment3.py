f2=open('SSH_log_Sample.txt','r')
c=0
l=[]
for line in f2:
    if 'Failed' in line:
        c+=1
    if 'version' in line:
        l=line.split()
    if 'private host key' in line:
        e=line.split()
    if 'Accepted' in line:
        u=line.split()
print('Number of failed login attempts: ',c)
print('sshd version: ',l[l.index('version')+1][:-1])
a=e[e.index('key')+3]
print(a)
b=a[:a.index(':')]
print('Encryption: ',b)
print('Successful Login User: ',u[u.index('Accepted')+3])
print('ip: ',u[u.index('Accepted')+5])
print('port: ',u[u.index('Accepted')+7])
