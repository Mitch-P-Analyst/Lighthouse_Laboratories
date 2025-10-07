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
    return render_template('index_cool.html')

@app.route('/predict', methods=['POST','GET'])
def predict():
   if flask.request.method == 'GET':
       inputs = {
        'MedInc': float(request.args.get('MedInc')),
        'HouseAge': float(request.args.get('HouseAge')),
        'AveRooms': float(request.args.get('AveRooms')),
        'AveBedrms': float(request.args.get('AveBedrms')),
        'Population': float(request.args.get('Population')),
        'AveOccup': float(request.args.get('AveOccup')),
        'Latitude': float(request.args.get('Latitude')),
        'Longitude': float(request.args.get('Longitude'))
    }
       prediction = pipeline.predict([list(inputs.values())])
       prediction = [p*100000 for p in prediction]  # Convert to 100K USD
       print(prediction)
       return render_template('predict_cool.html', prediction=prediction[0], inputs=inputs)

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