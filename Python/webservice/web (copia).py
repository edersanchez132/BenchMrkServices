from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def helloIndex():
    return 'Hello World'

@app.route('/greeting/<string:name>')
def greetingIndex(name: str):
    return 'Hello ' + name
    
@app.route('/fibonacci/<int:number>')
def fibonacciIndex(number: int):
    return str(fibo(number))


def fibo(n: int):
    """
    Calculating the fibonacci numbers
    """
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    
    
    
app.run(host='0.0.0.0', port=8080)
