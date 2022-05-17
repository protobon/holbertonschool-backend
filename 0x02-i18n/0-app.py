#!/usr/bin/env python3
"""Flask app"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

@app.route('/')
def index():
    render_template('0-index.html')
