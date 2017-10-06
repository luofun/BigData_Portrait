#!C:\Users\LENOVO\AppData\Local\Programs\Python\Python35

def test1():
    import cgi
    form=cgi.FieldStorage()
    print('Cotent-type:text/html\n')
    print('<title>Reply Page</title>')
    if not 'user' in form:
        print('<h1>who are you</h1>')
    else:
        print('<h1>hello <i>%s</i>!</h1>'%cgi.escape(form['user'].value))


if __name__=='__main__':
    #print('test')
    test1()