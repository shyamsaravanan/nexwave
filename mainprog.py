import addmodule
print(addmodule.msg)
print(addmodule.add(10,20))
line='-'*40
print(line)
#2nd way
import sys
print(sys.path)
#sys.path.append(r'C:\Python Training\lib')
import addmodule as a
print(a.msg)
print(a.add(10,20))
print(line)
#3rd way
from addmodule import msg,add
print(msg)
print(add(10,20))
print(line)
#4th way
from addmodule import msg as m,add as a
print(m)
print(a(10,20))
print(line)
#5th way
from addmodule import *
print(msg)
print(add(10,20))
#import directory 1st way
import project.net.addmodule
print(project.net.addmodule.msg)
print(line)
#2nd way
import project.net.addmodule as a
print(a.msg)
print(line)
#3rd way
from project.net.addmodule import msg,add
print(msg)
print(line)