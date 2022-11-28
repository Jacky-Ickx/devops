from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html', welcome_message = generate_welcome_message())

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

def generate_welcome_message():
    return "Welcome to DHBW"

def add (x, y):
    """the sole purpose of this function is to be unit-tested"""
    return x + y

if __name__ == '__main__':
   app.run()