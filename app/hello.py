#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from flask import request
# from flask import make_response
from flask import redirect

# @app.route('/')
# def index():
#     user_agent = request.headers.get('User-Agent')
#     return '<p>Your browser is %s</p>' % user_agent

# @app.route('/')
# def index():
#     response = make_response('<h1>This document carries a cookie!</h1>')
#     response.set_cookie('answer', '42')
#     return response

@app.route('/')
def index():
    return redirect('http://www.example.com')
