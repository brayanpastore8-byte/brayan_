from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'db_portal_secret_key' # Fondamentale per le sessioni

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/appuntamento')
def appuntamento():
    return render_template('appuntamento.html')

@app.route('/prestiti')
def prestiti():
    return render_template('prestiti.html')

@app.route('/assicurazioni')
def assicurazioni():
    return render_template('assicurazioni.html')

@app.route('/patrimonio')
def patrimonio():
    return render_template('patrimonio.html')

@app.route('/info')
def info():
    return render_template('info.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
