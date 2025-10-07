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
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
   if flask.request.method == 'GET':
       MedInc = float(request.args.get('MedInc'))
       HouseAge = float(request.args.get('HouseAge'))
       AveRooms = float(request.args.get('AveRooms'))
       AveBedrms = float(request.args.get('AveBedrms'))
       Population = float(request.args.get('Population'))
       AveOccup = float(request.args.get('AveOccup'))
       Latitude = float(request.args.get('Latitude'))
       Longitude = float(request.args.get('Longitude'))
       prediction = pipeline.predict([[MedInc, HouseAge, AveRooms, AveBedrms,
                                       Population, AveOccup, Latitude, Longitude]])
       return str(f"Prediction is : ${prediction[0]*100000:.2f}") # Price is in 100K USD

   if flask.request.method == 'POST':
      try:
        input_df = pd.DataFrame(request.json)
        print(input_df)
        prediction = list(pipeline.predict(input_df.values))

        return jsonify({"prediction":prediction})
      except:
         return jsonify({"trace": traceback.format_exc()})

if __name__ == "__main__":
   app.run()