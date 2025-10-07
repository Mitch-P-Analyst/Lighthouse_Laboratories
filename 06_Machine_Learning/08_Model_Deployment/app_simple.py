from flask import render_template, request, jsonify, Flask
import flask
import numpy as np
import traceback #allows you to send error to user
import pickle
import pandas as pd

# App definition
app = Flask(__name__)

# importing models
with open('pipeline.pkl', 'rb') as f:
   pipeline = pickle.load(f)

#webpage

@app.route('/')
def welcome():
   return "Good Morning! You can use this Flask App for California Housing Price Prediction, just send a POST request!"

@app.route('/predict', methods=['POST','GET'])
def predict():
   if flask.request.method == 'GET':
      return "Please use a POST request to get predictions"

   if flask.request.method == 'POST':
      try:
        input_data = request.json
        input_df = pd.DataFrame(input_data)
        print(input_df)
        prediction = list(pipeline.predict(input_df.values))

        return jsonify({"prediction":prediction})
      except:
         return jsonify({"trace": traceback.format_exc()})

if __name__ == "__main__":
   app.run()