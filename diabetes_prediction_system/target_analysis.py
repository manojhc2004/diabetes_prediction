import config
import pandas as pd
import numpy
import matplotlib.pyplot as plt
import seaborn as sns


class Target_Analysis:
    
    def __init__(self,df):
        self.df = df
        
    def diabetes_and_none(self):
        
        total = self.df.shape[0]
        print('total :',total)
    
        dia = len(self.df[self.df['Outcome'] == 1])
        nonedia = self.df.shape[0] - dia
        print('\nnumber of diabetes patients:',dia)
        print('\npercentage of diabetes patients:',dia / total * 100)
        
        print('\nnumber of none-diabetes patients:',nonedia)
        print('\npercentage of none-diabetes patients:',nonedia / total * 100)


        # for visualization 
        category = ['diabetes','nonediabetes']
        values = [dia,nonedia]
        plt.figure(figsize=(7,5))
        plt.bar(category, values, color='skyblue', edgecolor='black', width=0.6)
        plt.title('Number of diabets patients and none diabetes')
        plt.show()
        
        
    def diabetes_by_age(self):

        diabetic = self.df[self.df["Outcome"] == 1]

        age_group = pd.cut(
            diabetic["Age"],
            bins=[21,31,41,51,61,71,81],
            labels=["21-30","31-40","41-50","51-60","61-70","71-80"])

        count= diabetic.groupby(age_group, observed=False).size()

        # for visualization
        
        plt.figure(figsize=(7,5))
        sns.barplot(x=count.index, y=count.values,hue=count.index, palette='viridis',legend=False)
        plt.title("distribution of diabetes patients by Age")
        plt.xlabel('age')
        plt.ylabel('count')
        plt.show()
        
        return(count)