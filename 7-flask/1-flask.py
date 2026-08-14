from  flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return 'eae suave?'

@app.route('/sobre')
def sobre():
    return"""
        <b>ProgramandoFlask</b>: assista os videos sobre
        <a href='https://www.youtube.com/watch?v=1JpYOqvDJNU&t=252s'>Pandas</a>
"""
app.run(debug=True)