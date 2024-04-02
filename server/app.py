#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return f'<p>{text}</p>'


@app.route('/count/<int:num>')
def count(num):
    return '<br>'.join(str(i) for i in range  (num))
   

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation,num2):
    if operation == 'add':
        result = num1 + num2
    elif operation == 'sub':
        result = num1 - num2
    elif operation == 'multiplication':
        result =  num1 * num2
    elif operation == 'division':
        if num2 != 0:
            result = num1/num2
        else:
            return 'cannot divide by zero'
    elif operation == '%':
        if num2 == 0:
            return 'Cannot divide by zero.'
        result = num1 % num2
    else:
        return'operation not supported'
    return f'{num1} {operation} {num2} = {result}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
