from config import *

class Multivariate_Analysis:

    def __init__(self,df):
        
        self.df = df
    
    def pairplot(self,col1,col2,col3):
        
            plt.figure(figsize=(6,4))
            sns.boxplot(data=self.df,
                        x=col1,
                        y=col2,
                        hue=col3)
    
    
    def threerelation(self,col1,col2,col3):
        
        fig = plt.figure(figsize=(8,6))
        ax = fig.add_subplot(111, projection='3d')
       
        ax.scatter(
            self.df[col1],
            self.df[col2],
            self.df[col3],
            c = self.df["Outcome"])

        ax.set_xlabel(col1, labelpad=15)
        ax.set_ylabel(col2, labelpad=15)
        ax.set_zlabel(col3, labelpad=15)

        #ax.view_init(elev=25, azim=35)

        plt.title(f"3D Scatter Plot: {col1} vs {col2} vs {col3}")
        plt.tight_layout()
        plt.show()