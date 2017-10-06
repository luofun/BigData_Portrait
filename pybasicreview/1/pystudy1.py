filename='aaa'
x1='enddb.'
x2='endrec.'
x3='=>'

def store(db,name=filename):
    dbfile=open(name,'w')
    for key in db:
        print(key,file=dbfile)
        for(name,value) in db[key].item():
            print(name+x1+repr(value),file=dbfile)
        print(x2,file=dbfile)
    print(x3,file=dbfile)
    dbfile.close()

def load(name=filename):
    dbfile=open(name)
    import sys
    sys.stdin=dbfile
    db={}
    key=input()
    while key !=x1:
        rec={}
        filed=input()
        while filed !=x2:
            name2,value=filed.split(x3)
            rec[name2]=eval(value)
            filed=input()
        db[key]=rec
        key=input()
    return db

class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name=name
        self.age=age
        self.pay=pay
        self.job=job
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay*=(1.0+percent)
    def __str__(self):
        return '<%s => %s: %s, %s>'%(self.__class__.__name__,self.name,self.job,self.pay)

class Manager(Person):
    def __init__(self,name,age,pay):
        Person.__init__(self,name,age,pay,'manager')
    def giveRaise(self, percent, bonus=0.1):
        self.pay*=(1.0+percent+bonus)
        

if __name__=="__main__":
    pass
    filex=open('aaaa','w')
    print('test\n',file=filex)
    filex.close()
    filey=open('aaaa')
    import sys
    concon=sys.stdin
    sys.stdin=filey
    key=input()
    print("input:"+ key + '\n')
    #print("file:" + filey +'\n')
    filey.close()
    from initdata import db
    print(db)
    import pickle
    file222=open("pickletest",'wb')
    pickle.dump(db,file222)
    file222.close()
    file333=open('pickletest','rb')
    db=pickle.load(file333)
    for key in db:
        print(key,'=>\n',db[key])
    print(db['sue']['name'])
    file333.close()
    print('-'*30)
    from initdata import bob,sue,tom
    for(key, record) in [('bob',bob),('sue',sue),('tom',tom)]:
        recfile=open(key+'.pkl','wb')
        pickle.dump(record,recfile)
        recfile.close()
    print('-'*30)
    import glob
    for filename in glob.glob('*.pkl'):
        recfile=open(filename,'rb')
        record=pickle.load(recfile)
        print(filename,'=>\n',record);
    suefile=open('sue.pkl','rb')
    print(pickle.load(suefile)['name'])
    print('-'*30)
    suefile=open('sue.pkl','rb')
    sue=pickle.load(suefile)
    suefile.close()
    sue['age']*=1.10
    suefile=open('sue.pkl','wb')
    pickle.dump(sue,suefile)
    suefile.close()
    import shelve
    db=shelve.open('people-shelve')
    db['bob']=bob
    db['sue']=sue
    db.close()
    db=shelve.open('people-shelve')
    for key in db:
        print(key,'=>\n',db[key])
    print(db['sue']['age'])
    db.close()
    print('-'*30)
    db=shelve.open('people-shelve')
    sue=db['sue']
    sue['age']*=1.50
    db['sue']=sue
    db['tom']=tom
    db.close()
    print('-'*30)
    db=shelve.open('people-shelve')
    print(db['sue']['age'])
    db.close()
    print('-'*30)
    bob=Person('Bob Smith',42,30000,'software')
    sue=Person('Sue Jones',45,40000,'hardware')
    print(bob.name,sue.pay)
    print(bob.name.split()[-1])
    sue.pay*=1.10
    print(sue.pay)
    print('-'*30)
    print(bob.lastName())
    sue.giveRaise(.10)
    print(sue.pay)
    print('-'*30)
    tom=Manager(name='tom doe',age=50,pay=50000)
    print(tom.lastName())
    tom.giveRaise(.20)
    print(tom.pay)
    print('-'*30)
    tom=Manager('Tom Jones',50,40000)
    print(tom)
    bob=Person('Bob Smith',44)
    sue=Person('Sue Jones',47,40000,'hardware')
    tom=Manager(name='Tom Doe',age=50,pay=50000)
    print(sue,sue.pay,sue.lastName())
    for obj in  (bob,sue,tom):
        obj.giveRaise(.10)
        print(obj)
    print('-'*30)
    db=shelve.open('class-shelve')
    db['bob']=bob
    db['sue']=sue
    db['tom']=tom
    db.close()
    print('-'*30)
    db=shelve.open('class-shelve')
    for key in db:
        print(key,'=>\n',db[key].name,db[key].pay)
    bob=db['bob']
    print(bob.lastName())
    print(db['tom'].lastName())
    print('-'*30)
    db=shelve.open('class-shelve')
    sue=db['sue']
    sue.giveRaise(.25)
    db['sue']=sue
    tom=db['tom']
    tom.giveRaise(.20)
    db['tom']=tom
    db.close()
    print('-'*30)
    newtext='ttt'
    record=Person(name='?',age='?')
    field='name'
    print(record)
    sys.stdin=concon
    print(concon)
    newtext=input('input:')
    setattr(record,field,newtext)
    #record.name=newtext
    print(record)
    print('-'*30)



