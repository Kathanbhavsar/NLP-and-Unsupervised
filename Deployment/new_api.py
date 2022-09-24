from flask import Flask,request,jsonify
import joblib
import pandas as pd


#Create FLASK APP
app = Flask(__name__)


#CONNECT POST API CALL --> predict() Function
@app.route('/predict',methods=['POST'])
def predict():
    #Get a json req
    feature_data = request.json
    #Convert to pd
    df = pd.DataFrame(feature_data)
    df = df.reindex(columns=col_names)
    #predict
    prediction = list(model.predict(df))
    return jsonify({'prediction':str(prediction)})

##Load my model
if __name__ == '__main__':
    model = joblib.load('final_model.pkl')
    col_names = joblib.load('/Users/kathanbhavsar/Desktop/Unsupervised Algorithms/NLP-and-Unsupervised/Deployment/column_name.pkl')
    app.run(debug=True)