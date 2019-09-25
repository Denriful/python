#! /usr/bin/env python3

from flask import Flask, render_template, request, escape, session

from vsearch import search4letters

#import mysql.connector

from DBcm import UseDatabase, ConnectionError, CredentialError, SQLError

from checker import check_logged_in

from time import sleep

app = Flask(__name__)

app.secret_key = 'YouWillNeverGuess2'

app.config['dbconfig'] = { 'host': '127.0.0.1', 
        'user': 'vsearch', 
        'password': '34512',
        'database': 'vsearhlogDB', }

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out'

@app.route('/search4', methods=['POST'])
def do_search():
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)

    return render_template('results.html', 
        the_phrase=phrase, 
        the_letters=letters,
        the_title=title,
        the_results=results,)    
 
@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html', 
        the_title='Welcome to search4letters on the web!')

def log_request(req: 'flask_request', res: str) -> None:
    
 #   dbconfig = { 'host': '127.0.0.1', 
 #       'user': 'vsearch', 
 #       'password': '34512',
 #       'database': 'vsearhlogDB', }

 #   conn = mysql.connector.connect(**dbconfig)

 #   cursor = conn.cursor()
    #sleep(15)
    
    #raise ConnectionError()
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:

            _SQL = '''insert into log
                (phrase, letters, ip, browser_string, results)
                values
                (%s, %s, %s, %s, %s)'''

            cursor.execute(_SQL, (req.form['phrase'],
                req.form['letters'], 
                req.remote_addr,
                req.user_agent.browser,
                res, ))
    except ConnectionError as err:
         print('Is your DB switched on?:', str(err))  
    except CredentialError as err:
         print('User-id/Password issues. Error:', str(err)) 
    except SQLError as err:
         print('Is your query correct? Error:', str(err))       
    except Exception as err:
        print('Something went wrong: ', str(err))  
        return 'Error'

 #   conn.commit()
    
   # _SQL = '''select * from log'''

 #   cursor.close()
    
  #  conn.close()



    #with open('vsearch.log','a') as log:

    """ this is how to print 'flask request' attributes """
        #print(dir(req),res, file=log)

        #print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')
        



@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
 #   contents = []
 #   with open('vsearch.log') as log:        
 #       for line in log:       
 #           contents.append([])
  #          for item in line.split('|'):
 #               contents[-1].append(escape(item))
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = '''select phrase, letters, ip, browser_string, results
            from log'''
 
        cursor.execute(_SQL)

        contents = cursor.fetchall()

        titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')

        #contents = log.readlines()
        #return escape(''.join(contents))
        #return str(contents)
        return render_template('viewlog.html', 
                                the_title='View Log',
                                the_row_titles=titles,
                                the_data=contents,)



if __name__ == "__main__":    
    app.run(debug=True)
