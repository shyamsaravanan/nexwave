f1=open('log_report.txt','w')
f2=open('log_report.csv','w')
f1.write('IP\tDATE\tPICS\tURL')
f2.writelines(['IP,','DATE,','PICS,','URL\n'])
f3=open(r'C:\Python Training\log\Serverlog.txt')
for line in f3:
    if line[:3].isdigit():
        #print(line)
        sp=line.split()
        #print(sp)
        ip=sp[0]
        #print(ip)
        dt=sp[3]
        dt1=dt[1:12]#extracting date
        dt2=dt[1:dt.index(':')]#another method of extracting date
        #print(ip,dt2)
    #if sp[6].startswith('/pics')
        if 'pics' in sp[6]:
            im=sp[6] #'/pics/abc.jpg'
            im1=im[6:] #one way
            im2=im.split('/') #['','pics','abc.jpg']
            im2=im2[-1] #second way
            im3=im.lstrip('/pics/') #third way
            im4=im.replace('/pics/','') #fourth way
        else:
            im1='No image'
        url=sp[10][1:-1]
        print(ip,dt2,im1,url,sep='\t',file=f1)
        print(ip,dt2,im1,url,sep=',',file=f2)
f1.close()
f2.close()
f3.close()
