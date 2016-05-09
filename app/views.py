from flask import request, render_template, redirect, url_for
from app import app
from app import get_user_cred, ADMINS


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        correct_user = get_user_cred(request.form.get('login'), request.form.get('password'))
        if correct_user:
            if request.form.get('login') in ADMINS:
                return render_template('admin.html')
        else:
            return redirect(url_for('home'))
    return render_template('index.html', title='Sigh In')


@app.route('/about')
def about():
    return render_template('about.html')
