from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'YouWillNeverGuess'

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.' #+ str(session.values())

@app.route('/logout')
def do_logout():
    session.pop('logged_in')
    #return str(session.values())
    return 'You are now logged out'

@app.route('/status')
def status() -> str:
    if 'logged_in' in session:
        return 'You are currently logged in.'
    return 'You are not logged in.'

@app.route('/')
def hello() -> str:
    return 'Hello from simple webapp.'

@app.route('/page1')
def page1() -> str:
    return 'This is page 1.'

@app.route('/page2')
def page2() -> str:
    return 'This is page 2.'

@app.route('/page3')
def page3() -> str:
    return 'This is page 3.'

if __name__ == '__main__':
    app.run(debug=True)
