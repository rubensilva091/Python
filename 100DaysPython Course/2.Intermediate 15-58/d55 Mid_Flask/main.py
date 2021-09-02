import random
from flask import Flask
app = Flask(__name__)

number_gif = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'
low_gif='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'
correct_gif='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'
high_gif='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'


random_number = random.randint(0, 9)



@app.route('/<int:n>')
def game(n):
    if (n<random_number):
        return (f'<h1 style="color:#FF0000">Too Low bruuuh</h1><img src="{low_gif}"">')
    elif (n>random_number):
        return (f'<h1 style="color:#6F69AC">Too High bruuuh</h1><img src="{high_gif}"">')
    else:
        return (f'<h1 style="color:#95DAC1">YOU GOT IT BRUUH</h1><img src="{correct_gif}"">')

@app.route('/')
def hello():
    return (f'<h1>Guess the number between 0 n 9</h1><img src="{number_gif}"">')





if __name__ == '__main__':
    app.run(debug=True)
