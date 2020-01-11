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
        return 'Login Success'

app.run(host='192.168.3.237',port=8080)
