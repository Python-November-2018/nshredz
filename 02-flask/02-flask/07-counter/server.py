from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'lkhfeslihge'

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template("index.html")

@app.route('/add_two', methods=['POST'])
def add_two():
    session['counter'] += 1
    return redirect("/")

@app.route('/destroy_session', methods=['POST'])
def destroy():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)   