from flask import Flask

from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

#letters = search4letters('Life, the Universe, and Everything!', 'eiour')

@app.route('/search4')
def do_search() -> str:
    return str(search4letters('Life, the Universe, and Everything!', 'eiour'))

app.run()
