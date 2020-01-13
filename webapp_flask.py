import flask
#How to create website
app=flask.Flask('MyApp')
#app.run()
@app.errorhandler(404)
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
@app.route('/Verify',methods=['post'])#method should be same as the login page
def verifypage():
    u=flask.request.form.get('uname')
    p=flask.request.form.get('pw')
    if not(u=='abc'and p=='xyz'):
        return 'Login failed'
    else:
        #return 'Login Success'
        import sqlite3
        con=sqlite3.connect('mydb.sqlite3')
        cur=con.cursor()
        cur.execute('SELECT * FROM LOGDATA')
        result=cur.fetchall()
        return flask.render_template('report.html',res=result)
@app.route('/download/<filename>')
def staticfile(filename):
    return flask.send_from_directory(directory=r'C:\Python Training\bin',filename=filename)
@app.route('/empid/<int:eid>')
def empid(eid):
    d={'name':'abc','empid':eid}
    return d
@app.route('/logdata')
def logdata():
    return flask.redirect('/login')
@app.route('/passwords')
def passwords():
    return flask.abort(201,'Access Denied')
app.run(host='192.168.3.237',port=8080)
