from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = 'foobarfoobar'
@app.route('/')
def index():
    if 'clear' in session:
        session.clear()
    
    return render_template("index.html")

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    # store comments and name to populate form later in case of error
    session['name'] = request.form['name']
    session['comments'] = request.form['comments']
    
    # length of name, empty name check
    if len(request.form['name']) == 0:
        flash('Name can not be empty')
    elif len(request.form['name']) < 3:
        flash('Please enter full name')
    if len(request.form['comments']) == 0:
        flash('Comments can not be empty')
    elif len(request.form['comments']) > 120:
        flash('Comments greater than 120 characters')
    
    if '_flashes' in session.keys():
        return redirect("/")
    
    else:
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comments'] = request.form['comments']
    
        return redirect("/result")

@app.route('/result', methods=['POST','GET'])
def process_info():
    print("Got post info")
    print(request.form)
    print(f"Name: {session['name']}")
    print(f"Location: {session['location']}")
    print(f"Language: {session['language']}")
    print(f"Comments: {session['comments']}")
    
    session['clear'] = '1'
    return render_template("result.html")

if __name__=="__main__":
    app.run(debug=True) 