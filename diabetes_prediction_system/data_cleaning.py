from diabetes_prediction_system.config import *


class Numberic:
    
    def __init__(self,df):
        self.df = df 
        
    
    def zeros(self):
        
        for i in self.df.columns:
            zero = self.df[self.df[i] ==0]
            nonzero = self.df.shape[0]
            print(f'missing/zero {i} : {zero.shape[0]}, percentage : {round((zero.shape[0] / nonzero) * 100)}%')
    
    def greet(self):
        print('hello!')
    
    def mean(self,col):
        
        print('Mean :',self.df[col].mean())
    
    def median(self,col):
        print('Median :',self.df[col].median())
    
    def mode(self,col):
        print('Mode :',self.df[col].mode())
    
    def distri_plot(self,column):
        
        print('skewness :',self.df[column].skew())
        sns.displot(x=self.df[column])
        

        
    
    
class Filling_numeric(Numberic):
    
    def fill_mean_(self,df,column):
        
        mean_ = df[column].mean()
        df[column] = df[column].replace(0,mean_)
        
        return df
    
    def fill_median(self,df,column):
        
        median_ = df[column].median()
        df[column] = df[column].replace(0,median_)
    
        return df

    def fill_mode(self,df,column):
        
        mode_ = df[column].mode()
        df[column] = df[column].replace(0,mode_)
    
        return df
    
    def knn_imputer(self,df,column):
        pass


class Type_conv:
    
    def __init__(self,df):
        self.df = df
    
    def type_(self,col):
        print(f'{col} data-type is {self.df[col]}')
    
    def to_int(self,col):
    
        self.df[col] = self.df[col].astype(int)
        print(f'{col} is converted to int')
    
    def to_float(self,col):
        self.df[col] = self.df[col].astype(float)
        print(f'{col} is converted to float')
    
    def to_lower(self,col):
        self.df[col] = self.df[col].astype(str)
        print(f'{col} is converted to lower')
    
    def to_bool(self,col):
        self.df[col] = self.df[col].astype(bool)
        print(f'{col} is converted to boolean')
        
# class for outliers and removing outliers

class Outlier:
    
    def __init__(self,df):
        
        self.df = df
    
    def check_outlier(self,col):
        
        plt.figure(figsize=(6,4))
        sns.boxplot(self.df[col])
        plt.ylabel(col)
        plt.title(f'Outlier of plot {col}')
        plt.show()
    
    def count_outlier(self,col):
        Q1 = self.df[col].quantile(0.25)
        Q3 = self.df[col].quantile(0.75)
        IQR = Q3 - Q1

        # formula for calulating lower bound and upper bound
        lower =  Q1 - (1.5 * IQR)
        upper =  Q3 + (1.5 * IQR)
        
        # condition
        low_cnt = len(self.df[self.df[col] < lower])
        upper_cnt = len(self.df[self.df[col] > upper])
        
        #printing the result
        print('column :',col)
        print('lower count:',low_cnt)
        print('upper cnt:',upper_cnt)
        print('total outlier count:',low_cnt + upper_cnt)
             
    def remove_outlier(self):
        pass