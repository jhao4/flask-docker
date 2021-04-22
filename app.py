import time

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
  return 'Foo Bar Hello world!'

@app.route('/contributor')
def contribution():
  return 'Contributing to simple routes using Flask by @alhanson7210!'

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
