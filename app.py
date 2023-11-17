from flask import Flask, render_template, request
from flask import Flask, request, render_template
from matplotlib import scale
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler




app = Flask(__name__)



# page principalegi
@app.route('/')
def home():
    return render_template('index.html')



@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/contact')
def contact_us():
    return render_template('contact_us.html')


@app.route('/breast_cancer',methods=['POST','GET'])
def breast_cancer():
     concavity_se = request.form.get('concavity_se')
     radius_mean = request.form.get('radius_mean')
     texture_mean = request.form.get('texture_mean')
     perimeter_mean = request.form.get('perimeter_mean')
     area_mean = request.form.get('area_mean')
     smoothness_mean = request.form.get('smoothness_mean')
     compactness_mean = request.form.get('compactness_mean')
     concavity_mean = request.form.get('concavity_mean')
     concave_points_mean = request.form.get('concave_points_mean')
     symmetry_mean = request.form.get('symmetry_mean')
     fractal_dimension_mean = request.form.get('fractal_dimension_mean')
     radius_se = request.form.get('radius_se')
     texture_se = request.form.get('texture_se')
     perimeter_se = request.form.get('perimeter_se')
     area_se = request.form.get('area_se')
     smoothness_se = request.form.get('smoothness_se')
     compactness_se = request.form.get('compactness_se')
     concave_points_se = request.form.get('concave_points_se')
     symmetry_se = request.form.get('symmetry_se')
     fractal_dimension_se = request.form.get('fractal_dimension_se')
     radius_worst = request.form.get('radius_worst')
     texture_worst = request.form.get('texture_worst')
     perimeter_worst = request.form.get('perimeter_worst')
     area_worst = request.form.get('area_worst')
     smoothness_worst = request.form.get('smoothness_worst')
     compactness_worst = request.form.get('compactness_worst')
     concavity_worst = request.form.get('concavity_worst')
     concave_points_worst = request.form.get('concave_points_worst')
     symmetry_worst = request.form.get('symmetry_worst')
     fractal_dimension_worst = request.form.get('fractal_dimension_worst')
   

      # Vérifier et traiter les valeurs None
    
     concavity_se = float(concavity_se) if concavity_se is not None else 0
     radius_mean = float(radius_mean) if radius_mean is not None else 0.0
     texture_mean = float(texture_mean) if texture_mean is not None else 0.0
     perimeter_mean =float(perimeter_mean) if perimeter_mean is not None else 0.0
     area_mean = float(area_mean) if area_mean is not None else 0.0
     smoothness_mean = float(smoothness_mean) if smoothness_mean is not None else 0.0
     compactness_mean = float(compactness_mean) if compactness_mean is not None else 0.0
     concavity_mean = float(concavity_mean) if concavity_mean is not None else 0.0
     concave_points_mean = float(concave_points_mean) if concave_points_mean is not None else 0.0
     symmetry_mean = float(symmetry_mean) if symmetry_mean is not None else 0.0
     fractal_dimension_mean =float(fractal_dimension_mean) if fractal_dimension_mean is not None else 0.0
     radius_se =float(radius_se) if radius_se is not None else 0.0
     texture_se =float(texture_se) if texture_se is not None else 0.0
     perimeter_se = float(perimeter_se) if perimeter_se is not None else 0.0
     area_se = float(area_se) if area_se is not None else 0.0
     smoothness_se = float(smoothness_se) if smoothness_se is not None else 0.0
     compactness_se =float(compactness_se) if compactness_se is not None else 0.0
     concave_points_se = float(concave_points_se) if concave_points_se is not None else 0.0
     symmetry_se = float(symmetry_se) if symmetry_se is not None else 0.0
     fractal_dimension_se = float(fractal_dimension_se) if fractal_dimension_se is not None else 0.0
     radius_worst = float(radius_worst) if radius_worst is not None else 0.0
     texture_worst = float(texture_worst) if texture_worst is not None else 0.0
     perimeter_worst = float(perimeter_worst) if perimeter_worst is not None else 0.0
     area_worst =float(area_worst) if area_worst is not None else 0.0
     smoothness_worst = float(smoothness_worst) if smoothness_worst is not None else 0.0
     compactness_worst = float(compactness_worst) if compactness_worst is not None else 0.0
     concavity_worst = float(concavity_worst) if concavity_worst is not None else 0.0
     concave_points_worst = float(concave_points_worst) if concave_points_worst is not None else 0.0
     symmetry_worst = float(symmetry_worst) if symmetry_worst is not None else 0.0
     fractal_dimension_worst = float(fractal_dimension_worst) if fractal_dimension_worst is not None else 0.0
   
     
     tab = (radius_mean, texture_mean ,perimeter_mean ,  area_mean ,  smoothness_mean  ,compactness_mean,concavity_mean ,concave_points_mean ,
     symmetry_mean ,fractal_dimension_mean,radius_se,texture_se ,perimeter_se,area_se ,smoothness_se ,compactness_se, concavity_se, concave_points_se ,
     symmetry_se ,fractal_dimension_se , radius_worst , texture_worst , perimeter_worst , area_worst , smoothness_worst , compactness_worst ,
     concavity_worst ,concave_points_worst ,symmetry_worst,fractal_dimension_worst) 
     

     
     
     d_arr = np.array(tab)
     res_arr = d_arr.reshape(1, -1)

     loaded_modelbc = joblib.load('breastcancer_model')

     pred = loaded_modelbc.predict(res_arr)
     if pred == [0]:
        pred='Malignant Tumor'
     else:
        pred='Benign Tumor'

     
    
     
          
     return render_template('breast_cancer.html',predictionbc=pred)


@app.route('/heart_attact', methods=['POST','GET'])
def heart_attact():
    
     age = request.form.get('Age')
     gender = request.form.get('Gender')
     impulse = request.form.get('Impulse')
     pressure_high = request.form.get('pressure_high')
     pressure_low = request.form.get('pressure_low')
     glucose = request.form.get('glucose')
     kcm = request.form.get('kcm')
     troponin = request.form.get('troponin')

      # Vérifier et traiter les valeurs None
     age = int(age) if age is not None else 0
     gender = 1 if gender == 'M' else 0 if gender == 'F' else 0
     impulse = float(impulse) if impulse is not None else 0.0
     pressure_high = float(pressure_high) if pressure_high is not None else 0.0
     pressure_low = float(pressure_low) if pressure_low is not None else 0.0
     glucose = float(glucose) if glucose is not None else 0.0
     kcm = float(kcm) if kcm is not None else 0
     troponin = float(troponin) if troponin is not None else 0.0
     
     tab = [age, gender, impulse, pressure_high, pressure_low, glucose, kcm, troponin]
     data = []

     for index, value in enumerate(tab):
        if index == 1:
        # Modifier la valeur à cet index
            if value == 'M':
                data.append(1)
            else:
                data.append(0)
        else:
        # Laisser les autres valeurs inchangées
            data.append(value)

     datas= [int(data[0]),int(data[1]),float(data[2]),float(data[3]),float(data[4]),int(data[5]),float(data[6]),float(data[7])]
     dataset = np.array([datas])
     print("dataset yo",datas)
     
     
     loaded_model = joblib.load('model_Heart')
     prediction = loaded_model.predict(dataset)
     
    
     return render_template('heart_attact.html',prediction=prediction[0])


@app.route('/skin_cancer')
def skin_cancer():
    return render_template('skin_cancer.html')


@app.route('/diabetes',methods=['POST','GET'])
def diabetes():
     ages = request.form.get('ages')
     Pregnancies = request.form.get('Pregnancies')
     glucoses = request.form.get('glucoses')
     blood_pressure = request.form.get('blood_pressure')
     skin_Thickness = request.form.get('skin_Thickness')
     insulin = request.form.get('insulin')
     bmi = request.form.get('bmi')
     diabetes_Pedigree_Function = request.form.get('diabetes_Pedigree_Function')

      # Vérifier et traiter les valeurs None
     ages = int(ages) if ages is not None else 0
     Pregnancies = float(Pregnancies) if Pregnancies is not None else 0.0
     glucoses = float(glucoses) if glucoses is not None else 0.0
     blood_pressure = float(blood_pressure) if blood_pressure is not None else 0.0
     skin_Thickness = float(skin_Thickness) if skin_Thickness is not None else 0.0
     insulin = float(insulin) if insulin is not None else 0.0
     bmi = float(bmi) if bmi is not None else 0
     diabetes_Pedigree_Function = float(diabetes_Pedigree_Function) if diabetes_Pedigree_Function is not None else 0.0
     
     tab1= (Pregnancies,glucoses, blood_pressure, skin_Thickness, insulin,bmi, diabetes_Pedigree_Function,ages)
     tab_arr = np.array(tab1)
     tab_res = tab_arr.reshape(1, -1)
    #  scaler = StandardScaler()
    #  std_data = scaler.transform(tab_res)
     print('le tableau reshape',ages)
     print('le tableau reshape',tab_arr)
     print('le tableau reshape',tab_res)

     loaded_modelbc = joblib.load('ken_diabetes_model')

     pred1 = loaded_modelbc.predict(tab_res)
     if pred1[0] == [0]:
        pred1='NEGATIF'
     else:
        pred1='POSITIF'
     return render_template('diabetes.html',prediction=pred1)















if __name__ == '__main__':
    app.run(debug=True)
