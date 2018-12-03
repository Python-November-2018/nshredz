from flask import Flask, redirect, request, render_template, session, flash
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt 
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "aa3jf33jkekjekeeee"

mysql = connectToMySQL('userdb')
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    # if ('user_id' and 'first_name') in session.keys():
    #     return redirect('/home')
    # else:
    #     return render_template('index.html')
    
    if 'logged_in' in session.keys():
        return redirect('/home')
    else: 
        return render_template('index.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    # rember inputs to repopulate in case of flashed/error, do not remember passwd
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']

    # make sure email isn't already taken
    mysql = connectToMySQL("userdb")
    query = "SELECT * FROM users WHERE email = %(email)s;"    
    data = { 
        "email" : request.form['email']
    }
    result = mysql.query_db(query, data)
    print(result)
    if result:
        flash("Email address already exists!", "email")
    # verify other things
    if len(request.form['email']) < 1:
        flash("Email can not be empty", "email")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", "email")
    if len(request.form['first_name']) < 2:
        flash("First name must be at least 2+ characters", "first_name")
    elif not request.form['first_name'].isalpha():
        flash("First name must be all letters", "first_name")
    if len(request.form['last_name']) < 2:
        flash("Last name must be at least 2+ characters", "last_name")
    elif not request.form['last_name'].isalpha():
        flash("Last name must be all letters", "last_name")
    if len(request.form['password']) < 8:
        flash("Password must be at least 8 characters", "password")
    elif request.form['password'] != request.form['confirm_p']:
        flash("Passwords must match", "password_match")

    if '_flashes' in session.keys():
        return redirect("/")
    else:
        session.clear()
        # hash password, write data to DB, clear session and redirect
        #session.clear()
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)

        mysql = connectToMySQL("userdb")
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password_hash)s, NOW(), NOW());"
        data = { 
            "first_name"    : request.form['first_name'],
            "last_name"     : request.form['last_name'],
            "email"         : request.form['email'],
            "password_hash" : pw_hash
        }

        mysql.query_db(query, data)
        return redirect("/complete")

@app.route('/complete', methods=['GET', 'POST'])
def complete():
    return render_template("complete.html")

@app.route('/login', methods=["POST"])
def login():
    mysql = connectToMySQL("userdb")
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = { "email" : request.form["login"] }
    result = mysql.query_db(query, data)
    if result:
        if bcrypt.check_password_hash(result[0]['password'], request.form['log_pass']):
            session['userid'] = result[0]['id']
            session['first_name'] = result[0]['first_name']
            session['logged_in'] = '1'
            # never render on a post, always redirect!
            return redirect('/home')
    # if unable to login flash and redirect
    flash("You could not be logged in", "login")
    return redirect("/")

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return render_template("index.html")

if __name__== "__main__":
    app.run(debug=True)