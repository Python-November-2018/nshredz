from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def process_info():
    print("Got post info")
    print(request.form)
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']
    print(f"Name: {request.form['name']}")
    print(f"Location: {request.form['location']}")
    print(f"Language: {request.form['language']}")
    print(f"Comments: {request.form['comments']}")
    #return redirect('/')
    return render_template("result.html")

if __name__=="__main__":
    app.run(debug=True) 