#!/usr/bin/env python3
"""Simple Flask Application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    GET root
    renders 0-index.html
    """
    return render_template('0-index.html')
