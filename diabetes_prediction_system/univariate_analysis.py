from diabetes_prediction_system.config import *

class Univariate_Analysis:
    
    def __init__(self,df,col):
        self.df = df
        self.col = col
        self.skewness = self.df[self.col].skew()
    
    def describe(self):
        
        des = self.df[self.col].describe()
        return des
    
    def missing_na_(self):
        
        missing = self.df[self.col].isna().sum()
        #return missing
        if missing > 0:
            return(f'there is missing values in the column of {self.col}')
        
        return 'is there missing values'
    
    def dist_plot(self):
        
        
        print('skewness is :',self.skewness)
        
        plt.figure(figsize=(6,4))
        sns.displot(x=self.df[self.col])
        plt.title(f'Distribuion plot of:{self.col}')
        plt.show()

    
    def hist_plot(self):
        
        print('skewness is :',self.skewness)
        plt.figure(figsize=(6,4))
        sns.displot(x=self.df[self.col])
        plt.title(f'Distribuion plot of:{self.col}')
        plt.show()

    def outlier(self):
        
        plt.figure(figsize=(6,4))
        sns.boxplot(self.df[self.col])
        plt.ylabel(self.col)
        plt.title(f'Outlier of plot {self.col}')
        plt.show()