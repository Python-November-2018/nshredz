from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'somekey'

@app.route('/', methods=['GET', 'POST'])
def index():
    if not 'number' in session:
        session['number'] = random.randrange(0, 101)
        print(session['number'])
    else:
        if int(request.form['guess']) > session['number']:
            session['result'] = 2
        elif int(request.form['guess']) < session['number']:
            session['result'] = 1
        elif int(request.form['guess']) == session['number']:
            session['result'] = 0 
    return render_template("index.html")

@app.route('/restart', methods=['POST'])
def destroy():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)   