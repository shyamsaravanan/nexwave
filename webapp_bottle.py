import bottle
#How to create website
app=bottle.Bottle()
#app.run()
@app.error(404)
def errorpage(err):
    return 'Page under Construction'
@app.route('/')
def indexpage():
    return 'Welcome'
@app.route('/about')
def aboutpage():
    return '<b> This is about</b>'
@app.route('/login')
def loginpage():
    return '''<form action='/Verify' method='post'>
    USER NAME:<input type='text' name='uname'/><br/>
    PASSWORD:<input type='password' name='pw'/><br/>
             <input type='submit' value='LOGIN'/>
    </form>'''
@app.route('/Verify',method='post')#method should be same as the login page
def verifypage():
    u=bottle.request.forms.get('uname')
    p=bottle.request.forms.get('pw')
    if not(u=='abc'and p=='xyz'):
        return 'Login failed'
    else:
        #return 'Login Success'
        bottle.TEMPLATE_PATH.append(r'C:\Python Training\bin')
        import sqlite3
        con=sqlite3.connect('mydb.sqlite3')
        cur=con.cursor()
        cur.execute('SELECT * FROM LOGDATA')
        result=cur.fetchall()
        return bottle.template('report.tpl',res=result)
@app.route('/download/<filename>')
def staticfile(filename):
    return bottle.static_file(root=r'C:\Python Training\bin',filename=filename)
@app.route('/empid/<eid:int>')
def empid(eid):
    d={'name':'abc','empid':eid}
    return d
@app.route('/nameid/<nid:re:[a-z0-9]+>')
def name_id(nid):
    return str(nid)
@app.route('/logdata')
def logdata():
    return bottle.redirect('/login')
@app.route('/passwords')
def passwords():
    return bottle.abort(201,'Access Denied')

app.run(host='192.168.3.237',port=8080)
