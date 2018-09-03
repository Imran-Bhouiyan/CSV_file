import matplotlib.pyplot as plt
import csv
import pandas as pd



data=pd.read_csv('test.csv',sep=',',header=None,index_col=0)

data.plot(kind='bar')


plt.ylabel('Pass Student')
plt.xlabel('Total student')
plt.title('Students Mark')
#plt.legend()
plt.show()

        
        
        
    
        
        
