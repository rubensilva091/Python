from flask import Flask
app = Flask(__name__)



def make_bold(function):
    def bold():
        string = function()
        newstring = '<b>' + string + '</b>'
        return newstring
    return bold

def make_italic(function):
    def italic():
        string = function()
        newstring = '<em>' + string + '</em>'
        return newstring
    return italic

def make_underline(function):
    def underline():
        string = function()
        string= '<u>' +string+'</u>'
        return string
    return underline

@app.route('/')
@make_bold
@make_italic
@make_underline
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
