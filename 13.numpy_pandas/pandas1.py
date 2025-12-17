import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("13.numpy_pandas/sales_data.csv")

monthList=df['month']
tvData=df['tv'].tolist()
laptopData=df['laptop'].tolist()
phoneData=df['phone'].tolist()

plt.plot(monthList,tvData,label='tv ssales',marker='o',linewidth=3)
plt.plot(monthList,laptopData,label='laptop sales',marker='o',linewidth=3)
plt.plot(monthList,phoneData,label='phone sales',marker='o',linewidth=3)

plt.xlabel('month')
plt.ylabel('unit')
plt.legend(loc='upper left')
plt.xticks(monthList)
plt.yticks([1000,2000])
plt.title('Sales Data')
plt.show()