from flask import Flask, render_template
import requests


genderizer_url = 'https://api.genderize.io'
age_url = 'https://api.agify.io'
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/<username>')
def game(username):
    param = {
        'name' : username
    }
    gender = requests.get(genderizer_url, params=param).json()
    age = requests.get(age_url, params=param).json()
    return render_template('guess.html', name= username, gender=gender['gender'], age=age['age'])


if __name__ == '__main__':
    app.run(debug=True)
