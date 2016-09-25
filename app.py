from flask import Flask, render_template
import flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask_god/')
def question():
    return flask.jsonify(**{'question':'Who am I?'})


if __name__ == '__main__':
    app.run()
