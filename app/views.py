from app import app, db, lm
from flask import  render_template, flash, request, redirect, session, url_for, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from forms import LoginForm, RegistrationForm
from models import User

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Nick' }
    posts = [
        {
            'author': {'nickname': 'John'},
            'body':'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'Ololo cooool'
        }
    ]
    return render_template("index.html",
        title = 'Home',
        posts = posts,
        user = user)

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        #remember = request.form['remember_me']

        registered_user = User.query.filter_by(email=email, password=password).first()
        if registered_user is None:
            flash('username or password is invalid', 'error')
            return redirect(url_for('login'))
        login_user(registered_user)
        flash('Logged in successfully')
        return redirect(url_for('index'))
    return render_template("login.html", form = form)

@app.route('/registration', methods = ['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        user = User(form.nickname.data, form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration')
        return redirect(url_for('login'))
    return render_template('registration.html', form=form)