from flask import Flask, render_template

app = Flask(__name__)

#used this one https://colorhunt.co/palette/0023660f52bafa8072ffdab9

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)