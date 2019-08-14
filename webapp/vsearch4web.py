from flask import Flask

from flask import render_template, request

from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

#letters = search4letters('Life, the Universe, and Everything!', 'eiour')

@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    return str(search4letters(phrase, letters))
    #return str(search4letters('Life, the Universe, and Everything!', 'eiour'))

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', 
        the_title='Welcome to search4letters on the web!')

app.run(debug=True)
