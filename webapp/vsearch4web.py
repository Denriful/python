from flask import Flask

from flask import render_template, request, escape

""" relative import for 
support Heroku
annotations disabled for compatibility with Heroku
"""
from vsearch import search4letters

app = Flask(__name__)

#letters = search4letters('Life, the Universe, and Everything!', 'eiour')

@app.route('/search4', methods=['POST'])


#def do_search() -> 'html':
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
    #return str(search4letters(phrase, letters))
    #return str(search4letters('Life, the Universe, and Everything!', 'eiour'))

@app.route('/')
@app.route('/entry')
#def entry_page() -> 'html':
def entry_page():
    return render_template('entry.html', 
        the_title='Welcome to search4letters on the web!')

def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log','a') as log:

        """ this is how to print 'flask request' attributes """
        #print(dir(req),res, file=log)

        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

@app.route('/viewlog')
def view_the_log() -> str:
    contents = []
    with open('vsearch.log') as log:        
        for line in log:       
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
        #contents = log.readlines()
        #return escape(''.join(contents))
        return str(contents)



if __name__ == "__main__":    
    app.run(debug=True)
