from flask import Flask, request, render_template, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os
import urllib.request
import json
import ssl
import io
import os
import re
from os.path import join, dirname, realpath
import jinja2
jinja2.Environment().globals.update(zip=zip)


app = Flask(__name__, template_folder='templates', static_url_path='')

@app.route("/", methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route("/nearby", methods=['GET','POST'])
def nearby():
    return render_template('restaurants_nearby.html')

@app.route("/front_page", methods=['GET','POST'])
def front_page():
    return render_template('front_page.html')

@app.route("/restaurants_order", methods=['GET','POST'])
def restaurants_order():
    return render_template('restaurants_order.html')

@app.route("/before_checkout", methods=['GET','POST'])
def before_checkout():
    return render_template('before_checkout.html')

@app.route("/checkout", methods=['GET','POST'])
def checkout():
    return render_template('checkout.html')

@app.route("/register", methods=['GET','POST'])
def register():
    return render_template('register.html')

@app.route("/match", methods=['GET','POST'])
def match():
    return render_template('match.html')

@app.route("/orders", methods=['GET','POST'])
def orders():
    return render_template('orders.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
