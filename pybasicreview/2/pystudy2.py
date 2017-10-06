from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
import shelve

def test1():
    
   
    def reply():
        showinfo(title='popup',message='button pressed!')

    window=Tk()
    buttun=Button(window,text='press',command=reply)
    buttun.pack()
    window.mainloop()

class MyGui(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        button=Button(self,text='hello',command=self.reply)
        button.pack()
    def reply(self):
        showinfo(title='hi',message='button down')

def test2():
    window=MyGui()
    window.pack()
    window.mainloop()

def test3():
    mainwin=Tk()
    Label(mainwin,text=__name__).pack()
    popup=Toplevel()
    Label(popup,text='aaaa').pack(side=LEFT)
    MyGui(popup).pack(side=RIGHT)
    mainwin.mainloop()

class CustomGui(MyGui):
    def reply(self):
        showinfo(title='popup',message='Ouch!')


def test4():
    CustomGui().pack()
    mainloop()

def test5():
    def reply(name):
        showinfo(title='reply',message='hello%s'%name)

    top=Tk()
    top.title('echo')
    #top.iconbitmap('py-blue-trans-out.ico')
    Label(top,text='name:').pack(side=TOP)
    ent=Entry(top)
    ent.pack(side=TOP)
    btn=Button(top,text='submit',command=(lambda:reply(ent.get())))
    btn.pack(side=LEFT)
    top.mainloop()

shelvename='class-shelve'
fieldnames=('name','age','job','pay')

def makeWidgets():
    global entries
    window=Tk()
    window.title('people shelve')
    form=Frame(window)
    form.pack()
    entries={}
    for(ix,label) in enumerate(('key',)+fieldnames):
        lab=Label(form,text=label)
        ent=Entry(form)
        lab.grid(row=ix,column=0)
        ent.grid(row=ix,column=0)
        entries[label]=ent
    Button(window,text='fetch',command=fetchRecord).pack(side=LEFT)
    Button(window,text='updata',command=updataRecord).pack(side=LEFT)
    Button(window,text='quit',command=window.quit).pack(side=RIGHT)
    return window

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

def fetchRecord():
    key=entries['key'].get()
    try:
        record=db[key]
    except:
        showerror(title='error',message='no')
    else:
        for field in fieldnames:
            entries[field].delete(0,END)
            entries[field].insert(0,repr(getattr(record,field)))

def updataRecord():
    key=entries['key'].get()
    if key in db:
        record=db[key]
    else:
        record=Person(name='?',age='?')
    for field in fieldnames:
        setattr(record,field,entries[field].get())
    db[key]=record 

db=shelve.open(shelvename)

def test6():
    
    window=makeWidgets()
    window.mainloop()
    #db.close()

if __name__=="__main__":
    pass
    #test1()
    #test2()
    #test3()
    #test4()
    #test5()
    test6()
    db.close()
           
                
                    