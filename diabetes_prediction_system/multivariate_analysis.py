from diabetes_prediction_system.config import *

class Multivariate_Analysis:

    def __init__(self,df):
        
        self.df = df
    
    def pairplot(self,col1,col2,col3):
        
            plt.figure(figsize=(6,4))
            plt.title(f'{col1} and {col2} realtion ship')
            sns.scatterplot(x=col1,y=col2,hue=col3,data=self.df)
            plt.show()