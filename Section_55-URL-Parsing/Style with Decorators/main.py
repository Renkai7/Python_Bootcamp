from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        text = function()
        return f"<strong>{text}</strong>"

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        text = function()
        return f"<em>{text}</em>"

    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        text = function()
        return f"<u>{text}</u>"

    return wrapper_function


# Home route
@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://media.giphy.com/media/aCqb9YW7QclN3rtto5/giphy-downsized-large.gif" width=200>'


# Different routes using app.route decorator
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


# Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}"


if __name__ == "__main__":
    # Run app in debug to auto-reload
    app.run(debug=True)




# Note
# Running on 'Debug' mode allows updates to happen without reloading
# Debug mode: app.run(debug=True)
