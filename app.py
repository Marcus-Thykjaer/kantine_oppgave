from flask import Flask, render_template
from data import KONTAKT_INFO, MENY_ITEMS, VARER_ITEMS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html', kontakter=KONTAKT_INFO)


@app.route('/meny')
def meny():
    return render_template('meny.html', meny=MENY_ITEMS)


@app.route('/varer')
def varer():
    return render_template('varer.html', varer=VARER_ITEMS)

if __name__ == '__main__':
    app.run(debug=True)
