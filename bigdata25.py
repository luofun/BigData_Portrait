
import multiprocessing
import time

def func(msg):
  for i in xrange(3):
    print(msg)
    time.sleep(1)

def test1():
  p = multiprocessing.Process(target=func, args=("hello", ))
  p.start()
  p.join()
  print ("Sub-process done.")

def test2():
    pool = multiprocessing.Pool(processes=4)
    for i in xrange(10):
        msg = "hello %d" %(i)
        pool.apply_async(func, (msg, ))
    pool.close()
    pool.join()
    print( "Sub-process(es) done.")

def test3():
    pool = multiprocessing.Pool(processes=4)
    result = []
    for i in xrange(10):
        msg = "hello %d" %(i)
        result.append(pool.apply_async(func, (msg, )))
    pool.close()
    pool.join()
    for res in result:
        print (res.get())
    print ("Sub-process(es) done.")