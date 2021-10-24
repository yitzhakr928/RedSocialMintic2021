from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def feed():
    return render_template('feed.html')

if __name__ == '__main__':
    app.run(debug=True,port=5000)