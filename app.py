#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)
@app.route('/square/<a>')
def square(a):
    a= int(a)
    return str(a*a)+"\n"

@app.route('/cube/<b>')
def cube(b):
    b= int(b)
    return str(b*b*b)+"\n"

@app.route('/')
def intro():
    return "This is an arithmetic calculator\n"

if _name_ == '_main_':
    app.run(host='0.0.0.0')  # open for everyone
