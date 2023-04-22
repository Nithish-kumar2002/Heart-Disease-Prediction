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
    lst = []
    age = int(request.form["Enter age"])
    lst += [age]
    sex = int(request.form["Enter Sex"])
    if sex == 0:
        lst += [1 , 0]
    else:
        lst += [0 ,1 ]
    cp = int(request.form['chest pain type (4 values)'])
    if cp == 0:
        lst += [1 , 0 ,0 ,0]
    elif cp == 1:
        lst += [0 ,1 ,0 ,0]
    elif cp == 2:
        lst += [0 ,0 ,1 ,0]
    elif cp >= 3:
        lst += [0 ,0 ,0 ,1]
    trestbps = int(request.form["resting blood pressure" ])
    lst += [trestbps]
    chol = int(request.form["serum cholestoral in mg/dl"])
    lst += [chol]
    fbs = int(request.form["fasting blood sugar > 120 mg/dl"])
    if fbs == 0:
        lst += [1 , 0]
    else:
        lst += [0 , 1]
    restecg = int(request.form["resting electrocardiographic results (values 0,1,2)"])
    if restecg == 0:
        lst += [1 ,0 ,0]
    elif restecg == 1:
        lst += [0 ,1 ,0]
    else:
        lst += [0 , 0,1]
    thalach = int(request.form["maximum heart rate achieved"])
    lst += [thalach]
    exang = int(request.form["exercise induced angina"])
    if exang == 0:
        lst += [1 , 0]
    else:
        lst += [0 ,1 ]
    oldpeak = float(request.form["ST depression induced by exercise relative to rest"])
    if oldpeak == 0:
        lst += [1 , 0]
    else:
        lst += [0 ,1 ]
    slope = int(request.form["Slope (values 0,1,2)"])
    if slope == 0:
        lst += [1 ,0 ,0]
    elif slope == 1:
        lst += [0 ,1 ,0]
    else:
        lst += [0 , 0,1]
    ca = int(request.form['Ca values(0,1,2,3,4)'])
    if ca == 0:
        lst += [1 , 0 ,0 ,0,0]
    elif ca == 1:
        lst += [0 ,1 ,0 ,0,0]
    elif ca == 2:
        lst += [0 ,0 ,1 ,0,0]
    elif ca == 3:
        lst += [0 ,0 ,0 ,1,0]
    elif ca >= 3:
        lst += [0 ,0 ,0 , 0, 1]
    thal = int(request.form['Thal values(0,1,2,3)'])
    if thal == 0:
        lst += [1 , 0 ,0 ,0]
    elif thal == 1:
        lst += [0 ,1 ,0 ,0]
    elif thal == 2:
        lst += [0 ,0 ,1 ,0]
    elif thal >= 3:
        lst += [0 ,0 ,0 ,1]
    final_features = np.array([lst])
    pred = rf2.predict(final_features)
    return render_template('result.html', prediction = pred)

if __name__ == "__main__":
    app.run(debug=True)
