# Importerer Flask for å lage webapplikasjonen og render_template for å rendere HTML maler
from flask import Flask, render_template
# Importerer data fra data.py
from data import KONTAKT_INFO, MENY_ITEMS, VARER_ITEMS

# Initialiserer en flask app
app = Flask(__name__)

# Definerer en rute for hovedsiden ('/')
@app.route('/')
def index():
    # Viser index.html malen
    return render_template('index.html')

# Definerer en rute for kontaktsiden /kontakt
@app.route('/kontakt')
def kontakt():
    # Viser kontakt.html malen og sender med kontaktinformasjon
    return render_template('kontakt.html', kontakter=KONTAKT_INFO)

# Definerer en rute for menysiden ('/meny')
@app.route('/meny')
def meny():
    # Viser meny.html-malen og sender med meny-data
    return render_template('meny.html', meny=MENY_ITEMS)

# Definerer en rute for varesiden ('/varer')
@app.route('/varer')
def varer():
    # Viser varer.html malen og sender med vare data
    return render_template('varer.html', varer=VARER_ITEMS)

# Kjører appen hvis skriptet blir kjørt direkte
if __name__ == '__main__':
    app.run(debug=True)