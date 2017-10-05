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

if __name__=="__main__":
    pass
    filex=open('aaaa','w')
    print('test\n',file=filex)
    filex.close()
    filey=open('aaaa')
    import sys
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
    
