#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
# from flask.ext.script import Manager

app = Flask(__name__)
bootstrap = Bootstrap(app)
# manager = Manager(app)

# @app.route('/')
# def index():
#     return '<h1>Hello World</h1>'

# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello %s</h1>' % name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
    # manager.run()
