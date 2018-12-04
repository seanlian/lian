from .settings  import hand
from flask import render_template


@hand.route('/')
def show():
    return  render_template('hand01.html')