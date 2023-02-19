from flask import Flask, Response, render_template
import requests

app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/nature')
def nature():
  return render_template('nature.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)

