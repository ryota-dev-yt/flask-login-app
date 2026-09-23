import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from flask import session, flash

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

LOGIN_EMAIL = "example@example.com"
LOGIN_PW = "password"

@app.route('/')
def index():
    if session.get('logged_in'):
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email == LOGIN_EMAIL and password == LOGIN_PW:
            session['logged_in'] = True
            flash('Login successful!')
            return redirect(url_for('index'))
        else:
            flash('Login failed. Please check your email and password.','error')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You have been logged out.')
    return redirect(url_for('login'))