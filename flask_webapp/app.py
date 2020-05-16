from flask import Flask
from flask import render_template
from flask import send_from_directory

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index_view():
    return render_template('index.html')

@app.route('/train')
def train_view():
    return render_template('train.html')

@app.route('/test')
def test_view():
    return render_template('test.html')
    
if __name__ == '__main__':
    app.run(debug=True, port=5201)