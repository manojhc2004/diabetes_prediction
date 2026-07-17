from diabetes_prediction_system.config import *

class Basics:
    
    def __init__(self,df):
        self.df = df
        
    def col_row(self):
        shape = self.df.shape
        print('total columns:',shape[1])
        print('total row is:',shape[0])
            
    def describe(self):
        print('describe of data')
        print(self.df.describe())
        print()
        
    
    def missing_val(self):
        print(self.df.isna().sum())
        print()
        
        
    def age_is_greater(self,column,age):
        print(f'{age} of greater is : {self.df[self.df[column] >= age].count()}')
                                                     
    def data_type(self):
        for i in self.df.columns:
            print(f'{i} data type :{self.df[i].dtype}')