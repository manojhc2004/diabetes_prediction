from config import *

class Bivariate_Analysis:
            
        def __init__(self,df):
            self.df = df
            
        def corr_(self,col1,col2):
            
            plt.figure(figsize=(7,5))
            sns.scatterplot(data=self.df,
                            x=self.df[col1],
                            y=self.df[col2],
                            hue=self.df['Outcome']
                            )
            plt.title(f" {col1} Vs {col2} relation")
        