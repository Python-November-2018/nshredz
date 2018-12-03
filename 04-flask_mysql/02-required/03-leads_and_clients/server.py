
from flask import Flask, redirect, request, render_template, session, flash
from mysqlconnection import connectToMySQL
import datetime

app = Flask(__name__)
app.secret_key = "ajfjkekjekeeee"

mysql = connectToMySQL('lead_gen_business')

@app.route('/')
def index():
    if "begin_date" not in session:
        session["begin_date"] = "1970-01-01"

    if "end_date" not in session:
        now = datetime.datetime.now()
        session["end_date"] = now.strftime("%Y-%m-%d")

    data = {
            "begin_date": session["begin_date"],
            "end_date": session["end_date"]
    }
    print(data['begin_date'])
    print(data['end_date'])
    mysql = connectToMySQL("lead_gen_business")
    query = "SELECT CONCAT(clients.first_name, ' ', clients.last_name) as 'Name', COUNT(leads.id) AS 'Leads' FROM clients JOIN sites ON clients.id = sites.clients_id JOIN leads ON sites.id = leads.id WHERE leads.registered_datetime BETWEEN %(begin_date)s AND %(end_date)s GROUP BY clients.id"
    
    all_clients = mysql.query_db(query, data)
    return render_template('index.html', clients = all_clients)

@app.route('/date', methods=["POST"])
def date():
    session["begin_date"] = request.form["begin_date"]
    session["end_date"] = request.form["end_date"]
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)