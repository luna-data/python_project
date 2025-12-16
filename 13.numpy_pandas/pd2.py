import pandas as pd

data=pd.DataFrame({
    'Name':['Kim','lee','Park'],
    'Age':[25,30,22],
    'Gender':['Female','Male','Female']

})

data.to_csv('data.csv',index=False)
data.to_excel('data.xlsx',index=False)