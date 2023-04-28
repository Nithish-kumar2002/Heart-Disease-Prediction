import numpy as np
from flask import Flask, request, render_template, url_for
import pickle

app = Flask(__name__,static_url_path='/static')
rf2 = pickle.load(open('rf2.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response

@app.route('/predict',methods=['POST'])
def predict():
    age = int(request.form["age"])
    sex = int(request.form["sex"])
    cp = int(request.form['chest pain type (4 values)'])
    trestbps = int(request.form["resting blood pressure" ])
    chol = int(request.form["serum cholestoral in mg/dl"])
    fbs = int(request.form["fasting blood sugar > 120 mg/dl"])
    restecg = int(request.form["resting electrocardiographic results (values 0,1,2)"])
    thalach = int(request.form["maximum heart rate achieved"])
    exang = int(request.form["exercise induced angina"])
    oldpeak = float(request.form["ST depression induced by exercise relative to rest"])
    slope = int(request.form["Slope (values 0,1,2)"])
    ca = int(request.form['Ca values(0,1,2,3,4)'])
    thal = int(request.form['Thal values(0,1,2,3)'])
   
    
    final_features = np.array([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
    pred = rf2.predict(final_features.reshape(1, -1))
    return render_template('result.html', prediction = pred)

if __name__ == "__main__":
    app.run(debug=True)