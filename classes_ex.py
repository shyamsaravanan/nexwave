#multiple objects
#Inheritance
#Operator overloading
#Types of variable:
#-Local
#-Enclosed
#-Global
#-Instance-multiple use(adduser,viewuser are Instance methods); name is Instance variable
#-Class
#Two types of objects:Class object,Instance object
#cust1,cust2-Instance objects
#Account1-class object
#Create-__new__
#Initialize-__init__
class Account1:
    def adduser(self,n):
        self.name=n
    def viewuser(self):
        return self.name
    bank='SBI'#class variable
    @classmethod#decorator#Zero argument is not possible
    def bankrules(cls,area):#Zero argument is not possible
        return 'Bank Rules: '+area
    @staticmethod#zero argument is possible
    def bankinfo():
        return 'Bank Info'
    def __init__(self):#Like constructor
        print('SB Logic Here')
cust1=Account1()
cust2=Account1()
cust1.adduser('c1')#SB Logic Here is printed
cust2.adduser('c2')#SB Logic Here is printed
print(cust1.viewuser())
print(cust2.viewuser())
print(Account1.bank)
print(cust1.name)
print(Account1.bankrules('BLR'))
print(Account1.bankinfo())
Account1.viewuser(cust2)
class Account2(Account1):#Inheritance
    def addadhar(self,a):
        self.adhar=a
    def viewadhar(self):
        return self.adhar
    def viewuser(self):#Method overriding
        return 'Welcome '+self.name
    def __init__(self):
        super().__init__()#to call the super class(SB Logic Here is printed)
        print('CA Logic Here')
        Account1.__init__(self)#another way to call the super class(SB Logic Here is printed)
cust3=Account2()
cust3.adduser('c3')
print(cust3.viewuser())
print(Account2.bank)
print(Account2.bankrules('BLR'))
print(Account2.bankinfo())
cust3.addadhar('A1')
print(cust3.viewadhar())
class RBI:
    def viewrules(self):
        return 'RBI Rules'
class Account3(Account2,RBI):#Multiple inheritance
    pass
cust4=Account3()
print(cust4.viewrules())
cust4.adduser('c4')
class Govt:
    def viewrules(self):
        return 'Govt Rules'
class Account4(Account3,Govt):
    pass
cust5=Account4()
print(cust5.viewrules())#RBI Rules is displayed because it is found first
print(Govt.viewrules(cust5))#For displaying Govt Rules
class Account5(Account3):
    def __init__(self):
        self.gov=Govt()
cust6=Account5()
print(cust6.viewrules())
print(cust6.gov.viewrules())
class Account6:
    def __init__(self,n):
        self.name=n
    def __add__(self, x):
        return self.name+x.name
    def __str__(self):
        return self.name
    def __len__(self):
        return len(self.name)
    def __iter__(self):
        self.count=0
        return self
    def __next__(self):
        c=self.count
        if c<len(self.name):
            self.count+=1
            return self.name[c]
        else:
            raise StopIteration
cust7=Account6('abc')
cust8=Account6('xyz')
result=cust7+cust8#cust7.__add__(cust8)
print('Result= ',result)
print('cust7= ',cust7)
print('Length= ',len(cust7))
for i in cust7:
    print('i= ',i)
from abc import ABC,abstractmethod#abc-abstract base class
class Account(ABC):#creating abstract class
    def adduser(self,a):
        self.name=a
    @abstractmethod
    def viewuser(self):#abstract method
        pass
#a=Account()
class MyAccount(Account):
    def viewuser(self):
        return 'Hello '+self.name
b=MyAccount()
b.adduser('B')
print(b.viewuser())
