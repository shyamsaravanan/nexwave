#There are 3 ways to releasing the code
#1. Source code bt for this we need to install python
#2. Share the exe file
#We have copied this code in release1 so that we can make the exe file of this ie executable file of this
#pyinstaller is the 3rd party library to create exe file for which running we dont neend to ijnstall python
#pip install pyinstaller
#cd Releases
#cd release1
#pyinstaller -F searchprogram.py
#3. Trying to make a source file and wheel file  Go to https://packaging.python.org/->tutorials
'''This is functional representation
of this
>>> l=[10,20,30]
>>> dev_id_search(50,l)
'Dev ID found,Dev ID= 20Index= 1'
 '''
def dev_id_search(dev_id,dev_list):
    if dev_id in dev_list:
        return 'Dev ID found,Dev ID= '+str(dev_id)+'Index= '+str(dev_list.index(dev_id))
    elif dev_id>max(dev_list):
        return 'Not Found'
    else:
        for i in dev_list:
            if i>dev_id:
                return 'Value= '+str(i)+'Index= '+str(dev_list.index(i))
def main():
    l1 = [1, 3, 5, 16, 8]
    l2 = [6, 5, 9, 4, 13, 12]
    l3 = l1 + l2
    s = set(l3)
    l4 = list(s)
    l4.sort()
    while True:
        i=input('Enter id to search: ')
        i=eval(i)
        r=dev_id_search(i,l4)
        print('Search result:  ',r)
        ch=input('Quit(Y/N): ')
        if ch=='y':
            break
if __name__=='__main__':
    main()
    import doctest
    doctest.testmod()#Doctest executes the comment ie all examples written in docstring is proper or not on testing, we copied it from the python console by running the function dev_id_search()
#First comment is called the doctest



