from flask import Flask, render_template
app = Flask(__name__)

print('1')
print(__name__)
print('2')

@app.route('/play')
def play(num=3):
    return render_template('index.html', num2=3, color2='lightblue')

@app.route('/play/<num>')
def play_num(num, color2='lightblue'):
    return render_template('index.html', num2=int(num), color2='lightblue')

@app.route('/play/<num>/<color>')

def play_num_color(num, color):
    print(num)
    print(color)
    # passing num, color without argument returns error
    return render_template('index.html', num2=int(num), color2=color)
if __name__=="__main__":
    app.run(debug=True)    