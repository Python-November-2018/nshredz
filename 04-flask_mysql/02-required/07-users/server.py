# TODO
#  split SQL to helper file, finish checking existing email, vald inputs for update page

from flask import Flask, redirect, request, render_template, session, flash
from mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
SCHEMA = ("users07")

app = Flask(__name__)
app.secret_key = "afsjk39"
mysql = connectToMySQL(SCHEMA)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    mysql = connectToMySQL(SCHEMA)
    query = "SELECT id, CONCAT(first_name, ' ', last_name) AS 'Full Name', email, created_at FROM users;"
    users = mysql.query_db(query)

    return render_template("users.html", users=users)

@app.route('/users/new', methods=['GET','POST'])
def new():
    return render_template("new.html")

@app.route('/users/<id>', methods=['GET'])
def users_show(id):
    mysql = connectToMySQL(SCHEMA)
    query = "SELECT id, CONCAT(first_name, ' ', last_name) AS 'Full Name', email, created_at FROM users WHERE id = %(id)s;"
    data = {
        'id': id
    }
    users = mysql.query_db(query, data)
    
    return render_template("user_info.html", users=users)

@app.route('/users/<id>/destroy', methods=['GET'])
def destroy(id):
    mysql = connectToMySQL(SCHEMA)
    query = "DELETE FROM users WHERE id = %(id)s;"
    data = {
        "id": id
    }
    user = mysql.query_db(query, data)
    
    return redirect("/users")

@app.route('/users/<id>/edit', methods=['GET'])
def users_edit(id):
    mysql = connectToMySQL(SCHEMA)
    query = "SELECT * FROM users WHERE id = %(id)s;"
    data = {
        "id": id
    }
    user = mysql.query_db(query, data)
    print(user)
        
    # rember inputs to repopulate in case of flashed/error, do not remember passwd
    session['first_name'] = user[0]['first_name']
    session['last_name'] = user[0]['last_name']
    session['email'] = user[0]['email']
    session['id'] = id

    return render_template("user_edit.html", user=user)

@app.route("/users/edit_complete", methods=['GET','POST'])
def edit_complete():
    # make sure email isn't already taken
    # mysql = connectToMySQL(SCHEMA)
    # query = "SELECT * FROM users WHERE email = %(email)s;"    
    # data = { 
    #     "email" : session['email']
    # }
    # result = mysql.query_db(query, data)
    # print(result)
    # if result:
    #     flash("Email address already exists!", "email")
    # # verify other things
    # if len(session['email']) < 1:
    #     flash("Email can not be empty", "email")
    # elif not EMAIL_REGEX.match(session['email']):
    #     flash("Invalid Email Address!", "email")
    # if len(session['first_name']) < 2:
    #     flash("First name must be at least 2+ characters", "first_name")
    # elif not session['first_name'].isalpha():
    #     flash("First name must be all letters", "first_name")
    # if len(session['last_name']) < 2:
    #     flash("Last name must be at least 2+ characters", "last_name")
    # elif not session['last_name'].isalpha():
    #     flash("Last name must be all letters", "last_name")

    # if '_flashes' in session.keys():
    #     return redirect("/users/" + request.form['id'])
    # else:
        session.clear()
        mysql = connectToMySQL(SCHEMA)
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email=%(email)s, updated_at=NOW() WHERE id=%(id)s;"
        data = { 
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email'],
            "id": request.form['id']
        }
        mysql.query_db(query, data)
        
        return redirect("/")

@app.route('/users/create', methods=['POST'])
def create():
    # rember inputs to repopulate in case of flashed/error, do not remember passwd
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']

    # make sure email isn't already taken
    mysql = connectToMySQL(SCHEMA)
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

    if '_flashes' in session.keys():
        return redirect("/users/new")
    else:
        session.clear()
        
        mysql = connectToMySQL(SCHEMA)
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        data = { 
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form['email']
        }

        mysql.query_db(query, data)
        
        return redirect("/users")

if __name__== "__main__":
    app.run(debug=True)