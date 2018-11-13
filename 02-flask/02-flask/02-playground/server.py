from flask import Flask, render_template
app = Flask(__name__)

print('1')
print(__name__)
print('2')

@app.route('/play')
def play():
    return render_template('index.html', num=3, color='lightblue')

@app.route('/play/<num>')
def play_num(num):
    return render_template('index.html', num=int(num), color='lightblue')

@app.route('/play/<num>/<color>')

def play_num_color(num = 3, color = 'lightblue'):
    print(num)
    print(color)
    # passing num, color without argument returns error
    return render_template('index.html', num=int(num), color=color)
if __name__=="__main__":
    app.run(debug=True)    