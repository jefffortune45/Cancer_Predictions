from flask import Flask, render_template, request
from flask import Flask, request, render_template
import numpy as np
import joblib

import pickle

app = Flask(__name__)



# page principale
@app.route('/')
def home():
    return render_template('index.html')



@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/contact')
def contact_us():
    return render_template('contact_us.html')


@app.route('/breast_cancer')
def breast_cancer():
    return render_template('breast_cancer.html')


@app.route('/heart_attact',methods=['POST'])
def heart_attact():
     age = request.form.get('Age')
     gender = request.form.get('Gender')
     impulse = request.form.get('Impulse')
     pressure_high = request.form.get('pressure_high')
     pressure_low = request.form.get('pressure_low')
     glucose = request.form.get('glucose')
     kcm = request.form.get('kcm')
     troponin = request.form.get('troponin')
     
     tab = [age, gender, impulse, pressure_high, pressure_low, glucose, kcm, troponin]
     data = []
     for i in tab:
         if i == 'M':
             i=1
         else:
             i=0
         data.append(i)
     dataset = np.array([data])
     #prediction =dataset[1]
     #load model to make prediction
     loaded_model = joblib.load('model_Heart')
     prediction = loaded_model.predict(dataset)
     
    
     return render_template('heart_attact.html',prediction=prediction)


@app.route('/skin_cancer')
def skin_cancer():
    return render_template('skin_cancer.html')

















if __name__ == '__main__':
    app.run(debug=True)
