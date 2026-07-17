from diabetes_prediction_system.config import *

class Bivariate_Analysis:
            
        def __init__(self,df):
            self.df = df
        
        def corr(self,col1,col2):
            
            plt.figure(figsize=(5,3))
            sns.histplot(data=self.df,x=col1,hue=col2,kde=True)
            plt.title(f'{col1} and {col2} relation ship')
            plt.show()