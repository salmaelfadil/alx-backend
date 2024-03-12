#!/usr/bin/env python
"""Task 0 Module"""
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index() -> str:
    """renders template"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
