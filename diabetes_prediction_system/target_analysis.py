from diabetes_prediction_system.config import *

class Target_Analysis:
    
    def __init__(self,df):
        self.df = df
        
    def nondiabetes(self):
        
        none = self.df[self.df['Pregnancies']==0]
        print('number of diabetes :',none.shape[0])
        print()
        percenatage_of_none = (none.shape[0] / self.df.shape[0]) * 100
        print("percenatage of none",percenatage_of_none)
    
    def diabetes(self):
        
        dia = self.df[self.df['Pregnancies'] > 0]
        print('number diabetes patients',dia.shape[0])
        print()
        percentage_of_dia = (dia.shape[0] / self.df.shape[0]) * 100
        print('percentage of diabetes patients',percentage_of_dia)
    


    def diabetes_by_age(self):
            diabetic = self.df[self.df["Outcome"] == 1]
            return diabetic.groupby(
                pd.cut(diabetic["Age"], bins=[21,31,41,51,61,71,81])
            ).size()