from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def play():
    return render_template('index.html', x=8, y=8)

@app.route('/<x>/<y>')
def draw_board(x, y):    
    return render_template('index.html', x=int(x), y=int(y))

if __name__=="__main__":
    app.run(debug=True)    