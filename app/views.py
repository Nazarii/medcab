from flask import render_template, flash, redirect
from app import app
from forms import LoginForm


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested - ' + form.login.data)
        return render_template('admin.html', title='People')
    return render_template('login.html',
                            title = 'Sigh In',
                            form = form,
                            providers = app.config['OPENID_PROVIDERS'])
