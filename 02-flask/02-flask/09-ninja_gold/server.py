from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

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
    location_map = {
        "farm": random.randrange(10, 21),
        "cave": random.randrange(5, 11),
        "house": random.randrange(2, 6),
        "casino": random.randrange(-50, 51)
    }

    gold = location_map[request.form['property']]
    session['total_gold'] += gold

    activity = {}
    if gold >= 0:
        activity['css_class'] = "won"
        activity['content'] = "Won {} gold from the {}! ({})".format(str(abs(gold)),  request.form['property'], datetime.now().strftime('%c'))
    else:
        activity['css_class'] = "lost"
        activity['content'] = "Lost {} gold from the {}! ({})".format(str(abs(gold)),  request.form['property'], datetime.now().strftime('%c'))

    # if request.form['property'] == 'farm':
    #     gold = random.randrange(10, 21)
    #     session['total_gold'] += gold
    #     result = '<p class="won">Earned ' + str(gold) + ' gold from the ' + request.form['property'] + '!    (' + datetime.now().strftime('%c') + ') </p>'
    
    # elif request.form['property'] == 'cave':
    #     gold = random.randrange(5, 11)
    #     session['total_gold'] += gold
    #     result = '<p class="won">Earned ' + str(gold) + ' gold from the ' + request.form['property'] + '!    (' + datetime.now().strftime('%c') + ') </p>'
    
    # elif request.form['property'] == 'house':
    #     gold = random.randrange(2, 6)
    #     session['total_gold'] += gold
    #     result = '<p class="won">Earned ' + str(gold) + ' gold from the ' + request.form['property'] + '!    (' + datetime.now().strftime('%c') + ') </p>'
    
    # elif request.form['property'] == 'casino':
    #     gold = random.randrange(-50, 51)
    #     session['total_gold'] += gold
    #     if gold > -1:
    #         result = '<p class="won">Earned ' + str(gold) + ' gold from the ' + request.form['property'] + '!    (' + datetime.now().strftime('%c') + ') </p>'
    #     else:
    #         # result = '<p class="lost">Lost ' + str(abs(gold)) + ' gold from the ' + request.form['property'] + '!    (' + datetime.now().strftime('%c') + ') </p>'
    #         result = '<p class="lost">Lost {} gold from the {}! ({})</p>'.format(str(abs(gold)),  request.form['property'], datetime.now().strftime('%c'))
    session['activities'].append(activity)
    return redirect("/")

@app.route('/restart', methods=['POST'])
def destroy():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)   