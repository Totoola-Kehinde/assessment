from flask import Flask, render_template, request
from estimator import estimate
import json

app = Flask(__name__)


@app.route('/')
def home():
  impacts = estimate()
  return render_template('index.html')

if __name__ == "__main__":
  app.run(debug=True)