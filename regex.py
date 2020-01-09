import sqlite3
con=sqlite3.connect('mydb.sqlite3')
#import pymysql
#con=pymysql.connect(user='',password='',host='',port='',database='')
cur=con.cursor()
query='''CREATE TABLE IF NOT EXISTS LOGDATA(IP VARCHAR(100),
DATE VARCHAR(100),
PICS VARCHAR(100),
URL VARCHAR(100))'''
cur.execute(query)
import urllib.request as u
myurl='https://www.jafsoft.com/searchengines/log_sample.html'
f=u.urlopen(myurl)
import re
for line in f:
    #print(line)
    #print(type(line))
    line=line.decode()
    #print(type(line))
    # \w- word char-[a-zA-Z0-9_]
    # \W- non-word-[^a-zA-Z0-9_]
    # \S- non-space
    m=re.match('(\d\d\d\.\d{3}[.]\d{1,3}\.[0-9]{3}).*?(\d{1,2}/[a-zA-Z]{3}/\d{4}).*(?:GET|POST)\s+/(?:pics/(\w+\.\w+))?.*(http://\S+)</A>.*',line)
    if m!=None:
        ip=m.group(1)
        dt=m.group(2)
        im=m.group(3)
        if im==None:
            im='No image'
        wb=m.group(4)
        print(ip,dt,im,wb)
        query=f"INSERT INTO LOGDATA VALUES('{ip}','{dt}','{im}','{wb}')"
        print(query)
        cur.execute(query)
con.commit()
cur.execute('SELECT * FROM LOGDATA')
result=cur.fetchall()
print('Result= ',result)
import csv
f=open('dbdump.csv','w',newline='')
wt=csv.writer(f)
wt.writerow(['IP','DATE','PICS','URL'])
for eachrow in result:
    wt.writerow(eachrow)
f.close()
f=open('dbdump.csv')
rdr=csv.reader(f)
csv_out=list(rdr)
print('csv_out= ',csv_out)
import pandas as pd
df1=pd.DataFrame([[10,20,30],[40,50,60]],index=['r1','r2'],columns=['c1','c2','c3'])
print(df1)
l1=list([[10,20,30],[40,50,60]])
print(l1)
df2=pd.DataFrame(result)
print(df2)
df2.to_csv('out3.csv',index=None,header=['IP','DATE','PICS','URL'])
cur.execute('SELECT * FROM LOGDATA')
df3=pd.DataFrame(cur)
df3.to_csv('out4.csv')
df3.to_excel('out5.xlsx')
df4=df3.T
df4.to_json('out6.json')


