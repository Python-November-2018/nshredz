from flask import Flask, redirect, request, render_template, session, flash
from mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "ajf33jkekjekeeee"

mysql = connectToMySQL('emaildb')

@app.route('/')
def index():
    # if 'clear' in session:
    #     session.clear()
    
    mysql = connectToMySQL("emaildb")
    
    all_emails = mysql.query_db("SELECT * FROM emails")
    print("Fetched all friends", all_emails)
    return render_template('index.html', emails = all_emails)

@app.route('/add_email', methods=["POST"])
def add_email():
    session['email'] = request.form['email']
    print(session['email'])
    print('this is here')
    
    if len(request.form['email']) < 1:
        flash("Email can not be empty", "error")
        return redirect("/")
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", "error")
        return redirect("/")

    flash("The email address you entered " + session['email'] + " is a valid email address!", "success")

    mysql = connectToMySQL("emaildb")
    query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
    data = {
            'email': request.form['email'],
            }
    new_email_id = mysql.query_db(query, data)
    return redirect("/")

@app.route('/delete_email', methods=["GET","POST"])
def delete_email():
    print('here')
    mysql = connectToMySQL("emaildb")
    delete_ids = request.form.getlist('do_delete')
    print(delete_ids)
    query = 'DELETE FROM emails WHERE id IN (' + ','.join(map(str, delete_ids)) + ')'
    delete_them = mysql.query_db(query)
    return redirect('/')

# @app.route('/complete', methods=["GET","POST"])
# def complete():
#     print('complete')

#     session['clear'] = '1'
#     return render_template("complete.html")

if __name__== "__main__":
    app.run(debug=True)