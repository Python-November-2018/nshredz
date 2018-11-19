from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'foobarfsdfoobar'
@app.route('/')
def index():
    if 'clear' in session:
        session.clear()
    return render_template("index.html")

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']

    # length of name, empty name check
    if len(request.form['first_name']) < 1:
        flash('First name can not be empty')
    if len(request.form['last_name']) < 1:
        flash('Last name can not be empty')
    if len(request.form['email']) < 1:
        flash('Email can not be empty')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    if len(request.form['password']) < 1:
        flash("Password can not be empty")
    elif len(request.form['password']) < 8:
        flash("Password must be at least 8 characters")
    elif request.form['password'] != request.form['confirm_password']:
        flash("Passwords do not match", 'error')
    elif not re.search(r'[A-Z]', request.form['password']):
        flash("Password needs at least one uppercase letter")
    elif not re.search(r'[a-z]', request.form['password']):
        flash("Password needs at least one lowercase letter")
    if '_flashes' in session.keys():
        return redirect("/")
    else:    
        return redirect("/complete")

@app.route('/complete', methods=['GET', 'POST'])
def complete():
    print('complete')

    session['clear'] = '1'
    return render_template("complete.html")

if __name__=="__main__":
    app.run(debug=True) 