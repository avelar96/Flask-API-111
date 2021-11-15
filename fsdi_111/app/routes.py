from flask import Flask  # From the flask module import the Flask class

# We are intstatiating our Flask class into our app variable
app = Flask(__name__)


@app.route("/")            # A decorator that creates a new HTTP path
def index():
    return"<h1>Hello, world!</h1>"


@app.route("/users/martin")
def about_martin():
    me = {
        "first_name": "Martin",
        "Last_name": "Avelar",
        "Hobbies": "Hiking",
        "active": True
    }

    return me


@app.route("/greeting/<name>")
def print_name(name):
    return "<h1>Hello, %s!</h1>" % name


@app.route("/square/<int:num>")
def square_num(num):
    return "<h1>That number, squared is :%s </h1>" % (num**2)


# def myfunction(anotherfunction):
#   does something here
#   result = anotherfunction()
#   does soemthing else here
#   return result

# map:
# when people request "/"
# call the function index
