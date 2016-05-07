from flask import render_template, flash
from app import app
from forms import LoginForm


@app.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested - ' + form.login.data)
        return render_template('admin.html', title='People')
    return render_template('index.html',
                           title='Sigh In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS']
                           )


@app.route('/about')
def about():
    return render_template('about.html')
