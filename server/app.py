#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route("/print/<parameter>")
def print_string(parameter):
    print(f"{parameter}")
    return f"{parameter}"

@app.route("/count/<int:parameter>")
def count(parameter):

    num_list_string = ""

    for num in range(0, parameter):
        num_list_string += f"{num}\n"
    return num_list_string 


@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        return f"{num1 + num2}"
    elif operation == "-":
        return f"{num1 - num2}"
    elif operation == "%":
        return f"{num1 % num2}"
    elif operation == "div":
        return f"{num1/num2}"
    elif operation == "*":
        return f"{num1 * num2}"
    else:
        return

if __name__ == '__main__':
    app.run(port=5555, debug=True)
