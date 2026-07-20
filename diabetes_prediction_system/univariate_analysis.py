from config import *

class Univariate_Analysis:
    
    def __init__(self,df):
        self.df = df
        #self.col = col
        #self.skewness = self.df[self.col].skew()
    
    def describe(self,col):
        
        print(f"{col} describe")
        des = self.df[col].describe()
        print("skewness :",self.df[col].skew())
        return des
    
    def missing_na_(self,col):
        
        missing = self.df[col].isna().sum()
        #return missing
        if missing > 0:
            return(f'there is missing values in the column of {col}')
        
        return 'there is no missing values'

    def kdeplot(self,col):
        
        plt.figure(figsize=(7,5))
        sns.kdeplot(
            data=self.df,
            x=self.df[col],
            hue='Outcome',
            fill=True,
            alpha=0.4,
            common_norm=False
        )
        plt.title(f"{col} distribution by Outcome")
        plt.xlabel(f"{col}")
        plt.ylabel('density')
        plt.legend(["None-diabetic","diabetic"])
        plt.show()
        
    
    def hist_plot(self,col):
        
    
        plt.figure(figsize=(7,5))
        sns.histplot(data= self.df,
                     x=self.df[col])
        plt.title(f'histo plot of:{col}')
        plt.show()

    def outlier(self,col):
        
        plt.figure(figsize=(6,4))
        sns.boxplot(self.df[col])
        plt.ylabel(col)
        plt.title(f'Outlier of plot {col}')
        plt.show()