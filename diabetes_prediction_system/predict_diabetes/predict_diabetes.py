from config import *
from pathlib import Path
import time


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "best_model" / "diabetes_predicting_model.joblib" 

model = joblib.load(MODEL_PATH)


# requried input :
"	Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age	Outcome"
class Prediciting_system:
    
    def __init__(self,userdf):
        self.userdf = userdf
    
    def make_predict(self):
        
        model_pred = model.predict(self.userdf)
        model_proba = model.predict_proba(self.userdf)
        print(model_pred)
        print(model_proba)
        
        if model_pred[0] == 1:
            print('Prediction Higer likelihood of Diabetes')
            print('Probabilty is :',round(model_proba[0][1] * 100))
        
        else:
            print('Prediction Lower likelihood of Diabetes')
            print('Probabilty is :', round(model_proba[0][0] * 100))
            
        
        
        

# collecting the input form user

if __name__=='__main__':
    
    while True:
        
        collected = False
        
        
        try:
            pregnancies = int(input('Enter you number of Pregnancies: '))
            glucose = float(input('Enter you Glucose level: '))
            bp = float(input('Enter you BloodPressure level: '))
            st = float(input('Enter you SkinThickness: '))
            insulin = float(input('Enter you Insulin level: '))
            bmi = float(input('Enter you BMI level: '))
            dpf = float(input('Enter you DiabetesPedigreeFunctionlevel: '))
            age = int(input('Enter you Age: '))
            
            # converting use data into DataFrame
            user_df = pd.DataFrame(
                [{'Pregnancies':pregnancies,
                'Glucose':glucose,
                'BloodPressure':bp,
                'SkinThickness':st,
                'Insulin':insulin,
                'BMI':bmi,
                'DiabetesPedigreeFunction':dpf,
                'Age':age
                }])

        
        # raises error is use give's wrong data/datatype
        except ValueError as valueerror:
            print(valueerror)
            print('Invalid Data-type enter')
            
        else:
            time.sleep(2)
            print('Your Data is Transforming to the Predicting Model..')
            callsystem = Prediciting_system(user_df) # calling the predicting system
            
            time.sleep(2)
            print('calling the Predicting system')
            callsystem.make_predict() # calling method of predicting system
            
            time.sleep(1)
            print('model stopped!')     # finished
            break