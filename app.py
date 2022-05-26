#!/usr/bin/env python
from flask import Flask
app = Flask(_name_)
@app.route('/addition')
def addition(a,b):
    a= int(a)
    b= int(b)
    return str(a+b)+"\n"

@app.route('/subtraction')
def subtraction(c,d):
    c= int(c)
    d= int(d)
    return str(c-d)+"\n"

@app.route('/')
def intro():
    return "This is an arithmetic calculator\n"

if _name_ == '_main_':
    app.run(host='0.0.0.0')  # open for everyone
