from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    thought = request.form['thought']
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('journal.txt', 'a') as f:
        f.write(f"{timestamp} - {thought}\n")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)