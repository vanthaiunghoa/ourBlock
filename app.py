from flask import Flask,render_template,request,Response
from run_prediction import classify
import requests
import ast
import json
app = Flask(__name__)

@app.route('/post',methods=['POST'])
def post():
  form = ast.literal_eval(dict(request.form).keys()[0])
  try:
    classified,confidence = classify(form['Description'])[0]
  except Exception as e:
    print(e)
    classified,confidence = '',0
  data = {}
  data['body'] = form
  data['body']['Class'] = classified
  data['body']['Confidence'] = float(confidence)
  print(data['body']['Class'],data['body']['Confidence'])
  requests.post('https://gony0gqug0.execute-api.us-east-1.amazonaws.com/beta/post',json=data)
  resp = Response('')
  resp.headers['Access-Control-Allow-Origin'] = '*'
  return resp