from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/training')
def training():
    return render_template('training.html')

@app.route('/players')
def players():
    return render_template('players.html')

if __name__ == '__main__':
    app.run(debug=True)
