/
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Team Edge! Flask server is up and running'

@app.route('/about')
def about():
    return '<h1>About</h1><p>More content</p>'
@app.route('/nasa')
def show_nasa_pic():
    today =str(date.today())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
