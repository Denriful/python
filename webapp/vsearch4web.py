from flask import Flask

from flask import render_template, request

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

if __name__ == "__main__":    
    app.run(debug=True)
