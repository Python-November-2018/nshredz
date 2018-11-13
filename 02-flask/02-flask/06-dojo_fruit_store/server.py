from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    item_count = int(request.form['strawberry']) + int(request.form['raspberry']) + int    (request.form['apple'])
    print(item_count)
    return render_template("checkout.html", item_count=item_count)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    