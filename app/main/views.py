from _datetime import datetime
from flask import Flask, request, render_template
from . import main

@main.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')
