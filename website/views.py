from os import error
from flask import render_template, url_for, flash, redirect, session, request
from website import app
from website.models import User, db


@app.route("/")
@app.route("/home")
def home():
    if 'logged' in session:
        if session['logged']:
            return render_template('home.html')
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username=username, email=email, password=password)
        user2 = User.query.filter_by(email=email).first()
        if user2 != None:
            db.session.add(user)
            db.session.commit()
            session['logged'] = True
            session['username'] = username
            return render_template('home.html')
        else:
            flash("User already exists")
            return render_template('register.html')
    else:
        return render_template('register.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
    if user == None:
        flash("User does not exist")
        return render_template("login.html")
    else:
        if username == user.username and password == user.password:
            session['logged'] = True
            session['username'] = username
            return render_template('home.html')
        else:
            flash("Username or password is incorrect")
            return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged')
    session.pop('username')
    return render_template('home.html')
