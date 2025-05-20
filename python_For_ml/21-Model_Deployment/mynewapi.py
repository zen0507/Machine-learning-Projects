from flask import Flask,request,jsonify
import joblib
import pandas as pd

# CREATE FLASK APP
app = Flask(__name__)

# CONNECT POST API CALL ---> predict() Function
@app.route('/predict',methods=['POST'])
def predict():

    # GET JSON REQUEST
    feat_data=request.json
    # CONVERT JSON to PANDAS DF (col names)
    df = pd.DataFrame(feat_data)
    df = df.reindex(columns = col_names)
    
    #PREDICT
    prediction = list(model.predict(df))

    return jsonify({'prediction':str(prediction)})  #PREDICTION
    
# LOAD MY MODEL AND LOAD COLUMN NAMES
if __name__ == '__main__':

    model = joblib.load("final_model.pkl")
    col_names = joblib.load("col_names.pkl")

    app.run(debug=True)