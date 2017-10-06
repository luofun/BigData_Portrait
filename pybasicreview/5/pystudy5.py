def test1():
    import sys,os
    print(len(dir(sys)))
    print(len(dir(os)))
    print(dir(sys))
    print(sys.__doc__)
    help(sys)


def more(text,numlines=15):
    lines=text.splitlines()
    while lines:
        chunk=lines[:numlines]
        lines=lines[numlines:]
        for line in chunk:print(line)
        if lines and input('More?') not in ['y','Y']:break

def test1():
    import sys
    #more(open(sys.argv[1]).read(),10)
    more(sys.__doc__)

def test2():
    import os
    os.system('python test1.py')
    ttt=os.popen('python test1.py').read()
    print("ttt:"+ttt)
    ttt=os.popen('type test1.py').read()
    print(ttt)

def test3():
    import subprocess
    subprocess.call('python test1.py')
    subprocess.call('cmd /c "test1.py"')
    subprocess.call('type test1.py',shell=True)

def test4():
    from io import StringIO
    import sys
    buff=StringIO()
    temp=sys.stdout
    sys.stdout=buff
    print('aaaaaaaaaa')
    sys.stdout=temp
    print(buff.getvalue())

if __name__=='__main__':
    pass
    test4()
    
    