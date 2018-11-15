from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key = 'somekey'

@app.route('/', methods=['GET', 'POST'])
def index():
    if not 'total_gold' in session:
        session['total_gold'] = 0
    if not 'activities' in session:
        session['activities'] = []
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['property'] == 'farm':
        gold = random.randrange(10, 21)
        session['total_gold'] += gold
        now = datetime.datetime.now()
        result = '<p class="won">Earned ' + str(gold) + ' gold from the ' + request.form['property'] + '!    (' + now.strftime('%c') + ') </p>'
        session['activities'].append(result)
    
    if request.form['property'] == 'cave':
        gold = random.randrange(5, 11)
        session['total_gold'] += gold
        now = datetime.datetime.now()
        result = '<p class="won">Earned ' + str(gold) + ' gold from the ' + request.form['property'] + '!    (' + now.strftime('%c') + ') </p>'
        session['activities'].append(result)
    
    if request.form['property'] == 'house':
        gold = random.randrange(2, 6)
        session['total_gold'] += gold
        now = datetime.datetime.now()
        result = '<p class="won">Earned ' + str(gold) + ' gold from the ' + request.form['property'] + '!    (' + now.strftime('%c') + ') </p>'
        session['activities'].append(result)
    
    if request.form['property'] == 'casino':
        gold = random.randrange(-50, 51)
        session['total_gold'] += gold
        now = datetime.datetime.now()
        if gold > -1:
            result = '<p class="won">Earned ' + str(gold) + ' gold from the ' + request.form['property'] + '!    (' + now.strftime('%c') + ') </p>'
        else:
            result = '<p class="lost">Lost ' + str(abs(gold)) + ' gold from the ' + request.form['property'] + '!    (' + now.strftime('%c') + ') </p>'
        session['activities'].append(result)
    return redirect("/")

@app.route('/restart', methods=['POST'])
def destroy():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)   