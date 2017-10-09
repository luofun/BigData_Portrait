def test1():
    import os
    print('test value:\n'+str(os.popen('dir /B').readlines())+'\n'+'-'*30)

def test2():
    import glob
    print(glob.glob('*'))
    print(glob.glob('*.py'))
    import os
    os.system('dir')
    os.system('cd C:\\Users\\LENOVO\\Documents\\Visual Studio 2013\\Projects\\')#fail to use cd
    os.system('dir')
    print(glob.glob('*'))

def test3():
    import os 
    for(dirname,subshere,fileshere) in os.walk(r'C:\Users\LENOVO\Desktop'):
        print('['+dirname+']')
        for fname in fileshere:
            print(os.path.join(dirname,fname))

def mylister(currdir):
    import os
    print('['+currdir+']')
    for file in os.listdir(currdir):
        path=os.path.join(currdir,file)
        if not os.path.isdir(path):
            print(path)
        else:
            mylister(path)

def test4():
    import sys
    print(str(sys.getdefaultencoding())+'\n'+str(sys.getfilesystemencoding()))

if __name__=='__main__':
    pass
    test4()
    #mylister('.')