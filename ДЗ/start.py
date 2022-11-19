from flask import Flask, request
from fib import fibonacci


app = Flask(__name__)


@app.route('/')
def hello_world():
	return "Hello, world"

@app.route('/fibonacci')
def print_fibonacci1():
	n = request.args.get("n")
	return " ".join(map(str, fibonacci(int(n))))


if __name__ == '__main__':
	app.run()