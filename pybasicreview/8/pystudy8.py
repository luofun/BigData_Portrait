def test1():
    import sys
    print('bye')
    sys.exit(42)
    print('never')
    return

def test2():
    try:
        test1()
    except SystemExit:
        print('ignored')
    return

def test3():
    import os
    print('bye')
    os._exit(99)
    print('never')
    return

def test4():
    try:
        test3()
    except:
        print('ignored')
    return

def test5():
    import os
    exitstat=0
    def child():
        global exitstat
        exitstat+=1
        print('hello from child ', os.getpid(),exitstat)
        os._exit(exitstat)
        print('never')
        return
    def parent():
        while True:
            newpid=os.fork()
            pass
        #no in windows

    return

def test6():
    import _thread as thread
    #exitstat=0
    def child():
        global exitstat
        exitstat+=1
        threadid=thread.get_ident()
        print('hello child',threadid,exitstat)
        thread.exit()
        print('never')
    def parent():
        while True:
            thread.start_new_thread(child,())
            if input()=='q':break
    parent()
    return

def test7():
    import threading,sys,time
    def action():
        sys.exit()
    threading.Thread(target=action).start()
    time.sleep(2)
    print('main')



if __name__=='__main__':
    exitstat=0
    test7()